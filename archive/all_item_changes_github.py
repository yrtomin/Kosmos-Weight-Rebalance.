import os
import re

VANILLA_SCRIPTS_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\media\scripts"

# Build 42.13+ moved item names out of the old ItemName_EN.txt file and into
# ItemName.json, keyed by the item's full type (Module.ItemID) instead of
# "ItemName_ItemID". We auto-detect whichever file actually exists.
VANILLA_TRANSLATE_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\media\lua\shared\Translate\EN"

YOUR_MOD_FILE_PATH = r"B:\Dokument\Downloads\[standard] Mods\Zomboid\KosmoWeightModding\versions\1.3\KosmoWeightRebalance\Contents\mods\KosmoWeightRebalance\42\media\scripts\Kosmo_WeightChanges.txt"

# .md so GitHub renders it directly (README-style page or a committed file).
OUTPUT_FILE_PATH = r"B:\Dokument\Downloads\[standard] Mods\Zomboid\KosmoWeightModding\analysis\KosmoWeightRebalance-v1.3-masterlist.md"

# Confirmed: clothingItem XML files (media/clothing/clothingItems) hold only
# visual/model data (m_MaleModel, m_GUID, textureChoices, etc.) -- no weight
# field exists there. At runtime, the game itself silently defaults any
# clothing item with no explicit Weight in its script to 1.0. So for items
# that reference a ClothingItem and have no inline Weight, 1.0 IS the
# correct vanilla value -- no XML lookup needed.
CLOTHING_DEFAULT_WEIGHT = "1.0"

# Magnitude tiers for the emoji indicator, keyed by the minimum |% change|
# each tier covers. Markdown can't color arbitrary text, so this is the
# no-external-dependency stand-in for "redder = bigger change."
MAGNITUDE_TIERS = [
    (50.0, "🔴"),
    (25.0, "🟠"),
    (10.0, "🟡"),
    (0.0, "🟢"),
]


def strip_comments(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'//.*', '', content)
    return content


def find_blocks(text, keyword):
    """
    Manually scans `text` for blocks shaped like:
        keyword Name { ... possibly with nested { } blocks ... }
    and returns a list of (name, body) tuples.

    This replaces a naive `keyword\\s+name\\s*\\{([^}]*)\\}` regex, which
    stops at the FIRST closing brace it sees. Build 42 items very often
    contain nested blocks (Tags { ... }, BloodLocation lists, fluid
    containers, etc.), so that kind of regex silently truncates the item
    body -- and anything after the nested block (including Weight or
    DisplayName) gets lost.
    """
    results = []
    pattern = re.compile(r'\b' + re.escape(keyword) + r'\s+([A-Za-z0-9_\.]+)\s*\{', re.IGNORECASE)
    pos = 0
    n = len(text)
    while True:
        m = pattern.search(text, pos)
        if not m:
            break
        name = m.group(1)
        brace_start = m.end() - 1
        depth = 1
        i = brace_start + 1
        while i < n and depth > 0:
            c = text[i]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            i += 1
        body = text[brace_start + 1:i - 1]
        results.append((name, body))
        pos = i
    return results


def find_translation_file(translate_dir):
    """Prefer the new Build 42 ItemName.json, fall back to the legacy .txt."""
    json_path = os.path.join(translate_dir, "ItemName.json")
    txt_path = os.path.join(translate_dir, "ItemName_EN.txt")

    if os.path.exists(json_path):
        return json_path, "json (Build 42.13+ format)"
    if os.path.exists(txt_path):
        return txt_path, "legacy .txt format"
    return None, None


def load_translation_names(translate_dir):
    names = {}

    trans_file, fmt = find_translation_file(translate_dir)
    if not trans_file:
        print(f"CRITICAL WARNING: No ItemName.json or ItemName_EN.txt found in: {translate_dir}")
        return names

    print(f"Reading translations from: {trans_file} ({fmt})")

    content = ""
    for enc in ['utf-8-sig', 'utf-8', 'latin-1']:
        try:
            with open(trans_file, 'r', encoding=enc, errors='ignore') as f:
                content = f.read()
                if content:
                    break
        except Exception:
            continue

    raw_pairs = []

    if trans_file.lower().endswith('.json'):
        try:
            import json
            data = json.loads(content)
            if isinstance(data, dict):
                raw_pairs = list(data.items())
        except Exception:
            raw_pairs = []

    if not raw_pairs:
        raw_pairs = re.findall(r'"?([A-Za-z0-9_\.]+)"?\s*[:=]\s*"([^"]*)"', content)

    for key, val in raw_pairs:
        full_key = key.strip().lower()
        display_val = val.strip()

        if full_key.startswith('itemname_'):
            full_key = full_key[9:]

        if full_key in ['en', '']:
            continue

        names[full_key] = display_val

        if '.' in full_key:
            short_key = full_key.split('.')[-1]
            names.setdefault(short_key, display_val)

    print(f"Successfully indexed {len(names)} translation keys.")
    return names


