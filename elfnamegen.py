
import random
import testSwear




nm1 = ["Ad", "Ae", "Bal", "Bei", "Car", "Cra", "Dae", "Dor", "El", "Ela", "Er", "Far", "Fen", "Gen", "Glyn", "Hei", "Her", "Ian", "Ili", "Kea", "Kel", "Leo", "Lu", "Mira", "Mor", "Nae", "Nor", "Olo", "Oma", "Pa", "Per", "Pet", "Qi", "Qin", "Ralo", "Ro", "Sar", "Syl", "The", "Tra", "Ume", "Uri", "Va", "Vir", "Waes", "Wran", "Yel", "Yin", "Zin", "Zum"
]
nm2 = ["balar", "beros", "can", "ceran", "dan", "dithas", "faren", "fir", "geiros", "golor", "hice", "horn", "jeon", "jor", "kas", "kian", "lamin", "lar", "len", "maer", "maris", "menor", "myar", "nan", "neiros", "nelis", "norin", "peiros", "petor", "qen", "quinal", "ran", "ren", "ric", "ris", "ro", "salor", "sandoral", "toris", "tumal", "valur", "ven", "warin", "wraek", "xalim", "xidor", "yarus", "ydark", "zeiros", "zumin"
]
nm3 = ["Ad", "Ara", "Bi", "Bry", "Cai", "Chae", "Da", "Dae", "Eil", "En", "Fa", "Fae", "Gil", "Gre", "Hele", "Hola", "Iar", "Ina", "Jo", "Key", "Kris", "Lia", "Lora", "Mag", "Mia", "Neri", "Ola", "Ori", "Phi", "Pres", "Qi", "Qui", "Rava", "Rey", "Sha", "Syl", "Tor", "Tris", "Ula", "Uri", "Val", "Ven", "Wyn", "Wysa", "Xil", "Xyr", "Yes", "Ylla", "Zin", "Zyl"
]
nm4 = ["banise", "bella", "caryn", "cyne", "di", "dove", "fiel", "fina", "gella", "gwyn", "hana", "harice", "jyre", "kalyn", "krana", "lana", "lee", "leth", "lynn", "moira", "mys", "na", "nala", "phine", "phyra", "qirelle", "ra", "ralei", "rel", "rie", "rieth", "rona", "rora", "roris", "satra", "stina", "sys", "thana", "thyra", "tris", "varis", "vyre", "wenys", "wynn", "xina", "xisys", "ynore", "yra", "zana", "zorwyn"
]
nm5 = ["", "", "", "b", "c", "d", "dr", "f", "fl", "g", "h", "k", "l", "m", "n", "r", "qu", "s", "sh", "t", "th", "v", "w", "x", "y"
]
nm6 = ["ae", "ie", "ia", "ei", "ey", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u"
]
nm7 = ["dr", "l", "l", "ld", "ldr", "ll", "lph", "lt", "lth", "m", "n", "ndr", "nn", "nt", "ph", "r", "r", "rd", "rn", "s", "sh", "st", "str", "th", "thr", "v"
]
nm8 = ["a", "e", "i", "o"
]
nm9 = ["dr", "lk", "ndr", "nthr", "sc", "st", "str", "thr", "c", "h", "l", "m", "n", "nn", "ph", "r", "rr", "s", "ss", "v", "x"
]
nm10 = ["ii", "ie", "aea", "ia", "ua", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o"
]
nm11 = ["", "", "", "", "", "l", "n", "nn", "nt", "r", "s", "sh", "th"
]
nm12 = ["alder", "amber", "ash", "aspen", "autumn", "azure", "beech", "birch", "blue", "bold", "bronze", "cedar", "crimson", "dawn", "dew", "diamond", "dusk", "eager", "elder", "elm", "ember", "even", "fall", "far", "feather", "fir", "flower", "fog", "forest", "gem", "gold", "green", "hazel", "light", "lunar", "mist", "moon", "moss", "night", "oak", "oaken", "ocean", "poplar", "rain", "rapid", "raven", "sage", "shadow", "silent", "silver", "spark", "spirit", "spring", "star", "still", "stone", "summer", "sun", "swift", "wild", "willow", "wind", "winter", "wood"
]
nm13 = ["beam", "bell", "birth", "blossom", "breath", "breeze", "brook", "cloud", "crown", "dew", "dream", "dreamer", "fall", "fate", "flight", "flow", "flower", "fond", "gaze", "gazer", "gift", "gleam", "grove", "guard", "heart", "heel", "hold", "kind", "light", "mane", "might", "mind", "moon", "path", "petal", "pride", "rest", "river", "seeker", "sense", "shadow", "shard", "shine", "singer", "smile", "song", "spark", "spell", "spirit", "star", "vale", "walker", "watcher", "whisper", "wish"
]
nm14 = ["br", "ph", "th", "tr", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "z", "", "", "", ""
]
nm15 = ["ae", "ay", "oe", "ue", "ai", "ia", "y", "a", "e", "i", "o", "a", "e", "i", "o"
]
nm16 = ["k", "l", "ll", "m", "n", "nn", "r"
]
nm17 = ["a", "i"
]
nm18 = ["ll", "ng", "nn", "th", "rn", "l", "m", "n", "r", "s", "", ""
]



