import random
import dicerollGen
import appearanceGen
import encounterGen
import itemGen

alias = [
    'Bonecrusher',
]

directions = [
    'north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest'
]

resource_sites = [
    'logging camp','field mowing site','explosive mining site',''
]



guilds = {
    'Adventurers Guild': {
        'titles': {
            'Monster Hunter': [
                'client needs a monster killed, you can find it in the terrain to the direction', 'Client needs a monster captured, you can find it in the terrain to the direction'
            ],
            'Archaeologist': [
                'client needs someone to track down an ancient loot', 'client needs someone to find a lost location', 'client needs someone to search for a forgotten location'
            ],
            'Treasure Hunter': [
                'client is selling a treasure map, source is trustworthy. Decipher the clues and the treasure is yours. Map selling for gold'
            ],
            'Surveyor': [
                'client needs an adventurer to go into and map the unexplored terrain to the direction'
            ],
            'Zoologist': [
                'client needs a researcher to observe, research and write about monster traits - strengths, weakness, condition immunities, etc. reward for each trait discovered.'
            ],
        },
        'rewards': [
            'gold', 'trinket', 'potion', 'art', 'gem', 'magic item'
        ],
        'organizations': [
            'Champion of the Talon', 'Le Devour De Loups'
        ]
    },
    'Assassins Guild': {
        'titles': {
        
        },
        'rewards': {

        },
        'organizations': [

        ]
    },
    'Druidic Circle': {
        'titles': {
            'Enforcer': [
                'The Druidic Circle needs a site run by humanoid to end its operation, they are destroying the sacred terrain dedicated to deity. They have ignored all communications for them to cease, be prepared for force.'
            ],
            'Exterminator': [
                'Reports show an invasive beast have infested the nearby terrain. The Druidic circle needs able bodies to exterminate these beasts from the area.'
            ],
            'First Responder': [
                'We need first responders to mitigate the disaster that is destroying the nearby terrain. According to reports, a rogue elemental is the cause of the destruction.'
            ],
            'Defender': [
                'ecoterrorist is harmful_act of a nearby village. This will not only affect the village but is hurting the environment, we need defenders to neutralize this threat.'
            ],
            'Planar Protector': [
                'The Druidic Circle has been notified of a portal to plane in the terrain close-by, that is corrupting the area. We need planar experts to close the rift and remove the creature that came through.'
            ],
            'Rescuer': [
                'creatures have been captured by poachers for illicit trade. We need rescurers to track down the poachers hideout, that were seen in the nearby terrain. Then neutralize the threat, and free the captured creatures.'
            ]
        },
        'rewards': [
            'gold', 'trinket', 'potion', 'art', 'gem', 'magic item'
        ]
    },
    'Forbidden Council': {},
    'Grey Ring': {},
    'Mage Consortium': {},
    'Mercenary Company': {
        'titles': {
            'Bounty Hunter': [
                f'Wanted Dead or Alive - {alias}, {appearanceGen.raceGen()} to the {random.choice(directions)}! Warning: very armed and dangerous. Has many henchmen.'
            ]
        },
    },
    'Merchants Alliance': {},
    'Righteous Conclave': {},
    'Thieves Guild': {},
    'Virtues Fellowship': {},
}



town_jobs = {
    'exterminator','bounty hunter','missing persons','chicken wrangler','bodyguards','test subjects','fetcher','performer'
}


Town_Jobs = [
    'Exterminator needed: Ive got a mess of pest s in my basement. Bring me 10 pest corpses in return for payment.', 'Exterminator needed: Theres a bunch of noise coming from the attic. Like chains or moaning or something. Its probably those damn raccoons again. I would have my husband look into it, but the lazy oaf up and died on me. Payment dependent on work done.', f'House is overrun with pest s. Exterminate {dicerollGen.rolldice(4, 10)} pest and {dicerollGen.rolldice(2, 4)} big_pest. Reward of 450gp.'
    'Missing: a large turtle named Hubert who has escaped from the Casters School of Polymorphing. Please return if found!'

]


complications = '(The advert has a typo and should point to a house further down the way.)'


