import random
import appearanceGen
import nameGen
import socialGen
import personalityGen

race = ''
subrace = ''
sex = ''
job = ''

race = input('race:')
if race == 'aasimar':
    subrace = input('subrace:')
    if subrace not in appearanceGen.aasimar_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.aasimar_subraces:
        subrace = input('subrace:')
if race == 'changeling':
    subrace = input('subrace:')
    if subrace not in appearanceGen.changeling_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.changeling_subraces:
        subrace = input('subrace:')
if race == 'dragonborn':
    subrace = input('subrace:')
    if subrace not in appearanceGen.dragonborn_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.dragonborn_subraces:
        subrace = input('subrace:')
if race == 'dwarf':
    subrace = input('subrace:')
    if subrace not in appearanceGen.dwarf_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.dwarf_subraces:
        subrace = input('subrace:')
if race == 'elf':
    subrace = input('subrace:')
    if subrace not in appearanceGen.elf_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.elf_subraces:
        subrace = input('subrace:')
if race == 'genasi':
    subrace = input('subrace:')
    if subrace not in appearanceGen.genasi_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.genasi_subraces:
        subrace = input('subrace:')
if race == 'gnome':
    subrace = input('subrace:')
    if subrace not in appearanceGen.gnome_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.gnome_subraces:
        subrace = input('subrace:')
if race == 'halfling':
    subrace = input('subrace:')
    if subrace not in appearanceGen.halfling_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.halfling_subraces:
        subrace = input('subrace:')
if race == 'ratfolk':
    subrace = input('subrace:')
    if subrace not in appearanceGen.ratfolk_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.ratfolk_subraces:
        subrace = input('subrace:')
if race == 'tiefling':
    subrace = input('subrace:')
    if subrace not in appearanceGen.tiefling_subraces:
        print('Not a valid input')
    while subrace not in appearanceGen.tiefling_subraces:
        subrace = input('subrace:')
sex = input('sex:')


if race == '':
    race, subrace = appearanceGen.raceGen()

if sex == '':
    sex = appearanceGen.sex

appearance = appearanceGen.appearanceGen(race,subrace)
height, weight = appearanceGen.heightGen(race,subrace)
feet = round(height/12)
inches = height%12

if job == '':
    job, job_type = socialGen.jobGen(sex)

name = nameGen.nameGen(race,subrace,sex)
surname = nameGen.surnameGen(race,subrace,job,job_type)

if __name__ == "__main__":
    if sex == 'male' or sex == 'boy':
        print(f"A {sex} {subrace} {race} named {name} {surname}. He is {feet},{inches} tall and weigh about {weight}lbs. Has {appearance}")
    if sex == 'female' or sex == 'girl':
        print(f"A {sex} {subrace} {race} named {name} {surname}. She is {feet},{inches} tall and weigh about {weight}lbs. Has {appearance}")
    else:
        print(f"A {sex} {subrace} {race} named {name} {surname}. They are {feet},{inches} tall and weigh about {weight}lbs. Has {appearance}")