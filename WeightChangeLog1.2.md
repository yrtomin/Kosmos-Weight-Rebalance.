# Weight Changelog

Total changes: **347** (52 changed, 295 new vs. vanilla)

🔴 red = weight increased &nbsp;&nbsp; 🟢 green = weight decreased

## Table of Contents

- [Accessory](#accessory) (7)
- [Animal](#animal) (1)
- [Bug](#bug) (1)
- [Bunny](#bunny) (1)
- [Container](#container) (64)
- [CookingWeapon](#cookingweapon) (2)
- [Duck](#duck) (1)
- [Electronics](#electronics) (1)
- [Fishing](#fishing) (1)
- [FishingWeapon](#fishingweapon) (3)
- [Food](#food) (116)
- [Fox](#fox) (1)
- [Gardening](#gardening) (105)
- [Household](#household) (2)
- [InstrumentWeapon](#instrumentweapon) (1)
- [Junk](#junk) (2)
- [Literature](#literature) (2)
- [Material](#material) (7)
- [MaterialWeapon](#materialweapon) (1)
- [Memento](#memento) (21)
- [RecipeResource](#reciperesource) (1)
- [WaterContainer](#watercontainer) (6)

## Accessory

```diff
+ Base.Animal_BowtieGold       Bowtie                     0.5  -> 0.05
+ Base.Animal_BowtieGreen      Bowtie                     0.5  -> 0.05
+ Base.Animal_BowtieRed        Bowtie                     0.5  -> 0.05
+ Base.KnapsackSprayer         Backpack Sprayer           5.0  -> 1.5
+ Base.KnapsackSprayer_Stowed  Backpack Sprayer (Stowed)  5.0  -> 1.5
+ Base.Oxygen_Tank             Oxygen Tank                5.0  -> 2.5
+ Base.Gloves_HuntingCamo      Gloves - Hunting Camo      0.12 -> 0.10
```

## Animal

```diff
+ Base.WaterDish  Water Dish  0.3 -> 0.10
```

## Bug

```diff
+ Base.KeyRing_Bug  Key Ring - Bug  0.05 -> 0.03
```

## Bunny

```diff
+ Base.KeyRing_RabbitFoot  Key Ring - Rabbit Foot  0.1 -> 0.03
```

## Container

```diff
+ Base.Garbagebag               Garbage Bag             0.1  -> 0.05
+ Base.Bag_TrashBag             Garbage Bag             0.1  -> 0.05
+ Base.Tote                     Tote Bag                0.5  -> 0.12
+ Base.Tote_Bags                Tote Bag                0.5  -> 0.12
+ Base.Tote_Clothing            Tote Bag                0.5  -> 0.12
+ Base.Bag_Dancer               Tote Bag                0.5  -> 0.12
+ Base.GroceryBag1              Plastic Bag             0.1  -> 0.05
+ Base.GroceryBag2              Plastic Bag             0.1  -> 0.05
+ Base.GroceryBag3              Plastic Bag             0.1  -> 0.05
+ Base.GroceryBag4              Plastic Bag             0.1  -> 0.05
+ Base.GroceryBag5              Plastic Bag             0.1  -> 0.05
+ Base.GroceryBagGourmet        Plastic Bag             0.1  -> 0.05
+ Base.Plasticbag               Plastic Bag             0.1  -> 0.05
+ Base.Plasticbag_Bags          Plastic Bag             0.1  -> 0.05
+ Base.Plasticbag_Clothing      Plastic Bag             0.1  -> 0.05
+ Base.PaperBag                 Paper Bag               0.1  -> 0.08
+ Base.Paperbag_Jays            Paper Bag               0.1  -> 0.08
+ Base.Lunchbag                 Lunchbag                0.1  -> 0.08
+ Base.Bag_TarpSack             Tarp Sack               0.5  -> 0.30
+ Base.Bag_Gunny                Gunny Sack              0.5  -> 0.30
+ Base.Bag_HideSack             Hide Sack               0.5  -> 0.30
+ Base.Bag_Laundry              Laundry Bag             0.5  -> 0.30
+ Base.Bag_LaundryHospital      Laundry Bag             0.5  -> 0.30
+ Base.Bag_LaundryLinen         Laundry Bag             0.5  -> 0.30
+ Base.Bag_Mail                 Mail Bag                0.5  -> 0.30
+ Base.EmptySandbag             Sack                    0.5  -> 0.30
+ Base.WheatSack                Sack                    0.5  -> 0.30
+ Base.WheatSeedSack            Sack                    0.5  -> 0.30
+ Base.Bag_TreasureBag          Sack                    0.5  -> 0.30
+ Base.Bag_DeadMice             Sack                    0.5  -> 0.30
+ Base.Bag_DeadRats             Sack                    0.5  -> 0.30
+ Base.Bag_DeadRoaches          Sack                    0.5  -> 0.30
+ Base.SeedBag                  Pouch                   0.1  -> 0.04
+ Base.SeedBag_Farming          Pouch                   0.1  -> 0.04
+ Base.DiceBag                  Pouch                   0.1  -> 0.04
+ Base.GemBag                   Pouch                   0.1  -> 0.04
+ Base.Wallet                   Wallet                  0.2  -> 0.05
+ Base.Wallet_Female            Wallet                  0.2  -> 0.05
+ Base.Wallet_Hide              Hide Wallet             0.2  -> 0.05
+ Base.Wallet_Male              Wallet                  0.2  -> 0.05
+ Base.Handbag                  Handbag                 1.0  -> 0.40
+ Base.Purse                    Purse                   1.0  -> 0.60
+ Base.KeyRing                  Key Ring                0.05 -> 0.03
+ Base.KeyRing_CarDealer        Key Ring                0.05 -> 0.03
+ Base.KeyRing_Forged           Key Ring - Forged       0.05 -> 0.03
+ Base.KeyRing_Forged_Gold      Key Ring - Gold         0.05 -> 0.03
+ Base.KeyRing_Forged_Silver    Key Ring - Silver       0.05 -> 0.03
+ Base.KeyRing_Large            Key Ring - Large        0.05 -> 0.03
+ Base.KeyRing_SecurityPass     Security Pass Key Ring  0.05 -> 0.03
+ Base.PhotoAlbum               Photo Album             0.5  -> 0.12
+ Base.PhotoAlbum_Old           Photo Album             0.5  -> 0.12
+ Base.ToolRoll_Fabric          Tool Roll - Fabric      0.5  -> 0.20
+ Base.ToolRoll_Leather         Tool Roll - Leather     0.5  -> 0.20
+ Base.Hatbox                   Hatbox                  0.5  -> 0.15
+ Base.Humidor                  Humidor                 1.0  -> 0.15
+ Base.JewelleryBox             Jewelry Box             1.0  -> 0.30
+ Base.JewelleryBox_Fancy       Jewelry Box             1.0  -> 0.35
+ Base.SewingKit                Sewing Kit              1.0  -> 0.20
+ Base.Shoebox                  Shoebox                 0.5  -> 0.15
+ Base.PencilCase               Pencil Case             0.3  -> 0.10
+ Base.PencilCase_Gaming        Pencil Case             0.3  -> 0.10
+ Base.MakeupCase_Professional  Makeup Case             1.0  -> 0.80
+ Base.ToolRoll_Fabric          Tool Roll - Fabric      0.5  -> 0.20
+ Base.ToolRoll_Leather         Tool Roll - Leather     0.5  -> 0.20
```

## CookingWeapon

```diff
+ Base.SaucepanCopper  Copper Saucepan  0.90 -> 0.60
+ Base.Saucepan        Saucepan         0.70 -> 0.50
```

## Duck

```diff
+ Base.KeyRing_RubberDuck  Key Ring - Rubber Duck  0.05 -> 0.03
```

## Electronics

```diff
+ Base.MotionSensor  Motion Sensor  0.3 -> 0.10
```

## Fishing

```diff
+ Base.FishRoeSac  Fish Roe Sac  0.1 -> 0.05
```

## FishingWeapon

```diff
+ Base.CraftedFishingRod  Makeshift Fishing Rod     1.0 -> 0.40
+ Base.FishingRod         Fishing Rod               1.0 -> 0.40
+ Base.FishingRodBreak    Fishing Rod without Line  1.0 -> 0.20
```

## Food

```diff
- Base.Macandcheese_Box             Box of Mac and Cheese            2.00 -> 2.40
- Base.Avocado                      Avocado                          0.12 -> 0.15
- Base.Banana                       Banana                           0.12 -> 0.15
+ Base.Blackbeans                   Black Beans                      0.30 -> 0.05
+ Base.Capers                       Capers                           0.05 -> 0.03
+ Base.Carrots                      Carrots                          0.20 -> 0.10
+ Base.Cucumber                     Cucumber                         0.30 -> 0.25
+ Base.Garlic                       Garlic                           0.05 -> 0.03
+ Base.GingerPickled                Ginger (Pickled)                 0.05 -> 0.03
+ Base.Grapefruit                   Grapefruit                       0.30 -> 0.25
+ Base.GreenOnions                  Green Onions                     0.10 -> 0.05
+ Base.Greenpeas                    Green Peas                       0.20 -> 0.10
+ Base.Kale                         Kale                             0.10 -> 0.05
+ Base.Leek                         Leek                             0.20 -> 0.15
+ Base.Lime                         Lime                             0.10 -> 0.08
+ Base.Olives                       Olives                           0.05 -> 0.03
+ Base.Onion                        Onion                            0.20 -> 0.15
+ Base.Peas                         Packaged Peas                    0.20 -> 0.10
+ Base.PepperHabanero               Habanero                         0.05 -> 0.02
+ Base.PepperHabaneroDried          Habanero (Dried)                 0.02 -> 0.01
+ Base.PepperJalapeno               Jalapeno                         0.05 -> 0.03
+ Base.PepperJalapenoDried          Jalapeno (Dried)                 0.02 -> 0.01
+ Base.RedRadish                    Radish                           0.10 -> 0.05
+ Base.Seaweed                      Seaweed                          0.05 -> 0.03
+ Base.SoybeansSeed                 Soybeans (Dried)                 0.02 -> 0.01
+ Base.Spinach                      Spinach                          0.10 -> 0.05
+ Base.Squash                       Squash                           0.50 -> 0.40
+ Base.SunflowerSeeds               Sunflower Seeds                  0.05 -> 0.03
+ Base.Tomato                       Tomato                           0.20 -> 0.15
+ Base.Turnip                       Turnip                           0.20 -> 0.15
+ Base.HayTuft                      Hay                              0.40 -> 0.03
+ Base.Croissant                    Croissant                        0.1  -> 0.08
+ Base.Crackers                     Crackers                         0.1  -> 0.05
+ Base.Marshmallows                 Marshmallows                     0.1  -> 0.05
+ Base.Icing                        Icing                            0.1  -> 0.05
- Base.CerealBowl                   Bowl of Cereal                   0.50 -> 0.60
- Base.Oatmeal                      Bowl of Oatmeal                  0.50 -> 0.60
- Base.NoodleSoup                   Bowl of Noodle Soup              0.50 -> 0.60
- Base.StewBowlClay                 Bowl of Stew                     0.55 -> 0.60
+ Base.StewBowl                     Bowl of Stew                     1.0  -> 0.60
+ Base.SoupBowl                     Bowl of Soup                     1.0  -> 0.60
+ Base.SoupBowlClay                 Bowl of Soup                     1.0  -> 0.60
+ Base.WaterSaucepanPasta           Saucepan with Pasta              3.0  -> 1.2
+ Base.WaterSaucepanPastaCopper     Copper Saucepan with Pasta       3.0  -> 1.3
+ Base.WaterSaucepanRice            Saucepan with Rice               3.0  -> 1.2
+ Base.WaterSaucepanRiceCopper      Copper Saucepan with Rice        3.0  -> 1.3
+ Base.WaterPotForgedPasta          Cooking Pot with Pasta           3.0  -> 2.60
+ Base.WaterPotForgedRice           Cooking Pot with Rice            3.0  -> 2.60
+ Base.WaterPotPasta                Cooking Pot with Pasta           3.0  -> 2.60
+ Base.WaterPotRice                 Cooking Pot with Rice            3.0  -> 2.60
+ Base.PotForgedSoupRecipe          Pot of Soup                      3.0  -> 2.50
+ Base.PotForgedStew                Pot of Stew                      3.0  -> 2.50
+ Base.PotOfSoup                    Pot of Soup                      3.0  -> 2.50
+ Base.PotOfSoupRecipe              Pot of Soup                      3.0  -> 2.50
+ Base.PotOfStew                    Pot of Stew                      3.0  -> 2.50
+ Base.SugarCubes                   Sugar Cubes                      0.10 -> 0.01
+ Base.CocoaPowder                  Cocoa Powder                     1.0  -> 0.50
+ Base.Coffee2                      Coffee                           1.0  -> 0.50
+ Base.Chicken                      Chicken Leg                      0.35 -> 0.30
+ Base.TurkeyLegs                   Turkey Leg                       0.35 -> 0.30
+ Base.Pancakes                     Pancakes                         0.3  -> 0.20
+ Base.Taco                         Taco                             0.3  -> 0.20
+ Base.CabbageRoll                  Cabbage Roll                     0.3  -> 0.20
+ Base.Milk                         Milk Carton                      0.2  -> 0.08
+ Base.Milk_Personalsized           Milk - Personal-sized            0.2  -> 0.02
+ Base.MilkChocolate_Personalsized  Chocolate Milk - Personal-sized  0.2  -> 0.02
+ Base.HotDrink                     Hot Drink                        0.5  -> 0.40
+ Base.HotDrinkClay                 Hot Drink                        0.5  -> 0.40
+ Base.HotDrinkCopper               N/A                              0.5  -> 0.40
+ Base.HotDrinkGold                 N/A                              0.5  -> 0.40
+ Base.HotDrinkMetal                N/A                              0.5  -> 0.40
+ Base.HotDrinkSilver               N/A                              0.5  -> 0.40
+ Base.HotDrinkSpiffo               Hot Drink                        0.5  -> 0.40
+ Base.HotDrinkTea                  Hot Drink                        0.5  -> 0.40
+ Base.HotDrinkTeaCeramic           Hot Drink                        0.5  -> 0.40
+ Base.HotDrinkTumbler              N/A                              0.5  -> 0.40
+ Base.HotDrinkWhite                Hot Drink                        0.5  -> 0.40
+ Base.JuiceBox                     Juice Box                        0.1  -> 0.02
+ Base.JuiceBoxApple                Juice Box                        0.1  -> 0.02
+ Base.JuiceBoxFruitpunch           Juice Box                        0.1  -> 0.02
+ Base.JuiceBoxOrange               Juice Box                        0.1  -> 0.02
+ Base.BeerCan                      Beer Can                         0.3  -> 0.05
+ Base.SodaCan                      Can of Soda                      0.3  -> 0.05
+ Base.Pop                          Diet Cola                        0.3  -> 0.05
+ Base.Pop2                         Cola                             0.3  -> 0.05
+ Base.Pop3                         Ginger Ale                       0.3  -> 0.05
+ Base.PopBottle                    Orange Soda                      0.1  -> 0.08
+ Base.PopBottleRare                Bottle                           0.1  -> 0.08
+ Base.JuiceCranberry               Bottle                           0.1  -> 0.05
+ Base.JuiceFruitpunch              Bottle                           0.1  -> 0.05
+ Base.JuiceGrape                   Bottle                           0.1  -> 0.05
+ Base.JuiceLemon                   Bottle                           0.1  -> 0.05
+ Base.JuiceOrange                  Bottle                           0.1  -> 0.05
+ Base.JuiceTomato                  Bottle                           0.1  -> 0.05
+ Base.Cider                        Cider                            1.0  -> 0.40
+ Base.BeerBottle                   Beer Bottle                      0.4  -> 0.30
+ Base.BeerImported                 Imported Beer                    0.4  -> 0.30
+ Base.WineAged                     Bottle of Fine Red Wine          1.0  -> 0.30
+ Base.WineBox                      Boxed Red Wine                   0.2  -> 0.10
+ Base.WineScrewtop                 Cheap Red Wine                   1.0  -> 0.30
+ Base.Scotch                       Scotch                           1.0  -> 0.40
+ Base.Sherry                       Sherry                           1.0  -> 0.40
+ Base.Whiskey                      Bottle of Whiskey                0.7  -> 0.40
+ Base.Rum                          Rum                              1.0  -> 0.40
+ Base.Port                         Port                             1.0  -> 0.40
+ Base.Tequila                      Tequila                          1.0  -> 0.40
+ Base.Vermouth                     Vermouth                         1.0  -> 0.40
+ Base.Vodka                        Vodka                            1.0  -> 0.40
+ Base.Brandy                       Brandy                           0.5  -> 0.40
+ Base.Champagne                    Champagne                        1.0  -> 0.50
+ Base.CoffeeLiquer                 Coffee Liqueur                   1.0  -> 0.40
+ Base.Curacao                      Curacao                          1.0  -> 0.40
+ Base.Grenadine                    Grenadine                        1.0  -> 0.40
+ Base.Gin                          Gin                              1.0  -> 0.40
+ Base.WaterRationCan               Water Ration Can                 0.8  -> 0.35
+ Base.WaterRationCan_Box           Box of Water Ration Cans         4.0  -> 2.3
```

## Fox

```diff
+ Base.KeyRing_BlueFox  Key Ring - Blue Fox  0.05 -> 0.03
```

## Gardening

```diff
+ Base.BarleyBagSeed             Seed Packet - Barley              0.1  -> 0.05
+ Base.BarleySeed                Barley Seeds                      0.02 -> 0.01
+ Base.BasilBagSeed              Seed Packet - Basil               0.1  -> 0.05
+ Base.BasilSeed                 Basil Seeds                       0.02 -> 0.01
+ Base.BellPepperBagSeed         Seed Packet - Bell Pepper         0.1  -> 0.05
+ Base.BellPepperSeed            Bell Pepper Seeds                 0.02 -> 0.01
+ Base.BlackSageBagSeed          Seed Packet - Black Sage          0.1  -> 0.05
+ Base.BlackSageSeed             Black Sage Seeds                  0.02 -> 0.01
+ Base.BroadleafPlantainBagSeed  Seed Packet - Broadleaf Plantain  0.1  -> 0.05
+ Base.BroadleafPlantainSeed     Broadleaf Plantain Seeds          0.02 -> 0.01
+ Base.BroccoliBagSeed2          Seed Packet - Broccoli            0.1  -> 0.05
+ Base.BroccoliSeed              Broccoli Seeds                    0.02 -> 0.01
+ Base.CabbageBagSeed2           Seed Packet - Cabbage             0.1  -> 0.05
+ Base.CabbageSeed               Cabbage Seeds                     0.02 -> 0.01
+ Base.CarrotBagSeed2            Seed Packet - Carrot              0.1  -> 0.05
+ Base.CarrotSeed                Carrot Seeds                      0.02 -> 0.01
+ Base.CauliflowerBagSeed        Seed Packet - Cauliflower         0.1  -> 0.05
+ Base.CauliflowerSeed           Cauliflower Seeds                 0.02 -> 0.01
+ Base.ChamomileBagSeed          Seed Packet - Chamomile           0.1  -> 0.05
+ Base.ChamomileSeed             Chamomile Seeds                   0.02 -> 0.01
+ Base.ChivesBagSeed             Seed Packet - Chives              0.1  -> 0.05
+ Base.ChivesSeed                Chives Seeds                      0.02 -> 0.01
+ Base.CilantroBagSeed           Seed Packet - Cilantro            0.1  -> 0.05
+ Base.CilantroSeed              Cilantro Seeds                    0.02 -> 0.01
+ Base.ComfreyBagSeed            Seed Packet - Comfrey             0.1  -> 0.05
+ Base.ComfreySeed               Comfrey Seeds                     0.02 -> 0.01
+ Base.CommonMallowBagSeed       Seed Packet - Common Mallow       0.1  -> 0.05
+ Base.CommonMallowSeed          Common Mallow Seeds               0.02 -> 0.01
+ Base.CornBagSeed               Seed Packet - Corn                0.1  -> 0.05
+ Base.CucumberBagSeed           Seed Packet - Cucumber            0.1  -> 0.05
+ Base.FlaxBagSeed               Seed Packet - Flax                0.1  -> 0.05
+ Base.FlaxSeed                  Flax Seeds                        0.02 -> 0.01
+ Base.GarlicBagSeed             Seed Packet - Garlic              0.1  -> 0.05
+ Base.GarlicSeed                Garlic Seeds                      0.02 -> 0.01
+ Base.GrassBag                  Grass Bag                         2.0  -> 1.0
+ Base.GreenpeasBagSeed          Seed Packet - Green Peas          0.1  -> 0.05
+ Base.GreenpeasSeed             Green Peas (Dried)                0.02 -> 0.01
+ Base.HabaneroBagSeed           Seed Packet - Habanero            0.1  -> 0.05
+ Base.HabaneroSeed              Habanero Seeds                    0.02 -> 0.01
+ Base.HempBagSeed               Seed Packet - Hemp                0.1  -> 0.05
+ Base.HempSeed                  Hemp Seeds                        0.02 -> 0.01
+ Base.HopsBagSeed               Seed Packet - Hops                0.1  -> 0.05
+ Base.HopsSeed                  Hops Seeds                        0.02 -> 0.01
+ Base.JalapenoBagSeed           Seed Packet - Jalapeno            0.1  -> 0.05
+ Base.JalapenoSeed              Jalapeno Seeds                    0.02 -> 0.01
+ Base.KaleBagSeed               Seed Packet - Kale                0.1  -> 0.05
+ Base.KaleSeed                  Kale Seeds                        0.02 -> 0.01
+ Base.LavenderBagSeed           Seed Packet - Lavender            0.1  -> 0.05
+ Base.LavenderSeed              Lavender Seeds                    0.02 -> 0.01
+ Base.LeekBagSeed               Seed Packet - Leek                0.1  -> 0.05
+ Base.LeekSeed                  Leek Seeds                        0.02 -> 0.01
+ Base.LemonGrassBagSeed         Seed Packet - Lemongrass          0.1  -> 0.05
+ Base.LemonGrassSeed            Lemon Grass Seeds                 0.02 -> 0.01
+ Base.LettuceBagSeed            Seed Packet - Lettuce             0.1  -> 0.05
+ Base.LettuceSeed               Lettuce Seeds                     0.02 -> 0.01
+ Base.MarigoldBagSeed           Seed Packet - Marigold            0.1  -> 0.05
+ Base.MarigoldSeed              Marigold Seeds                    0.02 -> 0.01
+ Base.MintBagSeed               Seed Packet - Mint                0.1  -> 0.05
+ Base.MintSeed                  Mint Seeds                        0.02 -> 0.01
+ Base.OnionBagSeed              Seed Packet - Onion               0.1  -> 0.05
+ Base.OnionSeed                 Onion Seeds                       0.02 -> 0.01
+ Base.OreganoBagSeed            Seed Packet - Oregano             0.1  -> 0.05
+ Base.OreganoSeed               Oregano Seeds                     0.02 -> 0.01
+ Base.ParsleyBagSeed            Seed Packet - Parsley             0.1  -> 0.05
+ Base.ParsleySeed               Parsley Seeds                     0.02 -> 0.01
+ Base.PoppyBagSeed              Seed Packet - Poppy               0.1  -> 0.05
+ Base.PotatoBagSeed2            Seed Packet - Potato              0.1  -> 0.05
+ Base.PotatoSeed                Potato Seeds                      0.02 -> 0.01
+ Base.PumpkinBagSeed            Seed Packet - Pumpkin             0.1  -> 0.05
+ Base.RedRadishBagSeed2         Seed Packet - Radish              0.1  -> 0.05
+ Base.RedRadishSeed             Radish Seeds                      0.02 -> 0.01
+ Base.RoseBagSeed               Seed Packet - Rose                0.1  -> 0.05
+ Base.RosemaryBagSeed           Seed Packet - Rosemary            0.1  -> 0.05
+ Base.RosemarySeed              Rosemary Seeds                    0.02 -> 0.01
+ Base.RoseSeed                  Rose Seeds                        0.02 -> 0.01
+ Base.RyeBagSeed                Seed Packet - Rye                 0.1  -> 0.05
+ Base.RyeSeed                   Rye Seeds                         0.02 -> 0.01
+ Base.SageBagSeed               Seed Packet - Sage                0.1  -> 0.05
+ Base.SageSeed                  Sage Seeds                        0.02 -> 0.01
+ Base.SoybeansBagSeed           Seed Packet - Soybeans            0.1  -> 0.05
+ Base.SpinachBagSeed            Seed Packet - Spinach             0.1  -> 0.05
+ Base.SpinachSeed               Spinach Seeds                     0.02 -> 0.01
+ Base.StrewberrieBagSeed2       Seed Packet - Strawberry          0.1  -> 0.05
+ Base.StrewberrieSeed           Strawberry Seeds                  0.02 -> 0.01
+ Base.SugarBeetBagSeed          Seed Packet - Sugar Beet          0.1  -> 0.05
+ Base.SugarBeetSeed             Sugar Beet Seeds                  0.02 -> 0.01
+ Base.SunflowerBagSeed          Seed Packet - Sunflower           0.1  -> 0.05
+ Base.SweetPotatoBagSeed        Seed Packet - Sweet Potato        0.1  -> 0.05
+ Base.SweetPotatoSeed           Sweet Potato Seeds                0.02 -> 0.01
+ Base.ThymeBagSeed              Seed Packet - Thyme               0.1  -> 0.05
+ Base.ThymeSeed                 Thyme Seeds                       0.02 -> 0.01
+ Base.TobaccoBagSeed            Seed Packet - Tobacco             0.1  -> 0.05
+ Base.TobaccoSeed               Tobacco Seeds                     0.02 -> 0.01
+ Base.TomatoBagSeed2            Seed Packet - Tomato              0.1  -> 0.05
+ Base.TomatoSeed                Tomato Seeds                      0.02 -> 0.01
+ Base.TurnipBagSeed             Seed Packet - Turnip              0.1  -> 0.05
+ Base.TurnipSeed                Turnip Seeds                      0.02 -> 0.01
+ Base.WatermelonBagSeed         Seed Packet - Watermelon          0.1  -> 0.05
+ Base.WatermelonSeed            Watermelon Seeds                  0.02 -> 0.01
+ Base.WheatBagSeed              Seed Packet - Wheat               0.1  -> 0.05
+ Base.WheatSeed                 Wheat Seeds                       0.02 -> 0.01
+ Base.WildGarlicBagSeed         Seed Packet - Wild Garlic         0.1  -> 0.05
+ Base.WildGarlicSeed            Wild Garlic Seeds                 0.02 -> 0.01
+ Base.ZucchiniBagSeed           Seed Packet - Zucchini            0.1  -> 0.05
+ Base.ZucchiniSeed              Zucchini Seeds                    0.02 -> 0.01
```

## Household

```diff
+ Base.CleaningLiquid2  Cleaning Liquid  0.40 -> 0.30
+ Base.Bleach           Bleach           0.2  -> 0.15
```

## InstrumentWeapon

```diff
+ Base.Violin  Violin  0.7 -> 0.50
```

## Junk

```diff
+ Base.Perfume  Perfume  0.20 -> 0.10
+ Base.Cologne  Cologne  0.2  -> 0.10
```

## Literature

```diff
+ Base.HottieZ_New  HottieZ            0.1  -> 0.08
+ Base.HottieZ      Magazine: HottieZ  0.10 -> 0.08
```

## Material

```diff
+ Base.Log                 Log                   9.0  -> 5.0
+ Base.LogStacks3          Log Stack - Three     9.0  -> 8.0
+ Base.LogStacks4          Log Stack - Four      12.0 -> 10.0
+ Base.StoneBlock          Stone Block           0.60 -> 0.30
+ Base.Aluminum            Aluminum Foil         0.15 -> 0.10
+ Base.SmallGoldBar        Small Gold Ingot      20   -> 0.40
+ Base.SmithingHammerHead  Smithing Hammer Head  0.80 -> 0.50
```

## MaterialWeapon

```diff
+ Base.Stone2  Stone  1.0 -> 0.50
```

## Memento

```diff
+ Base.Paperbag_Spiffos      Paper Bag                           0.1  -> 0.08
+ Base.KeyRing_Bass          Key Ring - Bass                     0.05 -> 0.03
+ Base.KeyRing_Clover        Key Ring - Four-Leaf Clover         0.05 -> 0.03
+ Base.KeyRing_EagleFlag     Key Ring - American Eagle           0.05 -> 0.03
+ Base.KeyRing_EightBall     Key Ring - Eight Ball               0.05 -> 0.03
+ Base.KeyRing_Hotdog        Key Ring - Hotdog                   0.05 -> 0.03
+ Base.KeyRing_Kitty         Key Ring - Kitty                    0.05 -> 0.03
+ Base.KeyRing_Nolans        Key Ring - Nolan's Used Cars        0.05 -> 0.03
+ Base.KeyRing_Panther       Key Ring - Panther                  0.05 -> 0.03
+ Base.KeyRing_PineTree      Key Ring - Pine Tree                0.05 -> 0.03
+ Base.KeyRing_PrayingHands  Key Ring - Praying Hands            0.05 -> 0.03
+ Base.KeyRing_Racing12      Key Ring - 12                       0.05 -> 0.03
+ Base.KeyRing_Racing34      Key Ring - 34                       0.05 -> 0.03
+ Base.KeyRing_Racing58      Key Ring - 58                       0.05 -> 0.03
+ Base.KeyRing_RainbowStar   Key Ring - Rainbow Star             0.05 -> 0.03
+ Base.KeyRing_Sexy          Key Ring - Sexy                     0.05 -> 0.03
+ Base.KeyRing_Spiffos       Key Ring - Spiffos                  0.05 -> 0.03
+ Base.KeyRing_StinkyFace    Key Ring - Stinky Face              0.05 -> 0.03
+ Base.KeyRing_WestMaple     Key Ring - West Maple Country Club  0.05 -> 0.03
+ Base.BunnySuitPink         Bunny Suit                          0.25 -> 0.08
+ Base.BunnySuitBlack        Bunny Suit                          0.25 -> 0.08
```

## RecipeResource

```diff
+ Base.FlaxBagSeed_Empty  Empty Seed Packet - Flax  0.02 -> 0.01
```

## WaterContainer

```diff
+ Base.Canteen               Canteen           0.2  -> 0.15
+ Base.CanteenClay           Canteen           0.2  -> 0.15
+ Base.CanteenMilitaryFull   Canteen           0.2  -> 0.15
+ Base.Sportsbottle          Sports Bottle     0.1  -> 0.08
+ Base.WaterDispenserBottle  Dispenser Bottle  2.0  -> 0.80
- Base.BeerCanEmpty          Beer Can          0.02 -> 0.05
```

