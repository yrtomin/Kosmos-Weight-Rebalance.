# Weight Changelog

Total changes: **270** (126 changed, 144 new vs. vanilla)

🔴 red = weight increased &nbsp;&nbsp; 🟢 green = weight decreased &nbsp;&nbsp; percentage shown is the change relative to the baseline value

## Table of Contents

- [AnimalPartWeapon](#animalpartweapon) (5)
- [Bag](#bag) (59)
- [BrokenWeapon](#brokenweapon) (6)
- [Bug](#bug) (4)
- [Communications](#communications) (3)
- [Container](#container) (75)
- [CookingWeapon](#cookingweapon) (3)
- [Gardening](#gardening) (2)
- [GardeningWeapon](#gardeningweapon) (2)
- [Household](#household) (4)
- [Junk](#junk) (3)
- [JunkWeapon](#junkweapon) (5)
- [Material](#material) (41)
- [Memento](#memento) (5)
- [SportsWeapon](#sportsweapon) (5)
- [ToolWeapon](#toolweapon) (5)
- [Water](#water) (1)
- [Weapon](#weapon) (9)
- [WeaponCrafted](#weaponcrafted) (32)
- [WeaponPart](#weaponpart) (1)

## AnimalPartWeapon

```diff
+ Base.AnimalBone            Animal Bone                   0.45 -> 0.30  (-33.3%)
+ Base.BoneClub              Bone Club                     0.50 -> 0.35  (-30.0%)
+ Base.BoneClub_Spiked       Bone Club with Spikes         0.50 -> 0.40  (-20.0%)
+ Base.LargeBoneClub         Sturdy Bone Club              1.00 -> 0.50  (-50.0%)
+ Base.LargeBoneClub_Spiked  Sturdy Bone Club with Spikes  1.00 -> 0.55  (-45.0%)
```

## Bag

```diff
+ Base.Bag_AmmoBox                  Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_308              Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_38               Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_44               Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_45               Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_9mm              Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_Hunting          Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_Mixed            Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_AmmoBox_ShotgunShells    Ammunition Box             1.0 -> 0.80  (-20.0%)
+ Base.Bag_RifleCaseCloth           Cloth Gun Case             1.0 -> 0.60  (-40.0%)
+ Base.Bag_RifleCaseCloth2          Cloth Gun Case             1.0 -> 0.60  (-40.0%)
+ Base.Bag_RifleCaseClothCamo       Cloth Gun Case             1.0 -> 0.60  (-40.0%)
+ Base.Bag_ShotgunCaseCloth         Cloth Gun Case             1.0 -> 0.60  (-40.0%)
+ Base.Bag_ShotgunCaseCloth2        Cloth Gun Case             1.0 -> 0.60  (-40.0%)
+ Base.Bag_PicnicBasket             Picnic Basket              1.5 -> 0.50  (-66.7%)
+ Base.Bag_BirthdayBasket           Basket                     1.5 -> 0.50  (-66.7%)
+ Base.Bag_GardenBasket             Garden Basket              1.5 -> 0.50  (-66.7%)
+ Base.Bag_TrumpetCase              Trumpet Case               1.0 -> 0.80  (-20.0%)
+ Base.Bag_FluteCase                Flute Case                 1.0 -> 0.30  (-70.0%)
+ Base.Bag_BowlingBallBag           Bowling Ball Bag           1.0 -> 0.50  (-50.0%)
+ Base.Toolbox_Mechanic             Toolbox                    2.0 -> 1.50  (-25.0%)
+ Base.Bag_JanitorToolbox           Toolbox                    2.0 -> 1.50  (-25.0%)
+ Base.Bag_CraftedFramepack_Large3  Large Framepack            4.0 -> 2.00  (-50.0%)
+ Base.Bag_CraftedFramepack_Large2  Framepack                  3.0 -> 1.60  (-46.7%)
+ Base.Bag_CraftedFramepack_Large   Simple Framepack           2.0 -> 1.30  (-35.0%)
+ Base.Bag_TarpFramepack_Large      Simple Framepack           2.0 -> 1.30  (-35.0%)
+ Base.Bag_TarpFramepack_Small      Small Simple Framepack     1.5 -> 1.00  (-33.3%)
+ Base.Bag_CraftedFramepack_Small   Small Simple Framepack     1.5 -> 1.00  (-33.3%)
+ Base.Bag_HideSlingBag             Hide Sling Bag             0.8 -> 0.5   (-37.5%)
+ Base.Bag_TarpSlingBag             Tarp Sling Bag             0.8 -> 0.3   (-62.5%)
+ Base.Bag_SheetSlingBag            Sheet Sling Bag            0.8 -> 0.2   (-75.0%)
+ Base.Bag_HydrationBackpack        Hydration Pack             1.0 -> 0.80  (-20.0%)
+ Base.Bag_HydrationBackpack_Camo   Hydration Pack             1.0 -> 0.90  (-10.0%)
+ Base.Bag_FishingBasket            Fishing Basket             1.5 -> 0.40  (-73.3%)
+ Base.Bag_ClothSatchel_Burlap      Crafted Burlap Satchel     1.0 -> 0.60  (-40.0%)
+ Base.Bag_ClothSatchel_Cotton      Crafted Cotton Satchel     1.0 -> 0.60  (-40.0%)
+ Base.Bag_ClothSatchel_Denim       Crafted Denim Satchel      1.0 -> 0.60  (-40.0%)
+ Base.Bag_ClothSatchel_DenimBlack  Crafted Denim Satchel      1.0 -> 0.60  (-40.0%)
+ Base.Bag_ClothSatchel_DenimLight  Crafted Denim Satchel      1.0 -> 0.60  (-40.0%)
+ Base.Bag_HideSatchel              Crafted Hide Satchel       1.0 -> 0.60  (-40.0%)
+ Base.Bag_Satchel                  Satchel                    1.0 -> 0.60  (-40.0%)
+ Base.Bag_Satchel_Leather          Leather Satchel            1.0 -> 0.60  (-40.0%)
+ Base.Bag_Satchel_Mail             Mail Satchel               1.0 -> 0.60  (-40.0%)
+ Base.Bag_Satchel_Medical          Medical Satchel            1.0 -> 0.60  (-40.0%)
+ Base.Bag_Satchel_Military         Military Satchel           1.0 -> 0.60  (-40.0%)
+ Base.Bag_SatchelPhoto             Satchel                    1.0 -> 0.60  (-40.0%)
+ Base.Bag_Schoolbag                Small Backpack             1.0 -> 0.60  (-40.0%)
+ Base.Bag_Schoolbag_Kids           Small Backpack             1.0 -> 0.60  (-40.0%)
+ Base.Bag_Schoolbag_Medical        Small Backpack             1.0 -> 0.60  (-40.0%)
+ Base.AmmoStrap_Brown_Bullets      Bullets Bandolier          1.0 -> 0.20  (-80.0%)
+ Base.AmmoStrap_Brown_Shells       Shells Bandolier           1.0 -> 0.20  (-80.0%)
+ Base.AmmoStrap_Bullets            Bullets Bandolier          1.0 -> 0.20  (-80.0%)
+ Base.AmmoStrap_Bullets_308        Bullets Bandolier          1.0 -> 0.20  (-80.0%)
+ Base.AmmoStrap_Shells             Shells Bandolier           1.0 -> 0.20  (-80.0%)
+ Base.Bag_ChestRig                 Chest Rig                  1.0 -> 0.5   (-50.0%)
+ Base.Bag_ChestRig_Tarp            Tarp Chest Rig             1.0 -> 0.3   (-70.0%)
+ Base.Bag_ALICE_BeltSus            ALICE Belt and Suspenders  1.0 -> 0.60  (-40.0%)
+ Base.Bag_ALICE_BeltSus_Camo       ALICE Belt and Suspenders  1.0 -> 0.60  (-40.0%)
+ Base.Bag_ALICE_BeltSus_Green      ALICE Belt and Suspenders  1.0 -> 0.60  (-40.0%)
```

## BrokenWeapon

```diff
- Base.Sword_Scrap_Broken  Broken Scrap Metal Sword  0.60 -> 0.65  (+8.3%)
- Base.ShortSword_Scrap    Scrap Metal Shortsword    0.70 -> 0.80  (+14.3%)
- Base.Sword_Broken        Broken Sword              0.50 -> 0.55  (+10.0%)
+ Base.CrudeSword_Broken   Broken Simple Sword       0.65 -> 0.60  (-7.7%)
- Base.Katana_Broken       Broken Katana             0.50 -> 0.55  (+10.0%)
+ Base.BaseballBat_Broken  Broken Baseball Bat       0.60 -> 0.40  (-33.3%)
```

## Bug

```diff
+ Base.Specimen_Beetles      Specimen Case - Beetles      1.0 -> 0.20  (-80.0%)
+ Base.Specimen_Butterflies  Specimen Case - Butterflies  1.0 -> 0.20  (-80.0%)
+ Base.Specimen_Centipedes   Specimen Jar - Centipedes    1.0 -> 0.20  (-80.0%)
+ Base.Specimen_Insects      Specimen Case - Insects      1.0 -> 0.20  (-80.0%)
```

## Communications

```diff
+ Base.TvAntique     Antique Television               10.0 -> 5.00  (-50.0%)
+ Base.TvBlack       ValuTech Television              10.0 -> 5.00  (-50.0%)
+ Base.TvWideScreen  Premium Technologies Television  10.0 -> 9.00  (-10.0%)
```

## Container

```diff
+ Base.RevolverCase1                                 Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.RevolverCase2                                 Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.RevolverCase3                                 Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.PistolCase1                                   Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.PistolCase2                                   Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.PistolCase3                                   Handgun Case                      0.5  -> 0.30  (-40.0%)
+ Base.Bag_ProtectiveCase                            Protective Case                   1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCase_Survivalist                Protective Case                   1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCase_Tools                      Protective Case                   1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall                       Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Armorer               Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Electronics           Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_FirstAid              Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_KeyCutting            Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Pistol1               Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Pistol2               Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Pistol3               Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Revolver1             Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Revolver2             Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Revolver3             Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_Survivalist           Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_WalkieTalkie          Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseSmall_WalkieTalkiePolice    Small Protective Case             1.0  -> 0.80  (-20.0%)
+ Base.Bag_ProtectiveCaseMilitary                    Protective Military Case          1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseMilitary_Medical            Protective Case - Military        1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseMilitary_Tools              Protective Case - Military        1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseSmallMilitary               Small Protective Military Case    1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseSmallMilitary_FirstAid      Small Protective Case - Military  1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseSmallMilitary_Pistol1       Small Protective Case - Military  1.0  -> 0.90  (-10.0%)
+ Base.Bag_ProtectiveCaseSmallMilitary_WalkieTalkie  Small Protective Case - Military  1.0  -> 0.90  (-10.0%)
+ Base.Toolbox                                       Toolbox                           2.0  -> 1.50  (-25.0%)
+ Base.Toolbox_Farming                               Toolbox                           2.0  -> 1.50  (-25.0%)
+ Base.Toolbox_Fishing                               Toolbox                           2.0  -> 1.50  (-25.0%)
+ Base.Toolbox_Gardening                             Toolbox                           2.0  -> 1.50  (-25.0%)
+ Base.Toolbox_Wooden                                Wooden Toolbox                    1.0  -> 0.50  (-50.0%)
+ Base.FirstAidKit                                   First Aid Kit                     1.0  -> 0.40  (-60.0%)
+ Base.FirstAidKit_New                               First Aid Kit                     1.0  -> 0.40  (-60.0%)
+ Base.FirstAidKit_NewPro                            First Aid Kit                     1.0  -> 0.40  (-60.0%)
+ Base.FirstAidKit_Military                          First Aid Kit - Military          0.3  -> 0.25  (-16.7%)
+ Base.FirstAidKit_Camping_New                       First Aid Kit - Camping           0.3  -> 0.10  (-66.7%)
+ Base.FirstAidKit_Camping                           First Aid Kit - Camping           0.3  -> 0.10  (-66.7%)
+ Base.Cooler                                        Cooler                            1.5  -> 1.00  (-33.3%)
+ Base.Cooler_Beer                                   Cooler                            1.5  -> 1.00  (-33.3%)
+ Base.Cooler_Meat                                   Cooler                            1.5  -> 1.00  (-33.3%)
+ Base.Cooler_Seafood                                Cooler                            1.5  -> 1.00  (-33.3%)
+ Base.Cooler_Soda                                   Cooler                            1.5  -> 1.00  (-33.3%)
+ Base.Suitcase                                      Suitcase                          3.0  -> 1.40  (-53.3%)
+ Base.Briefcase                                     Briefcase                         1.5  -> 0.80  (-46.7%)
+ Base.Briefcase_Money                               Briefcase                         1.5  -> 0.80  (-46.7%)
+ Base.Tacklebox                                     Tacklebox                         1.5  -> 0.50  (-66.7%)
+ Base.TakeoutBox_Chinese                            Chinese Takeout Container         0.3  -> 0.05  (-83.3%)
+ Base.TakeoutBox_Styrofoam                          Takeout Container                 0.3  -> 0.05  (-83.3%)
+ Base.Cashbox                                       Cashbox                           0.5  -> 0.20  (-60.0%)
+ Base.CigarBox                                      Cigar Box                         0.5  -> 0.20  (-60.0%)
+ Base.CigarBox_Gaming                               Cigar Box                         0.5  -> 0.20  (-60.0%)
+ Base.CigarBox_Keepsakes                            Cigar Box                         0.5  -> 0.20  (-60.0%)
+ Base.CigarBox_Kids                                 Cigar Box                         0.5  -> 0.20  (-60.0%)
+ Base.CookieJar                                     Cookie Jar                        1.0  -> 0.40  (-60.0%)
- Base.Hatbox                                        Hatbox                            0.15 -> 0.25  (+66.7%)
- Base.Humidor                                       Humidor                           0.15 -> 0.20  (+33.3%)
+ Base.Parcel_ExtraLarge                             Parcel - Extra Large              1.0  -> 0.60  (-40.0%)
+ Base.Parcel_Large                                  Parcel - Large                    1.0  -> 0.40  (-60.0%)
+ Base.Parcel_Medium                                 Parcel - Medium                   1.0  -> 0.30  (-70.0%)
+ Base.Parcel_Small                                  Parcel - Small                    1.0  -> 0.20  (-80.0%)
+ Base.Parcel_ExtraSmall                             Parcel - Extra Small              1.0  -> 0.10  (-90.0%)
+ Base.ProduceBox_ExtraLarge                         Produce Box - Extra Large         1.0  -> 0.60  (-40.0%)
+ Base.ProduceBox_Large                              Produce Box - Large               1.0  -> 0.40  (-60.0%)
+ Base.ProduceBox_Medium                             Produce Box - Medium              1.0  -> 0.30  (-70.0%)
+ Base.ProduceBox_Small                              Produce Box - Small               1.0  -> 0.20  (-80.0%)
+ Base.ProduceBox_ExtraSmall                         Produce Box - Extra Small         1.0  -> 0.10  (-90.0%)
+ Base.Present_ExtraLarge                            Gift - Extra Large                1.0  -> 0.60  (-40.0%)
+ Base.Present_Large                                 Gift - Large                      1.0  -> 0.40  (-60.0%)
+ Base.Present_Medium                                Gift - Medium                     1.0  -> 0.30  (-70.0%)
+ Base.Present_Small                                 Gift - Small                      1.0  -> 0.20  (-80.0%)
+ Base.Present_ExtraSmall                            Gift - Extra Small                1.0  -> 0.10  (-90.0%)
```

## CookingWeapon

```diff
+ Base.RollingPin         Rolling Pin   0.45 -> 0.40  (-11.1%)
+ Base.MeatCleaverForged  Meat Cleaver  0.60 -> 0.50  (-16.7%)
+ Base.MeatCleaver        Meat Cleaver  0.60 -> 0.50  (-16.7%)
```

## Gardening

```diff
+ Base.Scythe        Scythe  1.50 -> 1.40  (-6.7%)
+ Base.ScytheForged  Scythe  1.50 -> 1.40  (-6.7%)
```

## GardeningWeapon

```diff
+ Base.HandScytheForged  Hand Scythe  0.50 -> 0.40  (-20.0%)
+ Base.HandScythe        Hand Scythe  0.50 -> 0.40  (-20.0%)
```

## Household

```diff
- Base.MarkerBlack  Marker - Black  0.01 -> 0.02  (+100.0%)
- Base.MarkerBlue   Marker - Blue   0.01 -> 0.02  (+100.0%)
- Base.MarkerGreen  Marker - Green  0.01 -> 0.02  (+100.0%)
- Base.MarkerRed    Marker - Red    0.01 -> 0.02  (+100.0%)
```

## Junk

```diff
- Base.Pop2Empty  Pop Can  0.04 -> 0.05  (+25.0%)
- Base.Pop3Empty  Pop Can  0.04 -> 0.05  (+25.0%)
- Base.PopEmpty   Pop Can  0.04 -> 0.05  (+25.0%)
```

## JunkWeapon

```diff
- Base.SpadeHead                Spade Head                 0.50 -> 0.60  (+20.0%)
- Base.TableLeg                 Antique Table Leg          0.60 -> 0.70  (+16.7%)
+ Base.TableLeg_Broken          Broken Table Leg           0.45 -> 0.35  (-22.2%)
+ Base.FieldHockeyStick_Broken  Broken Field Hockey Stick  0.45 -> 0.35  (-22.2%)
+ Base.CanoePadelX2_Broken      Broken Canoe Paddle        0.45 -> 0.30  (-33.3%)
```

## Material

```diff
+ Base.MeatCleaverBlade             Meat Cleaver Blade                 0.45 -> 0.35  (-22.2%)
+ Base.ScytheBlade                  Scythe Blade                       0.80 -> 0.40  (-50.0%)
- Base.HandScytheBlade              Hand Scythe Blade                  0.20 -> 0.25  (+25.0%)
- Base.SpadeHead_Forged             Spade Head                         0.50 -> 0.60  (+20.0%)
+ Base.PackFrameLarge               Large Pack Frame                   1.50 -> 0.60  (-60.0%)
+ Base.PackFrame                    Pack Frame                         1.00 -> 0.40  (-60.0%)
- Base.CopperOre                    Copper Ore                         2.50 -> 2.75  (+10.0%)
- Base.PiercedSteelChunk            Steel Chunk (Pierced)              0.10 -> 0.12  (+20.0%)
- Base.PiercedSteelIngot            Steel Ingot (Pierced)              0.80 -> 1.70  (+112.5%)
- Base.SteelBlock                   Steel Block                        0.40 -> 0.60  (+50.0%)
- Base.SteelChunk                   Steel Chunk                        0.12 -> 0.15  (+25.0%)
- Base.SteelIngot                   Steel Ingot                        1.00 -> 1.80  (+80.0%)
- Base.PiercedIronIngot             Iron Ingot (Pierced)               1.20 -> 1.70  (+41.7%)
- Base.IronChunk                    Iron Chunk                         0.12 -> 0.15  (+25.0%)
- Base.PiercedIronChunk             Iron Chunk (Pierced)               0.10 -> 0.12  (+20.0%)
- Base.IronIngot                    Iron Ingot                         1.5  -> 1.80  (+20.0%)
- Base.IronOre                      Iron Ore                           0.40 -> 3.25  (+712.5%)
+ Base.ClawhammerHead               Clawhammer Head                    0.45 -> 0.30  (-33.3%)
+ Base.ClubHammerHead               Club Hammer Head                   0.65 -> 0.60  (-7.7%)
- Base.PickAxeHead                  Pick Axe Head                      1.20 -> 1.50  (+25.0%)
+ Base.FireAxeHead                  Firefighter Axe Head               0.90 -> 0.80  (-11.1%)
- Base.OldAxeHead                   Axe Head                           0.80 -> 0.85  (+6.2%)
+ Base.HandAxeHead                  Hatchet Head                       0.50 -> 0.45  (-10.0%)
- Base.MacheteBlade_NoTang          Machete Blade (No Tang)            0.30 -> 0.40  (+33.3%)
- Base.MacheteBlade                 Machete Blade                      0.35 -> 0.45  (+28.6%)
+ Base.MaceHead                     Mace Head                          0.80 -> 0.65  (-18.8%)
- Base.SwordBlade                   Sword Blade                        0.50 -> 0.80  (+60.0%)
+ Base.SwordBlade_Broken            Broken Sword Blade                 0.50 -> 0.40  (-20.0%)
- Base.SwordBlade_NoTang            Sword Blade (No Tang)              0.45 -> 0.70  (+55.6%)
+ Base.SwordBlade_Broken_NoTang     Broken Sword Blade (No Tang)       0.40 -> 0.35  (-12.5%)
- Base.CrudeBlade                   Simple Metal Blade                 0.15 -> 1.00  (+566.7%)
- Base.CrudeSwordBlade_NoTang       Simple Sword Blade (No Tang)       0.55 -> 0.90  (+63.6%)
+ Base.CrudeShortSwordBlade_NoTang  Simple Shortsword Blade (No Tang)  0.35 -> 0.30  (-14.3%)
+ Base.CrudeShortSwordBlade         Simple Shortsword Blade            0.40 -> 0.35  (-12.5%)
- Base.Katana_Blade                 Katana Blade                       0.50 -> 0.85  (+70.0%)
+ Base.Katana_Blade_Broken          Broken Katana Blade                0.50 -> 0.40  (-20.0%)
+ Base.StoneMaulHead                Stone Maul Head                    1.00 -> 0.45  (-55.0%)
+ Base.HatchetHead_Bone             Bone War Hatchet Head              0.35 -> 0.10  (-71.4%)
+ Base.StoneAxeHead                 Large Stone Axe Head               1.00 -> 0.45  (-55.0%)
+ Base.SpearHead                    Metal Spearhead                    0.40 -> 0.15  (-62.5%)
+ Base.SpearLongHead                Long Metal Spearhead               0.50 -> 0.30  (-40.0%)
```

## Memento

```diff
+ Base.Bag_DoctorBag          Doctor Bag       1.0  -> 0.50  (-50.0%)
+ Base.Bag_Satchel_Fishing    Fishing Satchel  1.0  -> 0.60  (-40.0%)
+ Base.Bag_Schoolbag_Patches  Small Backpack   1.0  -> 0.60  (-40.0%)
+ Base.Bag_Schoolbag_Travel   Small Backpack   1.0  -> 0.60  (-40.0%)
+ Base.Katana_Handle          Katana Handle    0.30 -> 0.25  (-16.7%)
```

## SportsWeapon

```diff
- Base.BaseballBat          Baseball Bat                  0.60 -> 0.80  (+33.3%)
- Base.BaseballBat_Metal    Metal Baseball Bat            0.50 -> 0.70  (+40.0%)
- Base.BaseballBat_Crafted  Crafted Baseball Bat          0.60 -> 0.80  (+33.3%)
+ Base.CanoePadel           Canoe Paddle                  0.60 -> 0.45  (-25.0%)
+ Base.CanoePadelX2         Canoe Paddle - Double-bladed  1.00 -> 0.60  (-40.0%)
```

## ToolWeapon

```diff
- Base.CrowbarForged  Crowbar     1.20 -> 1.50  (+25.0%)
- Base.Crowbar        Crowbar     1.20 -> 1.50  (+25.0%)
+ Base.PickAxe        Pickaxe     2.50 -> 2.00  (-20.0%)
+ Base.PickAxeForged  Pickaxe     2.50 -> 2.00  (-20.0%)
+ Base.LargeHook      Large Hook  0.60 -> 0.30  (-50.0%)
```

## Water

```diff
+ Base.WaterBottle  Water Bottle  0.1 -> 0.05  (-50.0%)
```

## Weapon

```diff
+ Base.Mace             Mace                   1.20 -> 0.90  (-25.0%)
+ Base.Mace_Stone       Stone Mace             1.00 -> 0.85  (-15.0%)
+ Base.LongMace_Stone   Long Stone Mace        1.40 -> 1.05  (-25.0%)
- Base.Sword            Sword                  1.00 -> 1.10  (+10.0%)
+ Base.ShortSword       Shortsword             0.60 -> 0.50  (-16.7%)
+ Base.CrudeSword       Simple Sword           1.30 -> 1.20  (-7.7%)
+ Base.CrudeShortSword  Simple Shortsword      0.70 -> 0.50  (-28.6%)
+ Base.Katana           Katana                 1.50 -> 1.10  (-26.7%)
- Base.SpearShort       Spear with Metal Head  0.70 -> 0.75  (+7.1%)
```

## WeaponCrafted

```diff
+ Base.MeatCleaver_Scrap              Scrap Metal Cleaver                    0.60 -> 0.50  (-16.7%)
- Base.Sword_Scrap                    Scrap Metal Sword                      1.10 -> 1.30  (+18.2%)
- Base.TableLeg_Nails                 Antique Table Leg with Nails           0.61 -> 0.65  (+6.6%)
- Base.TableLeg_Sawblade              Antique Table Leg with Sawblade        0.75 -> 0.85  (+13.3%)
+ Base.TableLeg_Broken_Nails          Broken Table Leg with Nails            0.45 -> 0.40  (-11.1%)
- Base.BaseballBat_Can                Baseball Bat - Can-Reinforced          0.65 -> 0.85  (+30.8%)
- Base.BaseballBat_ScrapSheet         Baseball Bat - Sheet Metal Reinforced  0.75 -> 0.95  (+26.7%)
- Base.BaseballBat_GardenForkHead     Baseball Bat with Garden Fork Head     0.90 -> 1.10  (+22.2%)
- Base.BaseballBat_Nails              Baseball Bat with Nails                0.61 -> 0.85  (+39.3%)
- Base.BaseballBat_RailSpike          Baseball Bat with Railspike            0.80 -> 1.00  (+25.0%)
- Base.BaseballBat_RakeHead           Baseball Bat with Rake Spikes          0.85 -> 1.05  (+23.5%)
- Base.BaseballBat_Sawblade           Baseball Bat with Sawblade             0.80 -> 1.00  (+25.0%)
- Base.BaseballBat_Spiked             Baseball Bat with Spikes               0.61 -> 0.85  (+39.3%)
+ Base.BaseballBat_Broken_Nails       Broken Baseball Bat with Nails         0.61 -> 0.45  (-26.2%)
- Base.BaseballBat_Metal_Bolts        Metal Baseball Bat with Bolts          0.65 -> 0.85  (+30.8%)
- Base.BaseballBat_Metal_Sawblade     Metal Baseball Bat with Sawblade       0.75 -> 0.95  (+26.7%)
- Base.Cudgel_ScrapSheet              Cudgel - Sheet Metal Reinforced        0.75 -> 1.15  (+53.3%)
- Base.Cudgel_Bone                    Cudgel with Bone Spikes                0.80 -> 1.05  (+31.2%)
- Base.Cudgel_Brake                   Cudgel with Brake Disc                 1.65 -> 1.75  (+6.1%)
- Base.Cudgel_GardenForkHead          Cudgel with Garden Fork Head           1.15 -> 1.35  (+17.4%)
- Base.Cudgel_Nails                   Cudgel with Nails                      0.80 -> 1.05  (+31.2%)
- Base.Cudgel_Sawblade                Cudgel with Sawblade                   0.95 -> 1.25  (+31.6%)
- Base.Cudgel_SpadeHead               Cudgel with Spade Head                 1.2  -> 1.4   (+16.7%)
- Base.Cudgel_Spike                   Cudgel with Spikes                     0.90 -> 1.20  (+33.3%)
- Base.StoneMaul                      Stone Maul                             0.70 -> 0.90  (+28.6%)
- Base.LongHandle_Can                 Large Handle - Can-Reinforced          0.50 -> 0.70  (+40.0%)
- Base.LongHandle_Nails               Large Handle with Nails                0.60 -> 0.70  (+16.7%)
+ Base.IceHockeyStick_BarbedWire      Ice Hockey Stick with Barbed Wire      0.85 -> 0.75  (-11.8%)
+ Base.FieldHockeyStick_Broken_Nails  Broken Field Hockey Stick with Nails   0.60 -> 0.50  (-16.7%)
+ Base.Hatchet_Bone                   Bone War Hatchet                       0.50 -> 0.30  (-40.0%)
+ Base.SpearScissors                  Spear with Scissors                    0.85 -> 0.70  (-17.6%)
- Base.SpearStone                     Spear with Stone Head                  0.70 -> 0.75  (+7.1%)
```

## WeaponPart

```diff
- Base.AmmoStraps  Ammo Straps  0.05 -> 0.20  (+300.0%)
```