def build_unified_vanilla_db():
    vanilla_db = {}
    clothing_item_ids = set()

    translations = load_translation_names(VANILLA_TRANSLATE_DIR)

    print("Scanning media/scripts directory...")
    for root, _, files in os.walk(VANILLA_SCRIPTS_DIR):
        for file in files:
            if not file.endswith('.txt'):
                continue

            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='latin-1', errors='ignore') as f:
                content = f.read()

            content = strip_comments(content)

            for module_name, module_body in find_blocks(content, 'module'):
                module_key = module_name.strip().lower()

                for raw_id, body in find_blocks(module_body, 'item'):
                    short_id = raw_id.strip().lower()
                    full_id = f"{module_key}.{short_id}"

                    found_name = translations.get(full_id) or translations.get(short_id)
                    if not found_name:
                        name_match = re.search(r'\b[Dd]isplay[Nn]ame\s*=\s*"?([^",\r\n]+)"?', body)
                        if name_match:
                            found_name = name_match.group(1).strip()

                    weight_match = re.search(r'\b[Ww]eight\s*=\s*([0-9.]+)', body)
                    found_weight = weight_match.group(1) if weight_match else None

                    category_match = re.search(r'\b[Dd]isplay[Cc]ategory\s*=\s*([A-Za-z0-9_]+)', body)
                    found_category = category_match.group(1).strip() if category_match else None

                    is_clothing = re.search(r'\b[Cc]lothing[Ii]tem\s*=\s*[A-Za-z0-9_]+', body) is not None

                    for key in {full_id, short_id}:
                        if key not in vanilla_db:
                            vanilla_db[key] = {'weight': 'N/A', 'name': 'N/A', 'category': 'Uncategorized'}
                        if found_name and found_name != "N/A":
                            vanilla_db[key]['name'] = found_name
                        if found_weight:
                            vanilla_db[key]['weight'] = found_weight
                        if found_category:
                            vanilla_db[key]['category'] = found_category
                        if is_clothing:
                            clothing_item_ids.add(key)

    defaulted = 0
    for key in clothing_item_ids:
        if vanilla_db[key]['weight'] == 'N/A':
            vanilla_db[key]['weight'] = CLOTHING_DEFAULT_WEIGHT
            defaulted += 1

    print(f"Clothing items identified: {len(clothing_item_ids)} "
          f"({defaulted} had no explicit Weight -> defaulted to {CLOTHING_DEFAULT_WEIGHT}, matching game behavior)")

    return vanilla_db


def extract_mod_items(mod_content):
    """
    Returns a list of (display_id, full_key, short_key, body) tuples.
    Handles mod files both with and without a "module { ... }" wrapper,
    and item IDs both with and without an explicit "Base." prefix.
    """
    mod_items = []
    module_blocks = find_blocks(mod_content, 'module')

    if module_blocks:
        for module_name, module_body in module_blocks:
            module_key = module_name.strip().lower()
            for raw_id, body in find_blocks(module_body, 'item'):
                raw_id = raw_id.strip()
                short_key = raw_id.lower()
                full_key = f"{module_key}.{short_key}"
                display_id = f"{module_name.strip()}.{raw_id}"
                mod_items.append((display_id, full_key, short_key, body))
    else:
        for raw_id, body in find_blocks(mod_content, 'item'):
            raw_id = raw_id.strip()
            full_key = raw_id.lower()
            short_key = raw_id.split('.')[-1].lower()
            mod_items.append((raw_id, full_key, short_key, body))

    return mod_items


def github_slug(text, used_slugs):
    """
    Mimics GitHub's heading-anchor algorithm: lowercase, strip anything
    that isn't a letter/digit/space/hyphen, collapse spaces to hyphens,
    de-duplicate repeats with -1, -2, etc.
    """
    slug = text.strip().lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)

    base_slug = slug
    counter = 1
    while slug in used_slugs:
        slug = f"{base_slug}-{counter}"
        counter += 1
    used_slugs.add(slug)
    return slug


def compute_percent(vanilla_weight_str, mod_weight_str):
    """
    % change of the mod's weight relative to vanilla. Returns
    (percent_string, direction) where direction is "up"/"down"/"same",
    handling non-numeric ("N/A") and zero-baseline cases without crashing.
    """
    try:
        vanilla_f = float(vanilla_weight_str)
        mod_f = float(mod_weight_str)
    except ValueError:
        return "n/a", "same"

    if vanilla_f == mod_f:
        return "0.0%", "same"

    if vanilla_f == 0:
        return "n/a (vanilla was 0)", ("up" if mod_f > vanilla_f else "down")

    pct = (mod_f - vanilla_f) / vanilla_f * 100
    direction = "up" if mod_f > vanilla_f else "down"
    return f"{pct:+.1f}%", direction