quest_type = {
    'kill quest': [

    ],
    'puzzle quest': [

    ],
    'delivery quest': [

    ],
    'gather quest': [

    ],
    'escort quest': [

    ],
    'hybrid quest':[

    ]
}



"""
def generate_job_post():
    category = random.choice(list(guild_lists.keys()))
    job_data = guild_lists[category]

    title = random.choice(job_data['titles'])
    responsibility = random.choice(job_data['responsibilities'])
    qualification = random.choice(job_data['qualifications'])
    benefit = random.choice(job_data['benefits'])

    job_post = f"Job Title: {title}\nResponsibilities: {responsibility}\nQualifications: {qualification}\nBenefits: {benefit}\n"

    return job_post

# Generate a random job post
job_post = generate_job_post()
print(job_post)
"""



#make 4-8 jobs for guild quest-board
def guildboardGen(guild):
    for job in range(random.randint(4,8)):
        rarity = random.choices(itemGen.rarities, cum_weights=[75,87,95,99,100])[0]
        reward = ''
        if guild == guilds['Adventurers Guild']:
            in_tags = []
            in_tags.append(rarity)
            title = random.choice(list(guild['titles'].keys()))
            if title == 'Monster Hunter':
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar' or terrain == 'urban':
                    terrain = random.choice(encounterGen.terrains)
                in_tags.append(terrain)
                direction = random.choice(directions)
                monster = encounterGen.monsterGen(*in_tags)
                task = random.choice(guild['titles'][title]).replace('monster', monster).replace('terrain', terrain).replace('direction', direction)
            if title == 'Archaeologist':
                treasure = rewardGen('trinket', rarity)
                location = random.choice(encounterGen.dungeons)
                direction = random.choice(directions)
                task = random.choice(guild['titles'][title]).replace('direction', direction).replace('loot', treasure).replace('location', location)
            if title == 'Treasure Hunter':
                location = random.choice(encounterGen.dungeons)
                gold = str(dicerollGen.rolldice(10,10)) + 'g'
                task = random.choice(guild['titles'][title]).replace('location', location).replace('dungeon', location).replace('gold', gold)
            if title == 'Surveyor':
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar' or terrain == 'urban':
                    terrain = random.choice(encounterGen.terrains)
                direction = random.choice(directions)
                task = random.choice(guild['titles'][title]).replace('terrain', terrain).replace('direction', direction)
            if title == 'Zoologist':
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar' or terrain == 'urban':
                    terrain = random.choice(encounterGen.terrains)
                in_tags.append(terrain)
                monster = encounterGen.monsterGen(*in_tags)
                task = random.choice(guild['titles'][title]).replace('monster', monster).replace('terrain', terrain)
            reward = rewardGen(random.choice(guild['rewards']), rarity)
            if title == 'Treasure Hunter':
                print(f'{title} Needed! \n{task}\n')
            else:
                print(f'{title} Needed! \n{task} \nReward: {reward}\n')
        if guild == guilds['Driuidic Circle']:
            in_tags = []
            in_tags.append(rarity)
            title = random.choice(list(guild['titles'].keys()))
            if title == 'Enforcer':
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar' or terrain == 'urban':
                    terrain = random.choice(encounterGen.terrains)
                in_tags.append('humanoid')
                humanoid = encounterGen.creatureGen(*in_tags)
                site = '' #'make a resource-gathering-site Generator'
                deity = 'nature deity'
                task = random.choice(guild['titles'][title]).replace('site', site).replace('humanoid', humanoid).replace('terrain', terrain).replace('deity', deity)
            if title == 'Exterminator':
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar':
                    terrain = random.choice(encounterGen.terrains)
                if terrain == 'urban':
                    terrain = 'village'
                monster = encounterGen.monsterGen(*in_tags)
                task = random.choice(guild['titles'][title]).replace('beast', monster).replace('terrain', terrain)
            if title == 'First Responder':
                disaster = '' #make disasterGen
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar':
                    terrain = random.choice(encounterGen.terrains)
                monster = 'elemental' #make elemental gen
                task = random.choice(guild['titles'][title]).replace('disaster', disaster).replace('terrain', terrain).replace('elemental', monster)
            if title == 'Defender':
                harmful_act = '' # harmful act against natural resources
                villian = '' # villianGen - ecoterrorist
                direction = random.choice(directions)
                task = random.choice(guild['titles'][title]).replace('harmful_act', harmful_act).replace('ecoterrorist', villian)
            if title == 'Planar Protector':
                plane = '' # portal to plane generator
                terrain = random.choice(encounterGen.terrains)
                while terrain == 'planar' or terrain == 'urban':
                    terrain = random.choice(encounterGen.terrains)
                in_tags.append('planar')
                monster = encounterGen.monsterGen(*in_tags)
                task = random.choice(guild['titles'][title]).replace('plane', plane).replace('terrain', terrain).replace('creature', monster)
                
            #replace all task .replace with one task replace
            task = random.choice(guild['titles'][title]).replace('monster', monster).replace('terrain', terrain).replace('direction', direction)
            reward = rewardGen(random.choice(guild['rewards']), rarity)
            print(f'{title} Needed! \n{task} \nReward: {reward}\n')
        if guild == guilds['Forbidden Council']:
            'placeholder'
        if guild == guilds['Grey Ring']:
            'placeholder'
        if guild == guilds['Mage Consortium']:
            'placeholder'
        if guild == guilds['Mercenary Company']:
            'placeholder'
        if guild == guilds['Merchants Alliance']:
            'placeholder'
        if guild == guilds['Righteous Conclave']:
            'placeholder'
        if guild == guilds['Thieves Guild']:
            'placeholder'
        if guild == guilds['Virtues Fellowship']:
            'placeholder'


