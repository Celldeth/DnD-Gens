import random





races = [
    "aarakocra", "aasimar", "bugbear", "centaur", "changeling", "dragonborn", "dwarf", "elf", "firbolg", "genasi", "gnome", "goblin", "goliath", "half_elf", "halfling", "half_orc", "hobgoblin", "human", "khenra", "kobold", "leonin", "lizardfolk", "triton", "minotaur", "orc", "ratfolk", "satyr", "tabaxi", "tiefling", "tortle", "yuan_ti"
]

aasimar_subraces = [
    "protector", "scourge", "fallen"
]
changeling_subraces = [
    "annis hag", "green hag", "sea hag", "night hag", "bheur hag"
]
dragonborn_subraces = [
    "black", "blue", "green", "red", "white", "brass", "bronze", "copper", "gold", "silver"
]
dwarf_subraces = [
    "hill", "mountain", "underdark"
]
elf_subraces = [
    "dark", "fey", "high", "sea", "shadow", "wood", "desert", "blood"
]
genasi_subraces = [
    "air", "earth", "fire", "water"
]
gnome_subraces = [
    "forest", "rock", "deep"
]
halfling_subraces = [
    "lightfoot", "stout", "ghostwise"
]
human_subraces = [
    'calishite', 'chondathan', 'damaran', 'illuskan', 'mulan', 'rashemi', 'shou', 'tethyrian', 'turami'
]
ratfolk_subraces = [
    "burrow", "sewer", "wild"
]
tiefling_subraces = [
    "Asmodeus", "Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel", "devil tongued", "hellfire", "winged"
]

sexes = [
    "male", "female", "boy", "girl", "androgynous"
]

aarakocra_face =  [
    'curved gray-black beak'
]
aarakocra_eyes = [
    'black'
]
aarakocra_feathers = [
    'green','red','orange','black','pink','yellow','brown','gray'
]

aasimar_eyes = [
    'pupiless white','pupiless gray'
]
aasimar_hair = [
    'gold','silver'
]
aasimar_skin = [
    'emerald','blue','tan','deep brown','pale'
]



dwarf_hair = [
    'black','gray','brown','red'
]
dwarf_skin = [
    'deep brown','copper','light brown','deep tan'
]


sunelf_hair = [
    'black','copper','golden blond'
]
sunelf_eye = [
    'gold','silver','black'
]
sunelf_skin = [
    'bronze'
]

moonelf_hair = [
    'silver-white','black','blue','blond','brown','red'
]
moonelf_eye = [
    'blue, flecked with gold','green, flecked with gold'
]
moonelf_skin = [
    'white tinged with blue','copper','golden blond'
]

woodelf_hair = [
    'black','copper','blond','brown'
]
woodelf_eye = [
    'green', 'brown','hazel'
]
woodelf_skin = [
    'copper with trace of green'
]

darkelf_hair = [
    'white','pale yellow'
]
darkelf_eye = [
    'pale silver','pale pink','red','pale blue'
]
darkelf_skin = [
    'obsidian'
]

simple_hairstyles = [
    'long hair in simple braids','long hair in a ponytail','long hair in a bun','long hair'
]

major_trait = [
    'distinctive jewelry','piercings','flamboyant or outlandish clothes','formal, clean clothes','ragged, dirty cloths','pronounced scar','missing teeth','missing fingers','unusual eye color','tattoos','birthmark','unusual skin color','bald','braided beard or hair','unusual hair color','distinctive nose','distinctive posture','exceptionally beatuiful','exceptionally ugly'
]


sex = random.choices(sexes, cum_weights=[22,44,66,88,100])[0]



def raceGen():
    race = random.choices(races, cum_weights=[3,4,7,10,11,16,22,28,30,32,36,39,42,46,50,53,56,68,70,72,74,77,80,82,85,88,891,94,96,99,100])[0]
# RACE WEIGHTS - aarakocra-3, aasimar-1, bugbear-3, "centaur-3", "changeling-1", "dragonborn-5", "dwarf-6", "elf-6", "firbolg-2", "genasi-2", "gnome-4", "goblin-3", 
# "goliath-3", "half-elf-4", "halfling-4", "half-orc-3", "hobgoblin-3", "human-12", "khenra-2", "kobold-2", "leonin-2", lizardfolk-3 "triton-3", "minotaur-2", 
# "orc-3", "ratfolk-3", "satyr-3", "tabaxi-3", "tiefling-2", "tortle-3", "yuan-ti-1"
    if(race == 'aasimar'):
        subrace = random.choices(aasimar_subraces)[0]
        return race, subrace
    elif(race == 'changeling'):
        subrace = random.choices(changeling_subraces)[0]
        return race, subrace
    elif(race == 'dragonborn'):
        subrace = random.choices(dragonborn_subraces)[0]
        return race, subrace
    elif(race == 'dwarf'):
        subrace = random.choices(dwarf_subraces)[0]
        return race, subrace
    elif(race == 'elf'):
        subrace = random.choices(elf_subraces)[0]
        return race, subrace
    elif(race == 'genasi'):
        subrace = random.choices(genasi_subraces)[0]
        return race, subrace
    elif(race == 'gnome'):
        subrace = random.choices(gnome_subraces)[0]
        return race, subrace
    elif(race == 'halfling'):
        subrace = random.choices(halfling_subraces)[0]
        return race, subrace
    elif(race == 'ratfolk'):
        subrace = random.choices(ratfolk_subraces)[0]
        return race, subrace
    elif(race == 'tiefling'):
        subrace = random.choices(tiefling_subraces)[0]
        return race, subrace
    else:
        subrace = ""
        return race, subrace



