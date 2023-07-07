import random



def rolldice(dice, sides):
    result = 0
    for i in range(dice):
        roll = random.randint(1, sides)
        result += roll
    return result
