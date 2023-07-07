import random
import elfnamegen
import humannamegen
import heiweiGen
import personaltraits




#NPC Plot Hooks, Occupations, appearances, Personality Traits, Bonds, Voice types, Names, Ideals, special skills, mannerisms

################## Defining Strings ##################




environments = [
    'any', ' aquatic', ' arctic', ' badlands', ' coastal', ' desert', ' farmland', ' forest', ' grassland', ' hill', ' marshes', ' mountain', ' hell', ' plains', ' ethereal', ' ruins', ' swamp', ' underdark', ' underground', ' urban'
]





# NAME
# Names - pool determined by race, region - name_region, occupation - surname, 

if race == ['human']:
    name = humannamegen.nameGen(sex, subrace)
elif race == ['elf']:
    name = elfnamegen.nameGen(sex)
else:
    name = "noname"

# ENVIRONMENT GET
def environmentGET():
    environment = ""
    if environment == "":
        environment = input("what is the area-type?(any, aquatic, arctic, badlands, coastal, desert, farmland, forest, grassland, hill, marshes, mountain, hell, plains, ethereal, ruins, swamp, underdark, underground, urban)")
    if environment not in environments:
        environment = ""
        print('incorrect input')
        environmentGET()
    else:
        return environment




# --------------------APPEARANCE-------------------



height, weight = heiweiGen.heightGen(race,subrace)


# ---------------PERSONALITY--------------

bond, trait, ideal = personaltraits.personalityGen()

vocal_speed, vocal_pitch, vocal_texture, vocal_pattern, mannerism = personaltraits.voice_typeGen()



# PRINTING


if sex == ['male'] or sex == ['boy']:
    pronoun = 'he'
elif sex == ['female'] or sex == ['girl']:
    pronoun = 'she'
else:
    pronoun = ['they']


print('A', *sex, *subrace, *race, 'named', name, 'who works as a', *occupation)
print('Speaks in a',vocal_speed,'paced',vocal_pitch,'pitched voice, that sounds',vocal_texture, 'and', vocal_pattern, '.', pronoun,'tends to', mannerism)

print("Final height:", height // 12, "feet", height % 12, "inches")
print('Final weight:', weight, 'lbs')

print("Bond:",bond,"\nTrait:",trait,"\nIdeal:",ideal)


#Print choices in a readable format


if race == ['aarakocra']:
    print('A', *sex, *subrace, *race, 'named', name, 'who works as a', *occupation)
    print('Speaks in a',vocal_speed,'paced',vocal_pitch,'pitched voice, that sounds',vocal_texture, 'and', vocal_pattern, '.', pronoun,'tends to', mannerism)
    print("Final height:", height // 12, "feet", height % 12, "inches")
    print('Final weight:', weight, 'lbs')
    print("Bond:",bond,"\nTrait:",trait,"\nIdeal:",ideal)