def magnitude_icon(percent_str):
    """
    Picks an emoji tier based on |% change|, independent of direction.
    Markdown tables can't color text directly, so this is the stand-in:
    bigger change = more intense-looking emoji.
    """
    match = re.search(r'([0-9.]+)%', percent_str)
    if not match:
        return "⚪"  # n/a / non-numeric case

    magnitude = abs(float(match.group(1)))
    for threshold, icon in MAGNITUDE_TIERS:
        if magnitude >= threshold:
            return icon
    return MAGNITUDE_TIERS[-1][1]


def process_mod_file():
    vanilla_db = build_unified_vanilla_db()

    if not vanilla_db:
        print("ERROR: Database empty.")
        return

    print("\nExtracting and formatting reference list...")

    if not os.path.exists(YOUR_MOD_FILE_PATH):
        print(f"ERROR: Mod file not found at {YOUR_MOD_FILE_PATH}")
        return

    with open(YOUR_MOD_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as infile:
        mod_content = infile.read()

    mod_content = strip_comments(mod_content)
    mod_items = extract_mod_items(mod_content)

    total = 0
    matched_names = 0
    changed_count = 0
    # category -> list of (id, name, mod_weight, vanilla_weight, direction, percent_str)
    categories = {}

    for display_id, full_key, short_key, body in mod_items:
        total += 1

        mod_weight_match = re.search(r'\b[Ww]eight\s*=\s*([0-9.]+)', body)
        mod_weight = mod_weight_match.group(1) if mod_weight_match else "N/A"

        item_info = vanilla_db.get(full_key) or vanilla_db.get(short_key) or \
            {'weight': 'N/A', 'name': 'N/A', 'category': 'Uncategorized'}
        vanilla_weight = item_info['weight']
        display_name = item_info['name']

        category_match = re.search(r'\b[Dd]isplay[Cc]ategory\s*=\s*([A-Za-z0-9_]+)', body)
        category = category_match.group(1).strip() if category_match else item_info.get('category', 'Uncategorized')

        if display_name != "N/A":
            matched_names += 1

        percent_str, direction = compute_percent(vanilla_weight, mod_weight)
        if direction == "same":
            continue  # unchanged from vanilla -- not worth listing
        changed_count += 1

        categories.setdefault(category, []).append(
            (display_id, display_name, mod_weight, vanilla_weight, direction, percent_str)
        )

    sorted_categories = sorted(categories.keys(), key=lambda c: (c == "Uncategorized", c.lower()))

    lines_by_category = {}
    used_slugs = set()
    toc_entries = []

    for category in sorted_categories:
        rows = categories[category]
        table_rows = [(item_id, name, van_wt, mod_wt, percent_str)
                      for item_id, name, mod_wt, van_wt, direction, percent_str in rows]
        lines_by_category[category] = table_rows

        slug = github_slug(category, used_slugs)
        toc_entries.append((category, slug, len(rows)))

    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as outfile:
        outfile.write("# All Item Weight Changes vs. Vanilla\n\n")
        outfile.write(f"Total mod items scanned: **{total}** &nbsp;&nbsp; "
                       f"Changed from vanilla: **{changed_count}** &nbsp;&nbsp; "
                       f"Display names resolved: **{matched_names}/{total}**\n\n")
        outfile.write("Percentage shown is the change relative to the vanilla value. "
                       "Items matching vanilla exactly are omitted. "
                       "🔴 ≥50% &nbsp; 🟠 ≥25% &nbsp; 🟡 ≥10% &nbsp; 🟢 <10% change (by magnitude, either direction)\n\n")

        outfile.write("## Table of Contents\n\n")
        for category, slug, count in toc_entries:
            outfile.write(f"- [{category}](#{slug}) ({count})\n")
        outfile.write("\n")

        for category in sorted_categories:
            outfile.write(f"## {category}\n\n")
            outfile.write("| Item ID | Display Name | Vanilla | Current | % Change |\n")
            outfile.write("|---|---|---:|---:|---:|\n")
            for item_id, name, van_wt, mod_wt, percent_str in lines_by_category[category]:
                icon = magnitude_icon(percent_str)
                # Backticks give the item ID a monospace, "code" look so it
                # stands out against the plain display name next to it.
                outfile.write(f"| `{item_id}` | {name} | {van_wt} | {mod_wt} | {icon} **{percent_str}** |\n")
            outfile.write("\n")

    print("\n==========================================")
    print("PROCESS COMPLETE!")
    print(f"Total Mod Items Extracted: {total}")
    print(f"Display Names Resolved: {matched_names}/{total}")
    print(f"Items changed from vanilla: {changed_count}")
    print(f"Categories found: {len(sorted_categories)} -> {', '.join(sorted_categories)}")
    print(f"Saved cleanly to: {OUTPUT_FILE_PATH}")
    print("==========================================")


if __name__ == "__main__":
    process_mod_file()
    input("\nPress Enter to exit...")