# Determine appearance based on race and occupation
def appearanceGen(race, subrace):
    if race == 'aarakocra':
        eyes = random.choice(aarakocra_eyes)
        face = random.choice(aarakocra_face)
        hue1 = random.choice(aarakocra_feathers)
        hue2 = random.choice(aarakocra_feathers)
        while hue1 == hue2:
            hue2 = random.choice(aarakocra_feathers)
        final_hue = hue1 + hue2
        return eyes, face, final_hue
    if race == 'aasimar':
        eyes = random.choice(aasimar_eyes)
    else:
        return 'no appearance'



def heightGen(race, subrace):
    if race == 'bugbear' or race == 'centaur':
        base_height_inches = 72
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 12)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'dragonborn' or race == 'leonin':
        base_height_inches = 66
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'dwarf':
        if subrace == 'hill':
            base_height_inches = 44
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == 'mountain':
            base_height_inches = 48
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
    if race == 'human' or race == 'aasimar' or race == 'hobgoblin' or race == 'yuan-ti' or race == 'changeling' or race == 'khenra':
        base_height_inches = 56
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'elf':
        if subrace == 'high' or subrace == 'wood':
            base_height_inches = 54
            dice1 = random.randint(1, 10)
            dice2 = random.randint(1, 10)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == 'dark' or subrace == 'desert':
            base_height_inches = 53
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == 'eladrin' or subrace == 'blood':
            base_height_inches = 54
            dice1 = random.randint(1, 12)
            dice2 = random.randint(1, 12)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == 'sea' or subrace == 'shadow':
            base_height_inches = 54
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
    if race == 'firbolg':
        base_height_inches = 74
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 12)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'gnome':
        base_height_inches = 35
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'goblin':
        base_height_inches = 41
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'goliath' or race == 'minotaur':
        base_height_inches = 74
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'half-elf' or race == 'tiefling' or race == 'tortle':
        base_height_inches = 57
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'half-orc':
        base_height_inches = 58
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'halfling':
        base_height_inches = 31
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'kobold':
        base_height_inches = 25
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'lizardfolk':
        base_height_inches = 57
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'orc':
        base_height_inches = 60
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'tabaxi' or race == 'aarakocra':
        base_height_inches = 58
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'triton' or race == 'satyr':
        base_height_inches = 44
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == 'genasi':
        if subrace == 'air':
            base_height_inches = 58
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier            
        if subrace == 'earth':
            base_height_inches = 58
            dice1 = random.randint(1, 12)
            dice2 = random.randint(1, 12)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier   
        if subrace == 'fire':
            base_height_inches = 58
            dice1 = random.randint(1, 10)
            dice2 = random.randint(1, 10)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier               
        if subrace == 'water':
            base_height_inches = 58
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
    if race == 'ratfolk':
        if subrace == 'burrow':
            base_height_inches = 48
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
        if subrace == 'sewer':
            base_height_inches = 48
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
        if subrace == 'wild':
            base_height_inches = 48
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
    weight = weightGen(race, subrace, height_modifier)
    return final_height_inches, weight



def weightGen(race, subrace, height_modifier):
    if race == 'aasimar' or race == 'half-elf' or race == 'hobgoblin' or race == 'human' or race == 'tiefling' or race == 'yuan-ti' or race == 'khenra':
        base_weight = 110
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'bugbear' or race == 'goliath' or race == 'centaur' or race == 'minotaur' or race == 'tortle':
        base_weight = 200
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'dragonborn' or race == 'firbolg' or race == 'orc' or race == 'leonin':
        base_weight = 175
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'dwarf':
        if subrace == 'hill':
            base_weight = 115
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
        else: 
            base_weight = 130
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
    if race == 'elf' or race == 'changeling':
        if subrace == 'wood':
            base_weight = 100
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
        if subrace == 'dark':
            base_weight = 75
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
        else: 
            base_weight = 90
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
    if race == 'gnome' or race == 'goblin' or race == 'halfling' or race == 'kobold':
        base_weight = 35
        weight_modifier = 1
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'half-orc':
        base_weight = 140
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'lizardfolk':
        base_weight = 120
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'tabaxi' or race == 'triton' or race == 'ratfolk' or race == 'satyr':
        base_weight = 90
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'aarakocra':
        base_weight = 70
        weight_modifier = 1
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == 'genasi':
        if subrace == 'air':
            base_weight = 70
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
        if subrace == 'earth':
            base_weight = 140
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
        if subrace == 'fire':
            base_weight = 110
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight             
        if subrace == 'water':
            base_weight = 90
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
    

if __name__ == "__main__":
    race, subrace = raceGen()
    appearance = appearanceGen(race,subrace)
    print(sex, race, subrace, appearance)