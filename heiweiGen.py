import random


def heightGen(race, subrace):
    if race == ['bugbear'] or race == ['centaur']:
        base_height_inches = 72
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 12)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['dragonborn'] or race == ['leonin']:
        base_height_inches = 66
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['dwarf']:
        if subrace == ['hill']:
            base_height_inches = 44
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == ['mountain']:
            base_height_inches = 48
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
    if race == ['human'] or race == ['aasimar'] or race == ['hobgoblin'] or race == ['yuan-ti'] or race == ['changeling'] or race == ['khenra']:
        base_height_inches = 56
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['elf']:
        if subrace == ['high'] or subrace == ['wood']:
            base_height_inches = 54
            dice1 = random.randint(1, 10)
            dice2 = random.randint(1, 10)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == ['dark'] or subrace == ['desert']:
            base_height_inches = 53
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == ['eladrin'] or subrace == ['blood']:
            base_height_inches = 54
            dice1 = random.randint(1, 12)
            dice2 = random.randint(1, 12)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
        if subrace == ['sea'] or subrace == ['shadow']:
            base_height_inches = 54
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier
    if race == ['firbolg']:
        base_height_inches = 74
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 12)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['gnome']:
        base_height_inches = 35
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['goblin']:
        base_height_inches = 41
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['goliath'] or race == ['minotaur']:
        base_height_inches = 74
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['half-elf'] or race == ['tiefling'] or race == ['tortle']:
        base_height_inches = 57
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['half-orc']:
        base_height_inches = 58
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['halfling']:
        base_height_inches = 31
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['kobold']:
        base_height_inches = 25
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['lizardfolk']:
        base_height_inches = 57
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['orc']:
        base_height_inches = 60
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['tabaxi'] or race == ['aarakocra']:
        base_height_inches = 58
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['triton'] or race == ['satyr']:
        base_height_inches = 44
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)
        height_modifier = dice1 + dice2
        final_height_inches = base_height_inches + height_modifier
    if race == ['genasi']:
        if subrace == ['air']:
            base_height_inches = 58
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier            
        if subrace == ['earth']:
            base_height_inches = 58
            dice1 = random.randint(1, 12)
            dice2 = random.randint(1, 12)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier   
        if subrace == ['fire']:
            base_height_inches = 58
            dice1 = random.randint(1, 10)
            dice2 = random.randint(1, 10)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier               
        if subrace == ['water']:
            base_height_inches = 58
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
    if race == ['ratfolk']:
        if subrace == ['burrow']:
            base_height_inches = 48
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
        if subrace == ['sewer']:
            base_height_inches = 48
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
        if subrace == ['wild']:
            base_height_inches = 48
            dice1 = random.randint(1, 8)
            dice2 = random.randint(1, 8)
            height_modifier = dice1 + dice2
            final_height_inches = base_height_inches + height_modifier  
    weight = weightGen(race, subrace, height_modifier)
    return final_height_inches, weight


def weightGen(race, subrace, height_modifier):
    if race == ['aasimar'] or race == ['half-elf'] or race == ['hobgoblin'] or race == ['human'] or race == ['tiefling'] or race == ['yuan-ti'] or race == ['khenra']:
        base_weight = 110
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['bugbear'] or race == ['goliath'] or race == ['centaur'] or race == ['minotaur'] or race == ['tortle']:
        base_weight = 200
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['dragonborn'] or race == ['firbolg'] or race == ['orc'] or race == ['leonin']:
        base_weight = 175
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['dwarf']:
        if subrace == ['hill']:
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
    if race == ['elf'] or race == ['changeling']:
        if subrace == ['wood']:
            base_weight = 100
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight
        if subrace == ['dark']:
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
    if race == ['gnome'] or race == ['goblin'] or race == ['halfling'] or race == ['kobold']:
        base_weight = 35
        weight_modifier = 1
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['half-orc']:
        base_weight = 140
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['lizardfolk']:
        base_weight = 120
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['tabaxi'] or race == ['triton'] or race == ['ratfolk'] or race == ['satyr']:
        base_weight = 90
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        weight_modifier = dice1 + dice2
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['aarakocra']:
        base_weight = 70
        weight_modifier = 1
        final_weight = height_modifier * weight_modifier + base_weight
        return final_weight
    if race == ['genasi']:
        if subrace == ['air']:
            base_weight = 70
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
        if subrace == ['earth']:
            base_weight = 140
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
        if subrace == ['fire']:
            base_weight = 110
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight             
        if subrace == ['water']:
            base_weight = 90
            dice1 = random.randint(1, 4)
            dice2 = random.randint(1, 4)
            weight_modifier = dice1 + dice2
            final_weight = height_modifier * weight_modifier + base_weight
            return final_weight  
    