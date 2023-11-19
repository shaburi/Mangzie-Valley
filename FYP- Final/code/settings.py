from pygame.math import Vector2

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

# Sound
VOLUME = .1  # between 0 and 1

# overlay positions 
OVERLAY_POSITIONS = {
    'tool': (40, SCREEN_HEIGHT - 15),
    'seed': (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
    'left': Vector2(-50, 40),
    'right': Vector2(50, 40),
    'up': Vector2(0, -10),
    'down': Vector2(0, 50)
}

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10
}

FRUIT_POS = {
    'Small': [(18, 17), (30, 37), (12, 50), (30, 45), (20, 30), (30, 10)],
    'Large': [(30, 24), (60, 65), (50, 50), (16, 40), (45, 50), (42, 70)]
}

FRUIT_NAMES = ['apple', 'orange', 'peach', 'pear']

GROW_SPEED = {
    'wheat': 1,
    'tomato': .7,
    'carrot': .7
}

SALE_PRICES = {
    'wood': 4,
    'apple': 2,
    'wheat': 10,
    'tomato': 20,
    'orange': 2,
    'peach': 2,
    'pear': 2
}
PURCHASE_PRICES = {
    'wheat': 4,
    'tomato': 5,
    'carrot': 5
}

SEED_DESCRIPTIONS = {
    'corn': "The first ancient farmers to\n"
            "cultivate corn were the native\n"
            "people of the North American \n"
            "continent, in an area that would\n"
            "become present-day Mexico, about\n"
            "10,000 years ago. \n"
            "It would soon become a crop\n"
            "popular across North America\n"
            "and, after Cristopher Columbus\n"
            "expeditions, corn became a staple\n"
            " food in Europe as well.\n"
            "\n"
            "Originally, the new crop discovered\n"
            "in the New World became known to\n"
            "European explorers as maize, based\n"
            "on the word ‘mahiz’ which indigenous\n"
            "people used to refer to the big\n"
            "green stalks they were cultivating.\n"
            "In Europe, the crop was referred to\n"
            "as the Indian corn, until eventually\n"
            "it became shortened to just corn.\n"
            "These days, both corn and maize are\n"
            "used in different parts of the globe.",

    'tomato': "Today’s tomatoes began as wild\n"
              "plants in the Andes, growing in\n"
              "parts of Bolivia, Chile, Colombia,\n"
              " Ecuador and Peru. The small\n"
              "fruits of the plant look very\n"
              "little like today’s cultivated\n"
              "tomatoes. Centuries of planting,\n"
              "growing and saving tomato seeds\n"
              "resulted in the fruit we recognize\n"
              "today, spreading through the\n"
              "Americas, then to Europe and\n"
              "eventually around the globe"
              "\n"
              "Tomatoes are members of the\n"
              "nightshade family, a plant family\n"
              "with known toxic compounds. Due\n"
              "to their history and association\n"
              "with more deadly member of the\n"
              "nightshade family tomatoes were\n"
              "slow to gain acceptance as a food\n"
              "crop. While tomatoes themselves\n"
              "are fine to eat, the leaves and\n"
              "stems of the plant are considered\n"
              "toxic.",

    'carrot': "Carrots are one of the healthiest\n"
              "vegetables provided to us by\n"
              "nature. They are a type of root\n"
              "vegetable common to temperate\n"
              "zones, but are domesticated\n"
              "throughout the world. They are\n"
              "packed with several essential\n"
              "minerals and vitamins. Some of\n"
              "these include vitamin A, several\n"
              "B vitamins, vitamin K, calcium,\n"
              "and potassium.\n"
              "\n"
              "Habitat:\n"
              "Carrots generally grow in temperate\n"
              "zones because of cooler temperature\n"
              "conditions. They are not compatible\n"
              "with warmer climatic conditions.\n"
              "They prefer loamy, well-drained\n"
              "soil that is rich in nutrients and\n"
              "organic material. Carrots also grow\n"
              "optimally when they are exposed to\n"
              "full sunlight.",

    'wheat': "\n"
             "Adaptation:\n"
             "\n"
             "Wheat originated in Asia. Although\n"
             "it is mostly used as a grain crop,\n"
             "it can be used as an annual forage\n"
             "crop. Wheat has good winter\n"
             "hardiness and can burn up with\n"
             "excess heat. It can tolerate a\n"
             "wide range of soils, but does not\n"
             "tolerate flooding at all.\n"
             "\n"
             "\n"
             "Growth Habitat:\n"
             "\n"
             "Wheat is an annual grass that\n"
             "usually is planted at the end of\n"
             "the summer. It overwinters and\n"
             "then starts growing and maturing\n"
             "towards the end of spring and\n"
             "beginning of the summer."
}
