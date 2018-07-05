from .EmbThread import EmbThread


def get_thread_set():
    return [
        EmbThreadJef(0, 0, 0, "Unknown", "0"),
        EmbThreadJef(0, 0, 0, "Black", "1"),
        EmbThreadJef(255, 255, 255, "White", "2"),
        EmbThreadJef(255, 255, 23, "Sunflower", "3"),
        EmbThreadJef(250, 160, 96, "Hazel", "4"),
        EmbThreadJef(92, 118, 73, "Olive Green", "5"),  # was green dust
        EmbThreadJef(64, 192, 48, "Green", "6"),
        EmbThreadJef(101, 194, 200, "Sky", "7"),
        EmbThreadJef(172, 128, 190, "Purple", "8"),
        EmbThreadJef(245, 188, 203, "Pink", "9"),
        EmbThreadJef(255, 0, 0, "Red", "10"),
        EmbThreadJef(192, 128, 0, "Brown", "11"),
        EmbThreadJef(0, 0, 240, "Blue", "12"),
        EmbThreadJef(228, 195, 93, "Gold", "13"),
        EmbThreadJef(165, 42, 42, "Dark Brown", "14"),
        EmbThreadJef(213, 176, 212, "Pale Violet", "15"),
        EmbThreadJef(252, 242, 148, "Pale Yellow", "16"),
        EmbThreadJef(240, 208, 192, "Pale Pink", "17"),
        EmbThreadJef(255, 192, 0, "Peach", "18"),
        EmbThreadJef(201, 164, 128, "Beige", "19"),
        EmbThreadJef(155, 61, 75, "Wine Red", "20"),
        EmbThreadJef(160, 184, 204, "Pale Sky", "21"),
        EmbThreadJef(127, 194, 28, "Yellow Green", "22"),
        EmbThreadJef(185, 185, 185, "Silver Grey", "23"),
        EmbThreadJef(160, 160, 160, "Grey", "24"),
        EmbThreadJef(152, 214, 189, "Pale Aqua", "25"),
        EmbThreadJef(184, 240, 240, "Baby Blue", "26"),
        EmbThreadJef(54, 139, 160, "Powder Blue", "27"),
        EmbThreadJef(79, 131, 171, "Bright Blue", "28"),
        EmbThreadJef(56, 106, 145, "Slate Blue", "29"),
        EmbThreadJef(0, 32, 107, "Nave Blue", "30"),
        EmbThreadJef(229, 197, 202, "Salmon Pink", "31"),
        EmbThreadJef(249, 103, 107, "Coral", "32"),
        EmbThreadJef(227, 49, 31, "Burnt Orange", "33"),
        EmbThreadJef(226, 161, 136, "Cinnamon", "34"),
        EmbThreadJef(181, 148, 116, "Umber", "35"),
        EmbThreadJef(228, 207, 153, "Blonde", "36"),
        EmbThreadJef(225, 203, 0, "Sunflower", "37"),
        EmbThreadJef(225, 173, 212, "Orchid Pink", "38"),
        EmbThreadJef(195, 0, 126, "Peony Purple", "39"),
        EmbThreadJef(128, 0, 75, "Burgundy", "40"),
        EmbThreadJef(160, 96, 176, "Royal Purple", "41"),
        EmbThreadJef(192, 64, 32, "Cardinal Red", "42"),
        EmbThreadJef(202, 224, 192, "Opal Green", "43"),
        EmbThreadJef(137, 152, 86, "Moss Green", "44"),
        EmbThreadJef(0, 170, 0, "Meadow Green", "45"),
        EmbThreadJef(33, 138, 33, "Dark Green", "46"),
        EmbThreadJef(93, 174, 148, "Aquamarine", "47"),
        EmbThreadJef(76, 191, 143, "Emerald Green", "48"),
        EmbThreadJef(0, 119, 114, "Peacock Green", "49"),
        EmbThreadJef(112, 112, 112, "Dark Grey", "50"),
        EmbThreadJef(242, 255, 255, "Ivory White", "51"),
        EmbThreadJef(177, 88, 24, "Hazel", "52"),
        EmbThreadJef(203, 138, 7, "Toast", "53"),
        EmbThreadJef(247, 146, 123, "Salmon", "54"),
        EmbThreadJef(152, 105, 45, "Cocoa Brown", "55"),
        EmbThreadJef(162, 113, 72, "Sienna", "56"),
        EmbThreadJef(123, 85, 74, "Sepia", "57"),
        EmbThreadJef(79, 57, 70, "Dark Sepia", "58"),
        EmbThreadJef(82, 58, 151, "Violet Blue", "59"),
        EmbThreadJef(0, 0, 160, "Blue Ink", "60"),
        EmbThreadJef(0, 150, 222, "Solar Blue", "61"),
        EmbThreadJef(178, 221, 83, "Green Dust", "62"),
        EmbThreadJef(250, 143, 187, "Crimson", "63"),
        EmbThreadJef(222, 100, 158, "Floral Pink", "64"),
        EmbThreadJef(181, 80, 102, "Wine", "65"),
        EmbThreadJef(94, 87, 71, "Olive Drab", "66"),
        EmbThreadJef(76, 136, 31, "Meadow", "67"),
        EmbThreadJef(228, 220, 121, "Canary Yellow", "68"),
        EmbThreadJef(203, 138, 26, "Toast", "69"),
        EmbThreadJef(198, 170, 66, "Beige", "70"),
        EmbThreadJef(236, 176, 44, "Honey Dew", "71"),
        EmbThreadJef(248, 128, 64, "Tangerine", "72"),
        EmbThreadJef(255, 229, 5, "Ocean Blue", "73"),
        EmbThreadJef(250, 122, 122, "Sepia", "74"),
        EmbThreadJef(107, 224, 0, "Royal Purple", "75"),
        EmbThreadJef(56, 108, 174, "Yellow Ocher", "76"),
        EmbThreadJef(208, 186, 176, "Beige Grey", "77"),
        EmbThreadJef(227, 190, 129, "Bamboo", "78")
    ]


class EmbThreadJef(EmbThread):
    def __init__(self, red, green, blue, description, catalog_number):
        EmbThread.__init__(self)
        self.set_color(red, green, blue)
        self.description = description
        self.catalog_number = catalog_number
        self.brand = "Jef"
        self.chart = "Jef"