def rewardGen(reward, rarity):
    in_tags = [] 
    in_tags.append(rarity)

    value = \
        '20g' if rarity == 'common' else \
        '60g' if rarity == 'uncommon' else \
        '200g' if rarity == 'rare' else \
        '2000g' if rarity == 'very rare' else \
        '20000g' if rarity == 'legendary' else None

    if reward == 'art':
        reward = dicerollGen.rolldice(1,4)
        reward = str(reward) + f' {random.choice(itemGen.art[rarity])} worth {value} each'
    if reward == 'trinket':
        reward = dicerollGen.rolldice(1,4)
        reward = str(reward) + f" {random.choice(itemGen.trinkets['normal'])} worth {value} each"
    if reward == 'gold':
        reward = \
            dicerollGen.rolldice(10,8) if rarity == 'common' else \
            dicerollGen.rolldice(30,8) if rarity == 'uncommon' else \
            dicerollGen.rolldice(100,8) if rarity == 'rare' else \
            dicerollGen.rolldice(1000,8) if rarity == 'very rare' else \
            dicerollGen.rolldice(10000,8) if rarity == 'legendary' else None
        reward = str(reward) + 'g'
    if reward == 'potion':
        in_tags.append(reward)
        reward = dicerollGen.rolldice(1,4)
        reward = str(reward) + ' ' + itemGen.treasureGen(*in_tags)
    if reward == 'gem':
        reward = dicerollGen.rolldice(1,4)
        reward = str(reward) + ' ' + itemGen.gemGen(rarity) + f', a {rarity} gem'
    if reward == 'magic item':
        reward = itemGen.treasureGen(rarity) + f', a {rarity} magic item'
    return reward

# ------------------impliment recipies --------------
def secretjobGen():
    'placeholder'

guild = guilds['Adventurers Guild']

#guildboardGen(guilds['Adventurers Guild'])

guildboardGen(guild)



"""
First Roll:
The action of the quest is to:
1. Liberate/Recover/Intercept
2. Destroy/Kill
3. Guard/Defend
4. Transport/Escort/Journey To
5. Create/Build/Summon
6. Gather Information About

Second Roll:
The object of the quest is:
1. Item
2. NPC
3. Message/Data
4. Secret or Dangerous Location
5. Magical Equipment/Technology
6. Monster
"""