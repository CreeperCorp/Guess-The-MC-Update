import random
import textwrap

# List of major Minecraft updates (Java and Bedrock Edition) with their popular names
updates = [
    {
        "name": "Nether Update",
        "version": "1.16",
        "desc": "Added new Nether biomes, Piglins, Hoglins, Striders, Netherite, ancient debris, and bastions.",
        "hint": "Introduced Netherite gear."
    },
    {
        "name": "Caves & Cliffs",
        "version": "1.17/1.18",
        "desc": "Introduced goats, axolotls, glow squid, copper, amethyst, new cave and mountain biomes, and major world generation overhaul.",
        "hint": "Goats and huge caves."
    },
    {
        "name": "The Wild Update",
        "version": "1.19",
        "desc": "Added mangrove swamps, frogs, tadpoles, allay, the Deep Dark, ancient cities, and the Warden.",
        "hint": "Introduced the Warden and mangrove swamps."
    },
    {
        "name": "Trails & Tales",
        "version": "1.20",
        "desc": "Added camels, sniffers, archaeology, cherry grove biome, bamboo wood, and hanging signs.",
        "hint": "Introduced the sniffer and archaeology."
    },
    {
        "name": "Village & Pillage",
        "version": "1.14",
        "desc": "Revamped villages, added Pillagers, raids, new villager professions, and new blocks like barrels and bells.",
        "hint": "Pillagers and raids were introduced."
    },
    {
        "name": "Update Aquatic",
        "version": "1.13",
        "desc": "Oceans were overhauled, with new mobs (dolphins, turtles), new blocks, shipwrecks, and more.",
        "hint": "This was a huge update for oceans."
    },
    {
        "name": "Buzzy Bees",
        "version": "1.15",
        "desc": "Added bees, beehives, honey blocks, and honeycomb blocks.",
        "hint": "Bzzz!"
    },
    {
        "name": "Bountiful Update",
        "version": "1.8",
        "desc": "Added ocean monuments, guardians, prismarine, banners, and rabbits.",
        "hint": "Underwater temples and guardians."
    },
    {
        "name": "Update That Changed The World",
        "version": "1.7",
        "desc": "Added many new biomes, new flowers, stained glass, and fishing overhaul.",
        "hint": "Stained glass and lots of biomes arrived."
    },
    {
        "name": "The Jungle Update",
        "version": "1.2",
        "desc": "Introduced jungles, ocelots, iron golems, redstone lamps, and new world height.",
        "hint": "Jungles, ocelots, and iron golems."
    },
    {
        "name": "Adventure Update",
        "version": "Beta 1.8/1.0",
        "desc": "Introduced creative mode, new mobs (endermen, silverfish), strongholds, The End, Ender Dragon, brewing, enchanting, and potions.",
        "hint": "Endermen and The End!"
    },
    {
        "name": "Pretty Scary Update",
        "version": "1.4",
        "desc": "Added wither, witches, bats, anvils, and command blocks.",
        "hint": "The wither and command blocks came with this update."
    },
    {
        "name": "Redstone Update",
        "version": "1.5",
        "desc": "Added hoppers, droppers, comparators, and more advanced redstone mechanics.",
        "hint": "Major advancements for redstone engineers."
    },
    {
        "name": "Horse Update",
        "version": "1.6",
        "desc": "Added horses, donkeys, mules, leads, carpets, and hay bales.",
        "hint": "Rideable mounts were introduced."
    },
    {
        "name": "Combat Update",
        "version": "1.9",
        "desc": "Shields, dual wielding, new arrows, shulkers, and End City.",
        "hint": "Shields and End City ships!"
    },
    {
        "name": "Exploration Update",
        "version": "1.11",
        "desc": "Added woodland mansions, llamas, evokers, vindicators, and the totem of undying.",
        "hint": "Woodland mansions and totem of undying."
    },
    {
        "name": "World of Color Update",
        "version": "1.12",
        "desc": "Added concrete, glazed terracotta, parrots, and advancements.",
        "hint": "Colorful new blocks and parrots!"
    },
    {
        "name": "Frostburn Update",
        "version": "1.10",
        "desc": "Added polar bears, strays, husks, magma blocks, and fossils.",
        "hint": "Cold and hot mobs and blocks."
    }
    # Add more named updates as desired!
]

print("="*60)
print("Welcome to Minecraft: Guess the Update Name!")
print("="*60)
print("I will describe a Minecraft update. Can you guess its popular name?")
print("Type 'quit' to exit at any time.")
print()

score = 0
rounds = 0

unplayed_indices = list(range(len(updates)))
random.shuffle(unplayed_indices)

while unplayed_indices:
    idx = unplayed_indices.pop()
    update = updates[idx]
    print("\n--- New Challenge! ---")
    print("Description:", textwrap.fill(update["desc"], width=70))

    guess = input("\nWhat is the popular name of this update? ").strip()
    if guess.lower() == "quit":
        print("\nThanks for playing!")
        break

    rounds += 1

    if guess.lower() == update["name"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print("Incorrect.")
        # First hint: regular hint
        print(f"\nHint 1: {update['hint']}")
        guess2 = input("Guess again: ").strip()
        if guess2.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess2.lower() == update["name"].lower():
            print("Correct! 🎉")
            score += 1
            continue

        # Second hint: version number
        print(f"\nHint 2: Version number of this update: {update['version']}")
        guess3 = input("Last try: ").strip()
        if guess3.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess3.lower() == update["name"].lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Sorry! The correct answer was: '{update['name']}'.")

    print(f"Score: {score}/{rounds}")

    if score == len(updates):
        print("\nCongratulations! You guessed every update correctly — you beat the game! 🏆")
        break

if score < len(updates):
    print(f"\nFinal Score: {score}/{rounds} rounds played.")
    print("Goodbye!")
