import random


surname_types = [
    "desertfolk", "farmfolk", "foodmakers", "frozenlands", "garmentmakers", "islanders", "masons", "mountainfolk", "merchants", "mages", "religious", "riverfolk", "seafolk", "smiths", "soldiers", "stablehands", "swampfolk", "townfolk", "woodsfolk", "servants"
]

jobs = {
    'noble': [
        'a','b','c'
    ],
    'desertfolk': [
        'apothecary', 'cartographer', 'concubine', 'furrier', 'guide', 'herbalist', 'hunter', 'teacher', 'tracker',
    ],
    'farmfolk': [
        'farmer', 'gardener', 'milkmaid', 'miller', 'shepherd',
    ],
    'foodmakers': [
        'baker', 'brewer','butcher', 'cook', 'barmaid', 'winemaker',
    ],
    'frozenlands': [
        'apothecary', 'concubine', 'furrier', 'prospector', 'guide', 'herbalist', 'hunter', 'teacher', 'tracker',
    ],
    'garmentmakers': [
        'cobbler', 'dyer', 'furrier', 'leatherworker', 'spinster', 'tailor', 'weaver',
    ],
    'islanders': [
        'apothecary', 'cartographer', 'concubine', 'fishmonger', 'fisherman', 'guide', 'herbalist', 'hunter', 'teacher',
    ],
    'masons': [
        'carpenter', 'candlemaker', 'potter', 'thatcher', 'bricklayer'
    ],
    'mountainfolk': [
        'apothecary', 'concubine', 'furrier', 'prospector', 'guide', 'herbalist', 'hunter', 'miner', 'panhandler', 'stonecutter', 
    ],
    'merchants': [
        'banker', 'gemcutter', 'merchant', 'peddler', 'shopkeeper',
    ],
    'mages': [
        'astrologer', 'healer', 'scholar', 'scribe', 'shaman', 'teacher',
    ],
    'religious': [
        'acolyte', 'healer', 'midwife', 'monk', 'priest', 'shaman', 'herbalist',
    ],
    'riverfolk': [
        'apothecary', 'concubine', 'ferryman', 'fisherman', 'fishmonger', 'guide',
    ],
    'seafolk': [
        'cartographer', 'ferryman', 'fisherman', 'fishmonger', 'dockworker', 'sailor', 'shipwright',
    ],
    'smiths': [
        'armorer','blacksmith', 'goldsmith', 'silversmith', 'weaponsmith', 'fletcher', 'glassblower'
    ],
    'soldiers': [
        'bodyguard', 'bountyhunter', 'guard', 'hunter', 'knight', 'mercenary', 'soldier', 'squire',
    ],
    'stablehands': [
        'falconer', 'groom', 'page', 'shepherd', 'stablehand', 'wagondriver',
    ],
    'swampfolk': [
        'apothecary', 'concubine', 'fishmonger', 'fisherman', 'guide', 'herbalist', 'hunter',
    ],
    'townfolk': [
        'acrobat','actor','architect','alchemist', 'candlemaker', 'chamberlain', 'clerk', 'dancer', 'engineer', 'taxcollector', 'gardener', 'herald', 'bard', 'landlord', 'dockworker', 'minstrel', 'mortician', 'painter', 'sculptor', 'teacher', 'toymaker', 'fletcher', 'diplomat', 'gravedigger', 'inn_keeper'
    ],
    'woodsfolk': [
        'apothecary', 'concubine', 'furrier', 'guide', 'herbalist', 'hunter', 'teacher', 'tracker', 'woodsman' , 'fletcher'
    ],
    'servants': [
        'maid', 'butler', 'concubine', 'page', 'prostitute', 'servant', 'slave', 'slavetrader', 'thief', 'rat_catcher'
    ]
}



#weight jobs
def jobGen(sex):
    job_type = random.choice(surname_types)
    if sex == 'boy' or sex == 'girl':
        job = 'apprentice ' + random.choice(jobs[job_type])
        return job, job_type
    else:
        job = random.choice(jobs[job_type])
        return job, job_type



if __name__ == "__main__":
    sex = 'male'
    print(jobGen(sex))