def nameGen(sex):
    surname = ""
    if sex == ['boy'] or sex == ['girl']:
        child_name = nameChild()
        while child_name == "":
            nameChild()
        else:
            return child_name
    else:
        if random.choice([True, False]):
            sur1 = random.choice(nm12)
            sur2 = random.choice(nm13)
            while sur1 == sur2:
                sur2 = random.choice(nm13)
            full_name = sur1 + sur2
            surname = testSwear.testSwear(full_name)
        if surname == "":
            surname = nameSur()
            while surname == "":
                nameSur()
        if sex == ['female']:
            first_name = nameFem()
            while first_name == "":
                nameFem()
        elif sex == ['male']:
            first_name = nameMas()
            while first_name == "":
                nameMas()
        else:
            sex = random.choice(['male','female'])
            nameGen(sex)
        full_name = first_name + " " + surname
        return full_name



def nameFem():
    first_name = random.choice(nm3)
    last_name = random.choice(nm4)
    full_name = first_name + last_name
    name = testSwear.testSwear(full_name)
    return name

def nameMas():
    first_name = random.choice(nm1)
    last_name = random.choice(nm2)
    full_name = first_name + last_name
    name = testSwear.testSwear(full_name)
    return name

def nameSur():
    name_type = random.randint(0, 7)
    first_name = random.choice(nm5)
    last_name = random.choice(nm6)
    first_name3 = random.choice(nm7)
    first_name4 = random.choice(nm10)
    first_name5 = random.choice(nm11)
    if (name_type < 3):
        while first_name5 == first_name3 and first_name3 == first_name:
            first_name3 = random.choice(nm7)
        full_name = first_name + last_name + first_name3 + first_name4 + first_name5
    else:
        first_name6 = random.choice(nm8)
        first_name7 = random.choice(nm9)
        while (first_name5 == first_name6 and first_name6 == first_name3):
            first_name7 = random.choice(nm9)
        if (name_type < 6):
            full_name = first_name + last_name + first_name3 + first_name6 + first_name7 + first_name4 + first_name5
        else:
            first_name8 = random.choice(nm8)
            first_name9 = random.choice(nm9)
            while (first_name5 == first_name6 and first_name6 == first_name9):
                first_name7 = random.choice(nm9)
            if (name_type == 6):
                full_name = first_name + last_name + first_name3 + first_name6 + first_name7 + first_name8 + first_name9 + first_name4 + first_name5
            else:
                full_name = first_name + last_name + first_name7 + first_name8 + first_name3 + first_name6 + first_name9 + first_name4 + first_name5
    name = testSwear.testSwear(full_name)
    return name

def nameChild():
    name_type = int(random.random() * 2)
    first_name = random.choice(nm14)
    last_name = random.choice(nm15)
    first_name3 = random.choice(nm18)
    if (name_type == 0):
        if (first_name == ""):
            while (first_name3 == ""):
                first_name3 = random.choice(nm18)
        if (first_name3 == ""):
            last_name = random.choice(nm15)
        full_name = first_name + last_name + first_name3
    else:
        first_name4 = random.choice(nm16)
        first_name5 = random.choice(nm17)
        full_name = first_name + last_name + first_name4 + first_name5 + first_name3
    name = testSwear.testSwear(full_name)
    return name
