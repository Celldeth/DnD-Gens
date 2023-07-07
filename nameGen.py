import random
import testSwear
import socialGen
import copy



# Name Dictionary
name_data = {
    'aarakocra':{
        'name_sounds':[
            'click','trill','whistle','hoot','laugh','screech','caw','whinny','coo',''
        ],
        'names1':[
            'ak', 'clour', 'di', 'du', 'ecc', 'er', 'gre', 'hur', 'kli', 'kou', 'qha', 'quc', 'rhe', 'ri', 'sa', 'uc', 'ui', 'ur'
        ],
        'names2':[
            'el','ker','re','rar','er','i','ki','ca','ci'
        ],
        'names3':[
            'erk','ak','ca','iek','ef','is','e','r','f','a','ad','r','rk','el','le','k'
        ],
        'surname':[]
    },
    'aasimar':{
        'names1':[
            'an', 'az', 'cach', 'cath', 'el', 'gam', 'ham', 'ia', 'kar', 'kas', 'ma', 'on', 'perp', 'rad', 'sal', 'soph', 'zar', 'zu'
        ],
        'names2':[
            'uan','em','er','et','az','ur','ath','al'
        ],
        'names3':[
            'iel','iah','za','ael','ma','oel','el','al','ion'
        ],
    },
    'bugbear':{
        'names1':[
            'nan','gov','tat','zar','bal','thi','rath','vir','vamk','rut','tor','nud','namk','nor','bod','rar','gin','tik','dor','gan','dur','tin',
        ],
        'names2':[
            'r','k','h','n'
        ],
    },
    'centaur':{
        'male':{
            'names1':[
                'Aug','Bo','Cho','Dri','Eno','Ko','Or','Ske','To','Ya',
            ],
            'names2':[
                'h','r','z','v','l','m','n'
            ],
            'names3':[
                'us','mod','di','ios','o','im','val','or','is','og'
            ],
        },
        'female':{
            'names1':[
                'bi','dun','gal','ho','kot','mel','mi','pin','ra','sa','tat',
            ],
            'names2':[
                'is','no','ya','is'
            ],
            'names3':[
                'do','ja','nya','tia','li','oe','ra','ya','na'
            ],
        },
        'surname':{
            'names1':[
                "Aspen", "Autumn", "Birch", "Bloom", "Boulder", "Brook", "Brown", "Bright", "Brush", "Burrow", "Cedar", "Crater", "Creek", "Drift", "Dust", "Earthen", "Elm", "Fall", "Flood", "Fog", "Forest", "Grass", "Green", "Grove", "Hail", "Hazel", "Hill", "Hollow", "Ice", "Iron", "Laurel", "Maple", "Moon", "Moss", "Mountain", "Oaken", "Peak", "Pine", "Plain", "Rain", "Ridge", "River", "Rock", "Snow", "Spring", "Star", "Stone", "Storm", "Summer", "Sun", "Thorn", "Timber", "Valley", "Vine", "Willow", "Winter", "Wood", "Yew"
            ],
            'names2':[
                "bark", "basker", "bearer", "binder", "blade", "blesser", "blossom", "blossoms", "borne", "braid", "braider", "braids", "breaker", "bringer", "bruiser", "caller", "carver", "catcher", "chanter", "charger", "chaser", "cleanser", "conqueror", "crest", "dancer", "darter", "defender", "divider", "dreamer", "drinker", "eyes", "fader", "fighter", "force", "forcer", "former", "gatherer", "glow", "groom", "groomer", "guard", "heart", "herald", "hold", "hoof", "laugh", "leaf", "leaper", "leaves", "limp", "love", "mane", "mangle", "march", "mask", "mind", "muse", "pass", "pelt", "petals", "prowl", "prowler", "push", "reign", "rest", "reveler", "ride", "rise", "roamer", "roar", "run", "runner", "rush", "rusher", "scorn", "screamer", "seeker", "shadow", "shield", "shifter", "shine", "sign", "sleep", "slumber", "smile", "smirk", "spark", "spell", "stare", "strength", "tail", "temper", "thread", "trampler", "tree", "twister", "voice", "volley", "wander", "wanderer", "watch", "watcher", "whisper", "whisperer", "wish"
            ],
        },
    },
    'changeling':{
        'names1':[
            "", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"
        ],
        'names2':[
            "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai", "oo", "ou"
        ],
        'names3':[
            "c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"
        ],
    },
    'dragonborn':{
        'male':{
            'names1':[
                'ar','ba','bal','bh','do','ghe','he','kri','me','na','pa','pan','rho','sha','she','tar','tor'
            ],
            'names2':[
                'jha','lasa','ara','na','e','ska','dra','he','dar','dje','tri','ga','ma','din','hu','in'
            ],
            'names3':[
                'n','r','sh','ar','d','v'
            ],
        },
        'female':{
            'names1':[
                'ak','bi','da','fa','ha','jhe','ka','ko','mi','na','per','rai','so','su','tha','ua','ra'
            ],
            'names2':[
                'rid','ran','vil','rin','shan','an','rin','dj'
            ],
            'names3':[
                'ra','ri','ar','eh','n','ar','va','la','ra','a','it'
            ],
        },
        'surname':{
            'names1':[
                'cleth','da','del','drac','fen','kep','ker','kim','lin','my','nem','nor','oph','pre','shes','tur','ver','yar'
            ],
            'names2':[
                'tin','ard','mir','hed','ken','eshk','rhy','ba','xa','ka','tha','il','end','ka','bra','mol','tu','send','as','mon','ix','in','sh','ta','la','ji','xi','jan','di','ten','del','nur','this','ath','ur','gi','jer'
            ],
            'names3':[
                'lor','rian','ev','ion','don','ik','lon','ul','alor','tan','is','ius','ir','lin','iath','oth','esh','it'
            ],
        },
    },
    'dwarf':{
        'male':{
            'names1':[
                'ad','albe','ba','bar','brot','bru','da','dar','del','eb','ein','far','f','gar','har','kil','mor','or','os','ran','ru','tak','thor','tor','trau','tra','ulf','ve','von'
            ],
            'names2':[
                'rik','rich','ern','end','tor','enor','in','rak','g','erk','kil','grim','lint','dain','bek','drak','gran','sik','kar','linn','adin','dek','bon','vok','gar','it','dal'
            ],
        },
        'female':{
            'names1':[
                'am','ar','aud','bar','dag','di','eld','falk','fin','gun','gur','hel','h','ka','kri','il','lift','mard','ris','san','torb','torg','vis'
            ],
            'names2':[
                'ber','tin','hild','dryn','nal','esa','eth','run','ellen','loda','dis','ja','lin','thra','stryd','de','rasa','red','wynn','nl','era','tra'
            ],
        },
        'surname':{
            'names1':[
                'axe','battle','boulder','brawn','bronze','copper','deep','ember','fire','flint','frost','gem','gold','granite','iron','rock','silver','steel','stone','strong','swift','thunder'
            ],
            'names2':[
                'anvil','axe','beard','belly','breaker','bringer','brow','delver','finger','fist','foot','forge','grasp','grip','guard','hammer','heart','helm','hide','mantle','pick','shield','smith','spine','stone'
            ],
            'names3':[
                'bald', 'dan','gor','holder','lod','lut','rumna','strak','tor','un'
            ],
            'names4':[
                'derk','kil','unn','hek','err','gehr','heim','eln','gart'
            ],
        },
    },
    'elf':{
        'male':{
            'names1':[
                'ad','ae','ar','au','bei','ber','car','en','er','ga','ha','he','hi','im','iv','lau','min','pae','pe','qua','ri','ro','sov','tha','the','var'
            ],
            'names2':[
                'a','an','ri','al','lin','dar','i','me','el','ci','li','ar','el','mi'
            ],
            'names3':[
                'ran','lar','mil','nis','st','ro','an','ric','is','dan','van','ai','mo','ral','ios','tis','as','ren','on','don','len','or','vol','ol'
            ]
        },
        'female':{
            'names1':[
                'ad','al','and','ant','ana','beth','bi','cae','dru','en','fel','iel','jel','key','le','mer','me','ia','nai','que','quil','sa','sha','si','thei','the','va','xan'
            ],
            'names2':[
                'tha','stri','ras','in','ryn','sil','os','en','an','ie','va','len','la','ri','nai','la','dan','lan','aph'
            ],
            'names3':[
                'rie','ea','na','te','ua','na','rel','lynn','ia','ial','eth','leth','le','ra','the','el','va','qui','tra'
            ]
        },
        'blood':{
            'male':{
                'names1':[
                    'vo','ser','xal','va','ze','mal','thae','el','ar','dra','se','xa','ma', 'za', 'aer','lo','ne','ner','vra','pa',"dar'"
                ],
                'names2':[
                    'ren','ran','len','phy','ach','dri','li','an','ra','r','ph','lan','re'
                ],
                'names3':[
                    'thas','nis','ath','ar','us','ai','on','ven','en','is','as','eth','ir',
                ]
            },
            'female':{
                'names1':[
                    'az','ly','syl','ev','is','ny','ves','ve','am','ser','se','an','li','lir'
                ],
                'names2':[
                    'ar','ras','ra','va','an','ol','mer','me','pe','a','aph','eth'
                ],
                'names3':[
                    'iah','tra','ra','ya','de','ia','a','ine','eth','stra'
                ]
            },
            'surname':{
                'names1': [
                    'ash','blood','death','ember','raven','shadow','soul','void', 'crimson', 'ever', 'deep', 'great','high','last','far','end','rose','time','old','third','mind','spirit','mythic', 'grim','fatal','dire', 'pale','passing','new', 'ancient','gray','elder','long', 'first'
                ],
                'names2': [
                    'bane','fable','fire','heart','shade','shadow','thorn','veil','whisper', 'song','dawn','flame','blade', 'line','kin','rose','memory','mind','thought','call','eye' ,'tale','saga','birth', 'gift'
                ],
            },
        },
        'dark':{
            'male':{
                'names1':[
                    'yaz','er','url','ant','ur','an','rel','re','du','min','qu','nim',"k'",'se','zak','sel','mer','me','num','nu','ny','ryl','ry','jha','te','ha',
                ],
                'names2':[
                    'd','th','ax','od','ra','or','en','ru','y','on','ag','ni','ny','v','g','dr','ant','amk','b',"tch'"
                ],
                'names3':[
                    'aer','tel','le','ax','us','an','uel','el','ul','ve','il','l','en','ar','in','or','ryn',
                ],
            },
            'female':{

            },
            'surname':{
                'names1': [
                    ''
                ],
                'names2': [
                ],
            },
        },
        'desert':{
            'male':{

            },
            'female':{

            },
            'surname':{
                'names1': [
                ],
                'names2': [
                ],
            },
        },
        'fey':{
            'male':{

            },
            'female':{

            },
            'surname':{
                'names1': [
                ],
                'names2': [
                ],
            },
        },
        'high':{
            'male':{
                'names1':[
                    'ael','aer','al','an','ar','bel','cal','cor','eil','el','faer','gal','il','ith','lor','maer','nel','or','quel','raen','sel','tal','val','xan','zan',
                ],
                'names2':[
                    'a','an','ri','al','lin','dar','i','me','el','ci','li','ar','el','mi'
                ],
                'names3':[
                    'an','ar','el','en','il','in','ir','is','ius','on','or','us','yr',
                ]
            },
            'female':{
                'names1':[
                    'el','ser','is','el','cal','li','aer','al','syl','mi','se','ca',
                    'ad','al','and','ant','ana','beth','bi','cae','dru','en','fel','iel','jel','key','le','mer','me','ia','nai','que','quil','sa','sha','si','thei','the','va','xan',
                    'tha','stri','ras','in','ryn','sil','os','en','an','ie','va','len','la','ri','nai','la','dan','lan','aph'
                ],
                'names2':[
                    'ad','an','aph','ar','ath','dan','en','eth','ie','in','la','lan','len','nai','ol','os','ras','rel','ri','ryn','sil','stri','tha','va',
                ],
                'names3':[
                    'ia','ina','a','wen','wyn','ea','ine','ath'
                ]
            },
            'child':{
                'names1':[
                    'a','b','d','e','fa','in','la','mel','na','ph','r','ra','s','syl','th','v',
                ],
                'names2':[
                    'ra','ryn','el','en','nil','el','la','ill','eris','ann','inn','ai','lin','ia','all'
                ],
            },
            'surname':{
                'names1': [
                    'diamond','gem','gold','moon','night','silver','spell','star','sun','wind','winter','autumn','summer','spring','pearl','glit','bright','grand','great','noble','fine','radiant','pure','charm','elegant','worthy'
                ],
                'names2': [
                    'blade','bloom','blossom','born','borne','breeze','brook','caller','caster','dew','dust','fire','flower','heel','leaf','petal','pond','shade','shadow','strider','thorn','weaver','whisper','wind',
                ],
            },
        },
        'sea':{
            'male':{

            },
            'female':{

            },
            'surname':{
                'names1': [
                ],
                'names2': [
                ],
            },
        },
        'shadow':{
            'male':{

            },
            'female':{

            },
            'surname':{
                'names1': [
                ],
                'names2': [
                ],
            },
        },
        'wood':{
            'male':{

            },
            'female':{

            },
            'surname':{
                'names1': [
                    'ashen','briar','cedar','dawn','falcon','fern','green','grove','leaf','moss','oak','pine','river','shadow','storm','swift','thistle','wild','willow'
                ],
                'names2': [
                    'ashen','briar','cedar','dawn','falcon','fern','green','grove','leaf','moss','oak','pine','river','shadow','storm','swift','thistle','wild','willow'
                ],
            },
        },
        'surname':{
            'names1': [
                'ashen','briar','cedar','dawn','falcon','fern','green','grove','leaf','moss','oak','pine','river','shadow','storm','swift','thistle','wild','willow'
            ],
            'names2': [
                'ashen','briar','cedar','dawn','falcon','fern','green','grove','leaf','moss','oak','pine','river','shadow','storm','swift','thistle','wild','willow'
            ],
    },
    },
    'human':{
        'calishite':{
            'male':{
                'names1':[
                    'aay', 'ab', 'ad', 'af', 'ah', 'al', 'an', 'aq', 'ar', 'as', 'az', 'bar', 'bi', 'dan', 'fa', 'ha' 'has', 'hu', 'ib', 'ja', 'jal', 'ka' 'khe', 'ma', 'man', 'mar', 'muh', 'meh', 'na', 'od', 'oth', 'om', 'qa', 'ra', 'sa', 'sha', 'sal', 'su', 'sud', 'ta', 'tar', 'za','zash'
                ],
                'names2':[
                    'a', 'dul', 'e', 'ei', 'h', 'is', 'iz', 'kar', 'sa', 'ish', 'us'
                ],
                'names3':[
                    'al', 'ar', 'eid', 'eir', 'el', 'em', 'en', 'fan', 'had', 'han', 'ib', 'if', 'is', 'ish', 'lam', 'lan', 'len', 'mad', 'man', 'med', 'men', 'ran', 'sir', 'zan'
                ],
            },
            'female':{
                'names1':[
                    'ab', 'af', 'ai', 'al', 'am', 'an', 'aq', 'ar', 'as', 'at', 'ba', 'bu', 'bush', 'ce', 'esh', 'fa', 'far', 'ha', 'haf', 'han', 'in', 'iq', 'ja', 'jas', 'kha', 'kin', 'kir', 'la', 'ma', 'mad', 'mah', 'me', 'na', 'rab', 're', 'ruk', 'sa', 'sad', 'sam', 'san', 'seh', 'sei', 'sha', 'shu', 'sid', 'sob', 'son', 'sum', 'yash', 'zash'
                ],
                'names2':[ 
                    'a','id','il','po','ei','ti','ra','ri','di','ma', 'se'
                ],
                'names3':[ 
                    'ah', 'am', 'ba', 'da', 'een', 'fa', 'ha', 'ia', 'il', 'ir', 'ish', 'la', 'ma', 'mal', 'na', 'oor', 'ra', 'sa', 'sha', 'um', 'za'
                ],
            },
            'surname':{
                'names1':[
                    'a', 'ab', 'aba', 'ah', 'am', 'as', 'ay', 'az', 'ba', 'bak', 'bash', 'bil', 'bur', 'da', 'dar', 'dum', 'eb', 'fa', 'fad', 'far', 'fas', 'ha', 'hab', 'had', 'haf', 'hak', 'ham', 'har', 'has', 'hash', 'ib', 'iq', 'ir', 'is', 'ja', 'jab', 'jal', 'jam', 'jas', 'ka', 'kha', 'lagh', 'ma', 'mo', 'mos', 'mu', 'na', 'no', 'os', 'pash', 'qa', 'qu', 'ra', 're', 'sa', 'sha', 'ta', 'wa', 'ya'
                ],
                'names2':[
                    'dal','gh','da','wo', 's','ta', 'iz'
                ],
                'names3':[
                    'a', 'ad', 'al', 'an', 'ar', 'at', 'di', 'eid', 'ein', 'em', 'ib', 'id', 'im', 'in', 'in', 'ish', 'iz', 'lah', 'li', 'lid', 'mad', 'na', 'na', 'ri', 'si', 'uq'
                ],
            }
        },
        'cadonian':{
            'male':{
                'names1':[
                    'dar', 'do', 'ev', 'gor', 'gr', 'hel', 'mal', 'mo', 'ran', 'st','sor','mag','cil','cos','cas','raf','iv','li','le','di','stel','vig','bast','lar','cle','bru','las','ni'
                ],
                'names2':[
                    'en','st','er','fer','mi','ko'
                ],
                'names3':[
                    'vin','dur','ag','im','m','ark','rn','dal','edd','en','nus','ian','mo','per','ty','o','e','tri','an','on','go','ian','s','ent','no','zlo','lo','lai'
                ],
            },
            'female':{
                'names1':[
                    'Arv', 'Es', 'Jhes', 'Ker', 'Lur', 'Mi', 'Ro', 'Shan', 'Tes','sas','in','am','ga','ya'
                ],
                'names2':[
                    'ee','ve','sa','se','el'
                ],
                'names3':[
                    'ne','le','il','ri','wan','dri','kia','es','ie','ia','ra'
                ],
            },
            'surname':{
                'names1':[
                    'amble','bold','brave','bright','calm','clear','fair','fine','free','great','kind','pure','quick','smart','strong','sweet','swift','tall','true','warm','wise',
                ],
                'names2':[
                    'abbey','acorn','anchor','arrow','axe','banner','barn','bow','bridge','castle','chain','church','cottage','crown','dagger','drum','farm','forge','gate','halbert','harp','heart','horn','house','hydra','keep','lance','laurel','mace','mail','man','mill','moat','phoenix','pike','ram','scimitar','scythe','shield','sword','tavern','tower','wall','well','wharf','wood',
                ],
            },
        },
        'damaran':{
            'male':{
                'names1':[
                    'aleks', 'bra', 'ber', 'bro', 'bo', 'che', 
                ],
                'names2':[
                    'ri','gu','to', 'do', 'om', 'ir','ib' ,'ni',
                ],
                'names3':[
                    'slav','mir','dar','il'
                ],
            },
            'female':{
                'names1':[
                    'Al', 'Ka', 'Kat', 'Ma', 'Nat', 'Ol', 'Ta', 'Zo','ni','ve','mi','an','nad','lil','ta','sa','ki','ang'
                ],
                'names2':[
                    'eth','er','a','er','tian','sta','li','ia','el'
                ],
                'names3':[
                    'ra','na','ma','li','in','ya','lia','ka','sha','ia','ica'
                ],
            },
            'surname':{
                'names1':[
                    'Ber', 'Chern', 'Dot', 'Kul', 'Mar', 'Nem', 'Shem', 'Star','iv','smirn','sid','nov','vol'
                ],
                'names2':[
                    'en','et','an','or','ik','oz'
                ],
                'names3':[
                    'ov','sk','in','ag','ev'
                ],
            },
        },
        'ekesic':{
            'male':{

            },
            'female':{

            },
        },
        'skan':{
            'male':{
                'names1':[
                    'And', 'Bla', 'Bran', 'Fra', 'Ge', 'Land', 'Lu', 'Malc', 'St', 'Tam', 'Ur'
                ],
                'names2':[
                    'rik','rich','ern','end','tor','enor','in','rak','g','erk','kil','grim','lint','dain','bek','drak','gran','sik','kar','linn','adin','dek','bon','vok','gar','it','dal'
                ],
                'names3':[
                    'er','th','an','er','or'
                ],
            },
            'female':{
                'names1':[
                    'Ama', 'Beth', 'Ce', 'Keth', 'Ma', 'Ol', 'Si', 'West', 
                ],
                'names2':[
                    'li'
                ],
                'names3':[
                    'frey','a','ra','ga'
                ],
            },
            'surname':{
                'names1':[
                    'Bright', 'Horn', 'Lack', 'Storm', 'Wind'
                ],
                'names2':[

                ],
                'names3':[
                    'wood','raven','man','wind','river','hold'
                ],
            }
        },
        'martese':{
            'male':{

            },
            'female':{

            },
        },
        'naiwedon':{
            'male':{

            },
            'female':{

            },
        },
        'pricepian':{
            'male':{

            },
            'female':{

            },
        },
        'rashemi':{
            'male':{

            },
            'female':{

            },
        },
        'shou':{
            'male':{

            },
            'female':{

            },
        },
        'turami':{
            'male':{

            },
            'female':{

            },
        },
    },
}






# - mesoamerican
# - polynesian




#Calishite- Arabic
#calishite name format = name - titles - parent name - surname - hometown :: ex: oma yr asfora el tenassar yi almravien (oma daughter of asfora of the tenassar family from almravien)
calishite_male_names1 = [
    'aay', 'ab', 'ad', 'af', 'ah', 'al', 'an', 'aq', 'ar', 'as', 'az', 'bar', 'bi', 'dan', 'fa', 'ha' 'has', 'hu', 'ib', 'ja', 'jal', 'ka' 'khe', 'ma', 'man', 'mar', 'muh', 'meh', 'na', 'od', 'oth', 'om', 'qa', 'ra', 'sa', 'sha', 'sal', 'su', 'sud', 'ta', 'tar', 'za','zash'
]
calishite_male_names2 = [
    'a', 'dul', 'e', 'ei', 'h', 'is', 'iz', 'kar', 'sa', 'ish', 'us'
]
calishite_male_names3 = [
    'al', 'ar', 'eid', 'eir', 'el', 'em', 'en', 'fan', 'had', 'han', 'ib', 'if', 'is', 'ish', 'lam', 'lan', 'len', 'mad', 'man', 'med', 'men', 'ran', 'sir', 'zan'
]
calishite_female_names1 = [
    'ab', 'af', 'ai', 'al', 'am', 'an', 'aq', 'ar', 'as', 'at', 'ba', 'bu', 'bush', 'ce', 'esh', 'fa', 'far', 'ha', 'haf', 'han', 'in', 'iq', 'ja', 'jas', 'kha', 'kin', 'kir', 'la', 'ma', 'mad', 'mah', 'me', 'na', 'rab', 're', 'ruk', 'sa', 'sad', 'sam', 'san', 'seh', 'sei', 'sha', 'shu', 'sid', 'sob', 'son', 'sum', 'yash', 'zash'
]
calishite_female_names2 = [ 
    'a','id','il','po','ei','ti','ra','ri','di','ma', 'se'
]
calishite_female_names3 = [ 
    'ah', 'am', 'ba', 'da', 'een', 'fa', 'ha', 'ia', 'il', 'ir', 'ish', 'la', 'ma', 'mal', 'na', 'oor', 'ra', 'sa', 'sha', 'um', 'za'
]
calishite_surnames1 = [
    'a', 'ab', 'aba', 'ah', 'am', 'as', 'ay', 'az', 'ba', 'bak', 'bash', 'bil', 'bur', 'da', 'dar', 'dum', 'eb', 'fa', 'fad', 'far', 'fas', 'ha', 'hab', 'had', 'haf', 'hak', 'ham', 'har', 'has', 'hash', 'ib', 'iq', 'ir', 'is', 'ja', 'jab', 'jal', 'jam', 'jas', 'ka', 'kha', 'lagh', 'ma', 'mo', 'mos', 'mu', 'na', 'no', 'os', 'pash', 'qa', 'qu', 'ra', 're', 'sa', 'sha', 'ta', 'wa', 'ya'
]
calishite_surnames2 = [
    'dal','gh','da','wo', 's','ta', 'iz'
]
calishite_surnames3 = [
    'a', 'ad', 'al', 'an', 'ar', 'at', 'di', 'eid', 'ein', 'em', 'ib', 'id', 'im', 'in', 'in', 'ish', 'iz', 'lah', 'li', 'lid', 'mad', 'na', 'na', 'ri', 'si', 'uq'
]

#Cadonian - English
cadonian_male_names1 = [
    'dar', 'do', 'ev', 'gor', 'gr', 'hel', 'mal', 'mo', 'ran', 'st','sor','mag','cil','cos','cas','raf','iv','li','le','di','stel','vig','bast','lar','cle','bru','las','ni'
]
cadonian_male_names2 = [
    'en','st','er','fer','mi','ko'
]
cadonian_male_names3 = [
    'vin','dur','ag','im','m','ark','rn','dal','edd','en','nus','ian','mo','per','ty','o','e','tri','an','on','go','ian','s','ent','no','zlo','lo','lai'
]
cadonian_female_names1 = [
    'Arv', 'Es', 'Jhes', 'Ker', 'Lur', 'Mi', 'Ro', 'Shan', 'Tes','sas','in','am','ga','ya'
]
cadonian_female_names2 = [
    'ee','ve','sa','se','el'
]
cadonian_female_names3 = [
    'ne','le','il','ri','wan','dri','kia','es','ie','ia','ra'
]
cadonian_surnames1 = [
    'amble','bold','brave','bright','calm','clear','fair','fine','free','great','kind','pure','quick','smart','strong','sweet','swift','tall','true','warm','wise',
]
cadonian_surnames2 = [
]
cadonian_surnames3 = [
    'abbey','acorn','anchor','arrow','axe','banner','barn','bow','bridge','castle','chain','church','cottage','crown','dagger','drum','farm','forge','gate','halbert','harp','heart','horn','house','hydra','keep','lance','laurel','mace','mail','man','mill','moat','phoenix','pike','ram','scimitar','scythe','shield','sword','tavern','tower','wall','well','wharf','wood',
]

#damaran - Slavic
damaran_male_names1 = [
    'aleks', 'bra', 'ber', 'bro', 'bo', 'che', 
]
damaran_male_names2 = [
    'ri','gu','to', 'do', 'om', 'ir','ib' ,'ni', ''
]
damaran_male_names3 = [
    'slav','mir','dar','il'
]
damaran_female_names1 = [
    'Al', 'Ka', 'Kat', 'Ma', 'Nat', 'Ol', 'Ta', 'Zo','ni','ve','mi','an','nad','lil','ta','sa','ki','ang'
]
damaran_female_names2 = [
    'eth','er','a','er','tian','sta','li','ia','el'
]
damaran_female_names3 = [
    'ra','na','ma','li','in','ya','lia','ka','sha','ia','ica'
]
damaran_surnames1 = [
    'Ber', 'Chern', 'Dot', 'Kul', 'Mar', 'Nem', 'Shem', 'Star','iv','smirn','sid','nov','vol'
]
damaran_surnames2 = [
    'en','et','an','or','ik','oz'
]
damaran_surnames3 = [
    'ov','sk','in','ag','ev'
]

#Ekesics - Egyptian
male_Ekesic_names = ['Aoth', 'Bareris', 'Ehput-Ki', 'Kethoth', 'Mumed', 'Ramas', 'So-Kehur', 'Thazar-De', 'Urhur']
female_Ekesic_names = ['Arizima', 'Chathi', 'Nephis', 'Nulara', 'Murithi', 'Sefris', 'Thola', 'Umara', 'Zolis']
Ekesic_surnames = ['Ankhalab', 'Anskuld', 'Fezim', 'Hahpet', 'Nathandem', 'Sepret', 'Uuthrakt']

#skan - German/Norse
skan_male_names1 = [
    'And', 'Bla', 'Bran', 'Fra', 'Ge', 'Land', 'Lu', 'Malc', 'St', 'Tam', 'Ur'
]
skan_male_names2 = [

]
skan_male_names3 = [
    'er','th','an','er','or'
]
skan_female_names1 = [
    'Ama', 'Beth', 'Ce', 'Keth', 'Ma', 'Ol', 'Si', 'West', 
]
skan_female_names2 = [
    'li'
]
skan_female_names3 = [
    'frey','a','ra','ga'
]
skan_surnames1 = [
    'Bright', 'Horn', 'Lack', 'Storm', 'Wind'
]
skan_surnames2 = [

]
skan_surnames3 = [
    'wood','raven','man','wind','river','hold'
]

#Martese - french

#Naiwedon - japan/ cletic

#pricepian - Roman/greek


#Rashemi - indian
male_rashemi_names = ['Borivik', 'Faurgar', 'Jandar', 'Kanithar', 'Madislak', 'Ralmevik', 'Shaumar', 'Vladislak']
female_rashemi_names = ['Fyevarra', 'Hulmarra', 'Immith', 'Imzel', 'Navarra', 'Shevarra', 'Tammith', 'Yuldra']
rashemi_surnames = ['Chergoba', 'Dyernina', 'Iltazyara', 'Murnyethara', 'Stayanoga', 'Ulmokina']

#Shou - chinese
male_shou_names = ['An', 'Chen', 'Chi', 'Fai', 'Jiang', 'Jun', 'Lian', 'Long', 'Meng', 'On', 'Shan', 'Shui', 'Wen']
female_shou_names = ['Bai', 'Chao', 'Jia', 'Lei', 'Mei', 'Qiao', 'Shui', 'Tai']
shou_surnames = ['Chien', 'Huang', 'Kao', 'Kung', 'Lao', 'Ling', 'Mei', 'Pin', 'Shin', 'Sum', 'Tan', 'Wan']

#Turami - spanish
male_turami_names = [
    'Anton', 'Diero', 'Marcon', 'Pieron', 'Rimardo', 'Romero', 'Salazar', 'Umbero'
]
female_turami_names = [
    'Balama', 'Dona', 'Faila', 'Jalana', 'Luisa', 'Marta', 'Quara', 'Selise', 'Vonda'
]
turami_surnames = [
    'Agosto', 'Astorio', 'Calabra', 'Domine', 'Falone', 'Marivaldi', 'Pisacar', 'Ramondo'
]

job_surnames = {
    'noble_surnames': [
        
    ],
    'desertfolk_surnames': [
        'Bright', 'Brown', 'Browne', 'Brushfire', 'Camp', 'Campman', 'Canyon', 'Cricketts', 'Crickets', 'Dunes', 'Doons', 'Doones', 'Dunne', 'Dunneman', 'Flats', 'Fox', 'Foxx', 'Gold', 'Golden', 'Grey', 'Gray', 'Gulch', 'Gully', 'Hardy', 'Hills', 'Hill', 'Hopper', 'Hunter', 'Huntsman', 'March', 'Marcher', 'Moon', 'Redmoon', 'Palmer', 'Palms', 'Peartree', 'Pearman', 'Redd', 'Red', 'Rider', 'Ryder', 'Rock', 'Rockman', 'Rock', 'Rockman', 'Rocker', 'Sands', 'Scales', 'Redscale', 'Greyscale', 'Singer', 'Small', 'Smalls', 'Star', 'Starr', 'Stone', 'Stoneman', 'Storm', 'Storms', 'Strider', 'Stryder', 'Sunn', 'Sunner', 'Tumbleweed', 'Walker', 'Water', 'Watters'
    ],
    'farmfolk_surnames': [
        'Appletree', 'Appler', 'Applin', 'Barley', 'Barleycorn', 'Barleywine', 'Barns', 'Barnes', 'Barnard', 'Beans', 'Beanman', 'Beanstalk', 'Berry', 'Berryland', 'Bloom', 'Bloomland', 'Brown', 'Brownland', 'Brownard', 'Bull', 'Bullyard', 'Cabbage', 'Kabbage', 'Cotton', 'Cottonseed', 'Croppe', 'Cropman', 'Dairyman', 'Darryman', 'Darry', 'Derry', 'Farmer', 'Farmor', 'Fields', 'Fielder', 'Fieldman', 'Flats', 'Redflats', 'Sandflats', 'Stoneflats', 'Flowers', 'Gardner', 'Gardener', 'Gardiner', 'Green', 'Greene', 'Greenland', 'Greenyard', 'Grove', 'Groveland', 'Hays', 'Hayes', 'Hayward', 'Henkeeper', 'Hennerman', 'Herd', 'Hurd', 'Herdland', 'Land', 'Lander', 'Mares', 'Mayr', 'Mair', 'Meadows', 'Milk', 'Millet', 'Millett', 'Mills', 'Miller', 'Millard', 'Neeps', 'Neepland', 'Nutt', 'Nutman', 'Oates', 'Oats', 'Overland', 'Overfield', 'Peartree', 'Pearman', 'Pease', 'Peapod', 'Peabody', 'Picket', 'Picketts', 'Pickens', 'Pickman', 'Plant', 'Planter', 'Ploughman', 'Plowman', 'Plougherman', 'Pollen', 'Pollin', 'Polly', 'Pollard', 'Rains', 'Raines', 'Rayns', 'Raynes', 'Rainard', 'Root', 'Roote', 'Rutland', 'Shepherd', 'Shepard', 'Shepyrd', 'Shearer', 'Sheerer', 'Shears', 'Sheers', 'Sower', 'Soward', 'Tate', 'Tater', 'Thresh', 'Threshett', 'Tiller', 'Tillman', 'Vines', 'Vineland', 'Wheatley', 'Wheatly', 'Wheat', 'Whittaker', 'Whitard', 'Winnows', 'Winnower', 'Wool', 'Woolard', 'Yardly', 'Yardley', 'Yards'
    ],
    'foodmakers_surnames': [
        'Ales', 'Aleman', 'Aler', 'Baker', 'Bake', 'Bakeler', 'Barr', 'Barre', 'Barman', 'Berry', 'Berryman', 'Berriman', 'Boyle', 'Boiles', 'Boyles', 'Brewer', 'Brewster', 'Broyles', 'Broiles', 'Broyler', 'Butcher', 'Butchett', 'Cook', 'Dice', 'Dougherman', 'Dougher', 'Fry', 'Frey', 'Fryman', 'Gardner', 'Gardener', 'Gardiner', 'Grills', 'Grillett', 'Innes', 'Innman', 'Inman', 'Kettle', 'Kettleblack', 'Kettleman', 'Kneadler', 'Kneadman', 'Milk', 'Miller', 'Mills', 'Miller', 'Palewine', 'Pan', 'Pannerman', 'Panning', 'Peppers', 'Pepper', 'Pickler', 'Pickleman', 'Pickles', 'Pieman', 'Piemaker', 'Potts', 'Pott', 'Potter', 'Redwine', 'Roasterman', 'Salt', 'Salter', 'Simms', 'Simmerman', 'Slaughter', 'Smoke', 'Smoker', 'Vines', 'Vintner', 'Vinaker', 'Winaker', 'Wineman'
    ],
    'frozenlands_surnames': [
        'Biggs', 'Bigg', 'Byggs', 'Camp', 'Campman', 'Coates', 'Frost', 'Furrs', 'Furrman', 'Graysky', 'Whitesky', 'Blacksky', 'Grey', 'Gray', 'Hardy', 'Hardison', 'Hardland', 'Harland', 'Hills', 'Hill', 'Hylls', 'Hunter', 'Huntsman', 'Ice', 'Iceland', 'Icewind', 'Icecutter', 'Yceland', 'Ycewind', 'Ycecutter', 'Longnight', 'Longdark', 'Moon', 'Wintermoon', 'North', 'Northman', 'Norman', 'Northland', 'Norland', 'Pix', 'Pickman', 'Pickes', 'Pyckes', 'Seales', 'Seals', 'Silver', 'Silvermoon', 'Sylver', 'Snow', 'Snowes', 'Star', 'Starr', 'Northstar', 'Stone', 'Stoneman', 'Strider', 'Stryder', 'Walker', 'White', 'Whyte', 'Winter', 'Winters', 'Wynters'
    ],
    'garmentmakers_surnames': [
        'Bobbin', 'Bolt', 'Bolte', 'Bolter', 'Button', 'Buttonworth', 'Capers', 'Coates', 'Cotton', 'Dyer', 'Dye', 'Dyeworth', 'Dyerson', 'Dyson', 'Felter', 'Felterman', 'Glover', 'Hatter', 'Hatty', 'Hattiman', 'Hatson', 'Hemmings', 'Hemings', 'Hemson', 'Hyde', 'Hides', 'Hydes', 'Leathers', 'Lethers', 'Mercer', 'Needleman', 'Needler', 'Needleworth', 'Seams', 'Seems', 'Seemworth', 'Shearer', 'Sheerer', 'Shears', 'Sheers', 'Shoemaker', 'Stitches', 'Stitchworth', 'Tailor', 'Taylor', 'Tanner', 'Tannerman', 'Thredd', 'Threddler', 'Threddman', 'Threddaker', 'Weaver', 'Weever', 'Wool', 'Woolworth', 'Yardly', 'Yardley', 'Yards'
    ],
    'islanders_surnames': [
        'Bay', 'Bayes', 'Bayer', 'Bayers', 'Beacher', 'Beach', 'Blue', 'Bowman', 'Castaway', 'Crabb', 'Crab', 'Crest', 'Days', 'Dayes', 'Dunes', 'Doons', 'Doones', 'Dunne', 'Dunneman', 'Eddy', 'Fisher', 'Fishman', 'Flowers', 'Harper', 'Hook', 'Hooke', 'Iles', 'Isles', 'Ailes', 'Mast', 'Palmer', 'Palms', 'Rafman', 'Raftman', 'Reel', 'Reelings', 'Salt', 'Seasalt', 'Sands', 'Sandman', 'Seabreeze', 'Shell', 'Shellman', 'Shellmound', 'Sheller', 'Shelley', 'Shoals', 'Singer', 'Star', 'Starr', 'Stern', 'Sterne', 'Stillwater', 'Storm', 'Storms', 'Summers', 'Sunn', 'Sunner', 'Swimmer', 'Shwimmer', 'Swymmer', 'Tidewater', 'Waters', 'Watters', 'Waterman'
    ],
    'masons_surnames': [
        'Arch', 'Archmaker', 'Baskett', 'Basket', 'Bilder', 'Builder', 'Bulder', 'Bilds', 'Blow', 'Brickman', 'Bricker', 'Brycks', 'Bricks', 'Burgh', 'Berg', 'Burg', 'Burgher', 'Berger', 'Burger', 'Carpenter', 'Chandler', 'Candler', 'Clay', 'Cooper', 'Crafter', 'Glass', 'Glazier', 'Glasier', 'Hammer', 'Maker', 'Mason', 'Masen', 'Masyn', 'Potts', 'Pott', 'Potter', 'Quarrier', 'Quarryman', 'Rock', 'Rockman', 'Rocker', 'Roof', 'Roofe', 'Sawyer', 'Stone', 'Stoneman', 'Townes', 'Towns', 'Towny', 'Wahl', 'Wall', 'Wahls', 'Walls', 'Waller', 'Waxman', 'Wax', 'Wackes', 'Wood', 'Woods'
    ],
    'mountainfolk_surnames': [
        'Billy', 'Billie', 'Bluffe', 'Bluffclimber', 'Boulder', 'Bulder', 'Camp', 'Campman', 'Claymer', 'Clayms', 'Claimer', 'Cole', 'Coler', 'Coleman', 'Coalman', 'Coaler', 'Coaldigger', 'Coledegger', 'Condor', 'Condorman', 'Cragg', 'Cragman', 'Diggs', 'Digger', 'Diggman', 'Digger', 'Diggett', 'Dragonhoard', 'Dragonhord', 'Dragon', 'Drake', 'Dredge', 'Dredger', 'Crystalfist', 'Gemcutter', 'Ironfoot', 'Rockhewer', 'Seamfinder', 'Stonecutter''Hall', 'Haul', 'Heights', 'Hights', 'Hytes', 'Hites', 'Highland', 'Hills', 'Hill', 'Hillclimber', 'Hylltopper', 'Hoard', 'Hord', 'Hoar', 'Hoardigger', 'Hordegger', 'Kidd', 'Kipman', 'Kipper', 'Kipson', 'Kopperfield', 'Miner', 'Myner', 'Mynor', 'Minor', 'Mole', 'Moler', 'Moller', 'Molson', 'Molsen', 'Ores', 'Orr', 'Orrs', 'Oredigger', 'Orrdegger', 'Orson', 'Orrsen', 'Pan', 'Pans', 'Pannerman', 'Panning', 'Peaks', 'Peeks', 'Pike', 'Pyke', 'Pikeclimber', 'Pyketopper', 'Pix', 'Pickman', 'Pickes', 'Pyckes', 'Pickens', 'Quarrier', 'Quarryman', 'Ridge', 'Ridgeclimber', 'Ridgetopper', 'Rock', 'Rockman', 'Rocker', 'Rockridge', 'Snow', 'Snowes', 'Spade', 'Spader', 'Springs', 'Springer', 'Stone', 'Stoneman', 'Underhill', 'Underwood', 'Underman', 'Walker'
    ],
    'merchants_surnames': [
        'Barr', 'Barre', 'Cash', 'Copper', 'Coppers', 'Curry', 'Deals', 'Deels', 'Deel', 'Deelaker', 'Deelman.', 'Diamond', 'Glass', 'Glazier', 'Glasier', 'Gold', 'Golden', 'Goldsmith', 'Goldman', 'Jewels', 'Jules', 'Jewls', 'Lender', 'Lenderman', 'Lynder', 'Mercer', 'Money', 'Munny', 'Monny', 'Munnee', 'Monnee', 'Peppers', 'Pepper', 'Rich', 'Richman', 'Richett', 'Riches', 'Saffron', 'Sage', 'Salt', 'Scales', 'Shine', 'Ships', 'Schipps', 'Shipps', 'Shipman', 'Schippman', 'Silver', 'Sylver', 'Silverman', 'Small', 'Smalls', 'Spicer', 'Spiceman', 'Star', 'Starr', 'Thyme', 'Ware', 'Wool'
    ],
    'mages_surnames': [
        'Altarside', 'Altarworthy', 'Beacon', 'Beecon', 'Beeken', 'Bell', 'Bolt', 'Bolte', 'Bolter', 'Bones', 'Bright', 'Burns', 'Cast', 'Caster', 'Kast', 'Chaplain', 'Chaplin', 'Church', 'Churchside', 'Darko', 'Darkstar', 'Darker', 'Darkbrother', 'Deacon', 'Deecon', 'Deeken', 'Drake', 'Draco', 'Dragon', 'Dreamer', 'Dreemer', 'Dreems', 'Goodbrother', 'Goodman', 'Hecks', 'Heckes', 'Hex', 'Holiday', 'Holliday', 'Holyday', 'Hollier', 'Holly', 'Holier', 'Hollison', 'Hood', 'Kearse', 'Kerse', 'Kerser', 'Curser', 'Monk', 'Munk', 'Nunn', 'Nun', 'Powers', 'Preacher', 'Preecher', 'Priest', 'Preest', 'Sage', 'Sageworthy', 'Saint', 'School', 'Skool', 'Skolar', 'Scholyr', 'Shock', 'Shocker', 'Shaka', 'Skelton', 'Skeltyn', 'Smart', 'Spelling', 'Speller', 'Star', 'Starr', 'Brightstar', 'Teech', 'Teeches', 'Theery', 'Tinker', 'Tutor', 'Tudor', 'Vickers', 'Vykar', 'Vicker', 'Vikars', 'Wise', 'Overwise', 'Worthy', 'Zapp', 'Zappa'
    ],
    'riverfolk_surnames': [
        'Banks', 'Bankes', 'Bend', 'Benderman', 'Blue', 'Bridges', 'Cray', 'Craw', 'Eddy', 'Ferryman', 'Ferrimen', 'Ferry', 'Fisher', 'Fishman', 'Flowers', 'Garr', 'Hook', 'Hooke', 'Hopper', 'Iles', 'Isles', 'Ailes', 'Mills', 'Miller', 'Oars', 'Orrs', 'Orr', 'Oxbow', 'Piers', 'Peers', 'Poleman', 'Polman', 'Porter', 'Rafman', 'Raftman', 'Reed', 'Reede', 'Reedy', 'Reel', 'Reelings', 'River', 'Rivers', 'Salmon', 'Shell', 'Shellman', 'Sheller', 'Shelley', 'Silver', 'Silvermoon', 'Small', 'Smalls', 'Snails', 'Snailman', 'Spanner', 'Stillwater', 'Streams', 'Streems', 'Swimmer', 'Shwimmer', 'Swymmer', 'Trout', 'Waters', 'Watters', 'Waterman', 'Whitewater', 'Wurms', 'Worms'
    ],
    'seafolk_surnames': [
        'Anchor', 'Ankor', 'Anker', 'Ballast', 'Bay', 'Bayes', 'Bayer', 'Bayers', 'Beacon', 'Biggs', 'Bigg', 'Brigg', 'Briggs', 'Bowman', 'Capp', 'Capman', 'Castaway', 'Crabb', 'Crab', 'Crabber', 'Crabman', 'Crest', 'Darkwater', 'Decks', 'Decker', 'Eddy', 'Ferryman', 'Ferrimen', 'Ferry', 'Fisher', 'Fishman', 'Hardy', 'Hardison', 'Harper', 'Helms', 'Helmsman', 'Hook', 'Hooke', 'Iles', 'Isles', 'Ailes', 'Mast', 'Oars', 'Orrs', 'Orr', 'Piers', 'Peers', 'Pitch', 'Pytch', 'Porter', 'Redtide', 'Blacktide', 'Riggs', 'Riggett', 'Sailor', 'Saylor', 'Sailer', 'Sayler', 'Salt', 'Seasalt', 'Saltman', 'Seabreeze', 'Seaman', 'Season', 'Seeman', 'Ships', 'Schipps', 'Shipps', 'Shipman', 'Schippman', 'Shore', 'Shoreman', 'Singer', 'Star', 'Starr', 'Stern', 'Sterne', 'Storm', 'Storms', 'Swimmer', 'Shwimmer', 'Swymmer', 'Tar', 'Tarr', 'Tidewater', 'Tuggs', 'Tugman', 'Waters', 'Watters', 'Waterman', 'Whitewater'
    ],
    'smiths_surnames': [
        'Anvill', 'Anvilson', 'Bellows', 'Black', 'Blackiron', 'Copper', 'Coppers', 'Farrier', 'Fletcher', 'Fletchett', 'Forger', 'Forgeman', 'Goldsmith', 'Grey', 'Greysteel', 'Hammer', 'Hammett', 'Irons', 'Yrons', 'Ironsmith', 'Ironshoe', 'Ironhoof', 'Kettle', 'Kettleblack', 'Kettleman', 'Potts', 'Pott', 'Pottaker', 'Pound', 'Poundstone', 'Shields', 'Shieldson', 'Slagg', 'Slagman', 'Smith', 'Smyth', 'Smitts', 'Smittens', 'Smitty', 'Smythett', 'Smoke', 'Smoker', 'Steel', 'Steele', 'Steelman', 'Swords', 'Swordson', 'Tinn', 'Tinman', 'Tynn', 'Tyne', 'Tine'
    ],
    'soldiers_surnames': [
        'Ackes', 'Ax', 'Archer', 'Bailey', 'Banner', 'Bannerman', 'Bay', 'Bayes', 'Bones', 'Boots', 'Bootes', 'Bowman', 'Chestnut', 'Colt', 'Colter', 'Dice', 'Dyce', 'Dycen', 'Dyson', 'Flagg', 'Flag', 'Helms', 'Hightower', 'Knight', 'Leathers', 'Lethers', 'March', 'Marcher', 'Mares', 'Mayr', 'Mair', 'Marks', 'Mercer', 'Pike', 'Pikes', 'Pyke', 'Pykes', 'Pikeman','Pykeman', 'Poleman', 'Polman', 'Rider', 'Ryder', 'Shields', 'Shieldson', 'Slaughter', 'Spears', 'Speers', 'Swords', 'Swordson', 'Towers', 'Wahl', 'Wall', 'Wahls', 'Walls', 'Waller'
    ],
    'stablehands_surnames': [
        'Bay', 'Bayes', 'Brand', 'Carrier', 'Carryer', 'Carter', 'Carton', 'Cartwright', 'Chestnut', 'Colt', 'Colter', 'Driver', 'Dryver', 'Foote', 'Handler', 'Mares', 'Mayr', 'Mair', 'Porter', 'Quicke', 'Quick', 'Reines', 'Reynes', 'Reins', 'Reyns', 'Rider', 'Ryder', 'Ryde', 'Saddler', 'Stall', 'Stalls', 'Staller', 'Stallworth', 'Stallman', 'Swift', 'Swyft', 'Trainor', 'Trainer', 'Wain', 'Wayne', 'Wayn', 'Wainwright', 'Waynwright'
    ],
    'swampfolk_surnames': [
        'Banks', 'Bankes', 'Black', 'Blacktide', 'Greentide', 'Boggs', 'Bogg', 'Bogs', 'Bull', 'Buzzfly', 'Blackfly', 'Shoefly', 'Cray', 'Craw', 'Cricketts', 'Crickets', 'Darkwater', 'Dragonfly', 'Dragon', 'Eeler', 'Ealer', 'Eeles', 'Eales', 'Fisher', 'Fishman', 'Frogg', 'Frogman', 'Green', 'Greene', 'Greenwater', 'Blackwater', 'Grey', 'Gray', 'Grove', 'Groves', 'Hook', 'Hooke', 'Hopper', 'Marsh', 'Mayfly', 'May', 'Moss', 'Mosstree', 'Greentree', 'Poisonweed', 'Poisonwood', 'Polly', 'Pollywog', 'Polliwog', 'Rafman', 'Raftman', 'Ratt', 'Ratman', 'Reed', 'Reede', 'Reedy', 'River', 'Rivers', 'Rotten', 'Rotman', 'Scales', 'Greenscale', 'Blackscale', 'Shell', 'Shellman', 'Sheller', 'Shelley', 'Skeeter', 'Skito', 'Small', 'Smalls', 'Snails', 'Snailman', 'Stillwater', 'Swimmer', 'Shwimmer', 'Swymmer', 'Thick', 'Thicke', 'Tidewater', 'Vines', 'Waters', 'Watters', 'Wurms', 'Worms'
    ],
    'townfolk_surnames': [
        'Alley', 'Allie', 'Bailey', 'Bell', 'Berg', 'Berger', 'Burg', 'Burger', 'Brickman', 'Brickhouse', 'Bridges', 'Court', 'Gardner', 'Gardiner', 'Hall', 'Heap', 'Hightower', 'Hood', 'House', 'Lane', 'Lain', 'Laine', 'Lodge', 'Lodges', 'Park', 'Parks', 'Plaza', 'Rhoads', 'Rhodes', 'Roades', 'Roof', 'Spanner', 'Stairs', 'Street', 'Streets', 'Towers', 'Towns', 'Townsend', 'Townes', 'Towny', 'Towney', 'Vista', 'Wall', 'Wahl', 'Woodhouse'
    ],
    'woodsfolk_surnames': [
        'Ackes', 'Ax', 'Archer', 'Berry', 'Biggs', 'Bigg', 'Birch', 'Byrch', 'Bird', 'Byrd', 'Birdett', 'Byrdman', 'Bloom', 'Bowman', 'Branch', 'Brush', 'Buck', 'Deere', 'Deerman', 'Doe', 'Feller', 'Fletcher', 'Flowers', 'Forester', 'Forrester', 'Forrest', 'Fox', 'Foxx', 'Gardner', 'Gardener', 'Gardiner', 'Green', 'Greene', 'Grove', 'Groves', 'Harper', 'Hatchet', 'Hunter', 'Huntsman', 'Hyde', 'Hides', 'Hydes', 'Jack', 'Lodge', 'Lodges', 'Meadows', 'Mole', 'Moler', 'Moller', 'Moss', 'Mosstree', 'Greentree', 'Oaks', 'Oakes', 'Pine', 'Pines', 'Pyne', 'Pynes', 'Sawyer', 'Silver', 'Silvermoon', 'Singer', 'Springs', 'Springer', 'Strider', 'Stryder', 'Tanner', 'Tannerman', 'Thick', 'Thicke', 'Walker', 'Woods', 'Wood', 'Woode', 'Wooden', 'Woodyn'
    ]
}

aarakocra_name_sounds = [
    'click','trill','whistle','hoot','laugh','screech','caw','whinny','coo',''
]

aarakocra_nicknames1 = [
    'ak', 'clour', 'di', 'du', 'ecc', 'er', 'gre', 'hur', 'kli', 'kou', 'qha', 'quc', 'rhe', 'ri', 'sa', 'uc', 'ui', 'ur'
]
aarakocra_nicknames2 = [
    'el','ker','re','rar','er','i','ki','ca','ci'
]
aarakocra_nicknames3 = [
    'erk','ak','ca','iek','ef','is','e','r','f','a','ad','r','rk','el','le','k'
]

aasimar_names1 = [
    'an', 'az', 'cach', 'cath', 'el', 'gam', 'ham', 'ia', 'kar', 'kas', 'ma', 'on', 'perp', 'rad', 'sal', 'soph', 'zar', 'zu'
]
aasimar_names2 = [
    'uan','em','er','et','az','ur','ath','al'
]
aasimar_names3 = [
    'iel','iah','za','ael','ma','oel','el','al','ion'
]

bugbear_names1 = [
    'nan','gov','tat','zar','bal','thi','rath','vir','vamk','rut','tor','nud','namk','nor','bod','rar','gin','tik','dor','gan','dur','tin',
]
bugbear_names2 = [
    'r','k','h','n'
]

male_centaur_names1 = [
    'Aug','Bo','Cho','Dri','Eno','Ko','Or','Ske','To','Ya',
]
male_centaur_names2 = [
    'h','r','z','v','l','m','n'
]
male_centaur_names3 = [
    'us','mod','di','ios','o','im','val','or','is','og'
]

female_centaur_names1 = [
    'bi','dun','gal','ho','kot','mel','mi','pin','ra','sa','tat',
]
female_centaur_names2 = [
    'is','no','ya','is'
]
female_centaur_names3 = [
    'do','ja','nya','tia','li','oe','ra','ya','na'
]

centaur_clan_names1 = [
    "Aspen", "Autumn", "Birch", "Bloom", "Boulder", "Brook", "Brown", "Bright", "Brush", "Burrow", "Cedar", "Crater", "Creek", "Drift", "Dust", "Earthen", "Elm", "Fall", "Flood", "Fog", "Forest", "Grass", "Green", "Grove", "Hail", "Hazel", "Hill", "Hollow", "Ice", "Iron", "Laurel", "Maple", "Moon", "Moss", "Mountain", "Oaken", "Peak", "Pine", "Plain", "Rain", "Ridge", "River", "Rock", "Snow", "Spring", "Star", "Stone", "Storm", "Summer", "Sun", "Thorn", "Timber", "Valley", "Vine", "Willow", "Winter", "Wood", "Yew"
]
centaur_clan_names2 = [
    "bark", "basker", "bearer", "binder", "blade", "blesser", "blossom", "blossoms", "borne", "braid", "braider", "braids", "breaker", "bringer", "bruiser", "caller", "carver", "catcher", "chanter", "charger", "chaser", "cleanser", "conqueror", "crest", "dancer", "darter", "defender", "divider", "dreamer", "drinker", "eyes", "fader", "fighter", "force", "forcer", "former", "gatherer", "glow", "groom", "groomer", "guard", "heart", "herald", "hold", "hoof", "laugh", "leaf", "leaper", "leaves", "limp", "love", "mane", "mangle", "march", "mask", "mind", "muse", "pass", "pelt", "petals", "prowl", "prowler", "push", "reign", "rest", "reveler", "ride", "rise", "roamer", "roar", "run", "runner", "rush", "rusher", "scorn", "screamer", "seeker", "shadow", "shield", "shifter", "shine", "sign", "sleep", "slumber", "smile", "smirk", "spark", "spell", "stare", "strength", "tail", "temper", "thread", "trampler", "tree", "twister", "voice", "volley", "wander", "wanderer", "watch", "watcher", "whisper", "whisperer", "wish"
]

changeling_names1 = [
    "", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"
]
changeling_names2 = [
    "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai", "oo", "ou"
]
changeling_names3 = [
    "c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"
]

# dragonborn naming format = clan, surname, name
male_dragonborn_names1 = [
    'ar','ba','bal','bh','do','ghe','he','kri','me','na','pa','pan','rho','sha','she','tar','tor'
]
male_dragonborn_names2 = [
    'jha','lasa','ara','na','e','ska','dra','he','dar','dje','tri','ga','ma','din','hu','in'
]
male_dragonborn_names3 = [
    'n','r','sh','ar','d','v'
]
female_dragonborn_names1 = [
    'ak','bi','da','fa','ha','jhe','ka','ko','mi','na','per','rai','so','su','tha','ua','ra'
]
female_dragonborn_names2 = [
    'rid','ran','vil','rin','shan','an','rin','dj'
]
female_dragonborn_names3 = [
    'ra','ri','ar','eh','n','ar','va','la','ra','a','it'
]
dragonborn_clan_names1 = [
    'cleth','da','del','drac','fen','kep','ker','kim','lin','my','nem','nor','oph','pre','shes','tur','ver','yar'
]
dragonborn_clan_names2 = [
    'tin','ard','mir','hed','ken','eshk','rhy','ba','xa','ka','tha','il','end','ka','bra','mol','tu','send','as','mon','ix','in','sh','ta','la','ji','xi','jan','di','ten','del','nur','this','ath','ur','gi','jer'
]
dragonborn_clan_names3 = [
    'lor','rian','ev','ion','don','ik','lon','ul','alor','tan','is','ius','ir','lin','iath','oth','esh','it'
]

dwarf_male_names1 = [
    'ad','albe','ba','bar','brot','bru','da','dar','del','eb','ein','far','f','gar','har','kil','mor','or','os','ran','ru','tak','thor','tor','trau','tra','ulf','ve','von'
]
dwarf_male_names2 = [
    'rik','rich','ern','end','tor','enor','in','rak','g','erk','kil','grim','lint','dain','bek','drak','gran','sik','kar','linn','adin','dek','bon','vok','gar','it','dal'
]
dwarf_female_names1 = [
    'am','ar','aud','bar','dag','di','eld','falk','fin','gun','gur','hel','h','ka','kri','il','lift','mard','ris','san','torb','torg','vis'
]
dwarf_female_names2 = [
    'ber','tin','hild','dryn','nal','esa','eth','run','ellen','loda','dis','ja','lin','thra','stryd','de','rasa','red','wynn','nl','era','tra'
]
dwarf_surnames1 = [
    'axe','battle','boulder','brawn','bronze','copper','deep','ember','fire','flint','frost','gem','gold','granite','iron','rock','silver','steel','stone','strong','swift','thunder'
]
dwarf_surnames2 = [
    'anvil','axe','beard','belly','breaker','bringer','brow','delver','finger','fist','foot','forge','grasp','grip','guard','hammer','heart','helm','hide','mantle','pick','shield','smith','spine','stone'
]
dwarf_surnames3 = [
    'bald', 'dan','gor','holder','lod','lut','rumna','strak','tor','un'
]
dwarf_surnames4 = [
    'derk','kil','unn','hek','err','gehr','heim','eln','gart'
]




elf_high_surnames1 = [
    'Amakiir', 'Amastacia', 'Galanodel', 'Holimion', 'Ilphelkiir', 'Liadon', 'Meliamne', "Nai'lo", 'Siannodel', 'Xiloscient'
]
elf_high_surnames_translation1 = [
    'dawn','diamond','frost','gem','gold','moon','night','silver','spell','star','sun','wind','winter'
]
elf_high_surnames_translation2 = [
    'blade','bloom','blossom','born','borne','breeze','brook','caller','caster','dew','dust','fire','flower','heel','leaf','petal','pond','shade','shadow','strider','thorn','weaver','whisper','wind',
]
elf_child_names1 = [
    'a','b','d','e','fa','in','la','mel','na','ph','r','ra','s','syl','th','v',
]
elf_child_names2 = [
    'ra','ryn','el','en','nil','el','la','ill','eris','ann','inn','ai','lin','ia','all'
]

nature_adjectives = [
    'abloom', 'active', 'airy', 'alive', 'alluring', 'appealing', 'arctic', 'arresting', 'autumn', 'awakening', 'barren', 'beach', 'beautiful', 'beguiling', 'blazing', 'blissful', 'blooming', 'blossoming', 'blue', 'breathtaking', 'breezy', 'bright', 'budding', 'bustling', 'buzzing', 'cave', 'changing', 'charming', 'cheerful', 'chirping', 'clean', 'cliff', 'cloudless', 'cloudy', 'coast', 'colorful', 'countryside', 'crisp', 'crumbling', 'deciduous', 'delightful', 'dense', 'desert', 'desolate', 'devoid', 'dotted', 'dreary', 'dusky', 'earth', 'earthy', 'elegant', 'enchanting', 'enjoyable', 'enticing', 'environment', 'ethereal', 'expansive', 'exquisite', 'fair', 'fascinating', 'fertile', 'field', 'flawless', 'flood', 'floral', 'flourishing', 'forest', 'fragrant', 'fresh', 'gentle', 'grassy', 'green', 'growing', 'happy', 'harsh', 'healthy', 'heavenly', 'hill', 'ice', 'ideal', 'incredible', 'inspiring', 'invigorating', 'island', 'joyful', 'lake', 'land', 'light', 'lively', 'lovely', 'luscious', 'lush', 'massive', 'meadow', 'melting', 'moon', 'mountain', 'mountainous', 'new', 'newborn', 'ocean', 'outdoor', 'paradisiac', 'parched', 'pastel', 'peaceful', 'picturesque', 'planet', 'pleasant', 'pretty', 'pure', 'quaint', 'rain', 'rainforest', 'rainy', 'refreshing', 'rejuvenating', 'relaxing', 'renewing', 'river', 'sea', 'season', 'seasonal', 'sky', 'sleet', 'snow', 'soft', 'sparkling', 'special', 'spectacular', 'spring', 'sprouting', 'stars', 'summer', 'sun', 'sunny', 'sunshine', 'sweet', 'swimming', 'teeming', 'temperature', 'tender', 'thriving', 'towering', 'undulating', 'unforgiving', 'unique', 'unpredictable', 'valley', 'verdant', 'vernal', 'vibrant', 'vivid', 'volcano', 'warm', 'wild', 'windswept', 'windy', 'winter', 'wondrous', 'wooded', 'woodland', 'young'
]
nature_nouns = [
    'badger','bear','boar','bull','deer','dolphin','dragon','eagle','falcon','fish','fox','griffin','heron','horse','hound','leopard','lion','lynx','otter','owl','peacock','pelican','ram','salmon','serpent','sparrowhawk','stag','swan','tiger','unicorn','wolf',
    'boulder','cave','cloud','desert','field','flower','forest','fruit','grass','hill','lake','meadow','moon','moss','mountain','mushroom','ocean','pebble','rainbow','river','rock','sand','seed','shell','snow','star','sun','tree','valley','root','waterfall','wave',
    'acorn','angel','badger','beaver','boar','bull','cockatrice','crab','crane','deer','dolphin','dove','dragon','falcon','fish','forest','fox','frog','goat','heart','horse','hound','hydra','laurel','leopard','lizard','nightingale','oak','ostrich','owl','peacock','pheonix','rabbit','rainbow','ram','raven','rock','rose','salamander','salmon','savage','shell','stag','swan','wolf','wood','wyvern',
]

generic_names1 = [
    'amber', 'angry', 'ardent', 'azure', 'bittersweet', 'black', 'blasted', 'brass', 'brilliant', 'broken', 'bronze', 'burnt', 'cold', 'cornsilk', 'crimson', 'dagger', 'dark', 'diamond', 'dreaming', 'drowsy', 'dry', 'dusty', 'ebon/ebony', 'emerald', 'fire', 'fleet', 'gold/golden', 'good', 'grace', 'grand', 'gray', 'great', 'green', 'hammer', 'hasty', 'hazy', 'helm', 'high', 'holy', 'honey', 'hot', 'ice/icy', 'iron', 'ivory', 'kings', 'lilac', 'little', 'maple', 'mighty', 'night', 'oak/oaken', 'onyx', 'peaceful', 'pearl', 'prancing', 'quartz', 'queens', 'rain/rainy', 'red', 'rose/rosy', 'royal', 'ruby', 'sable', 'sacred', 'sage', 'sand', 'sapphire', 'screaming', 'shale', 'shining', 'short', 'silk/silken', 'silver', 'sleeping', 'small', 'snow', 'solid', 'steel', 'sterling', 'storm', 'strong', 'summer', 'swift', 'sword', 'tawny', 'thunder', 'topaz', 'tranquil', 'vast', 'verdant', 'vile', 'violet', 'virgin', 'whisper', 'white', 'wicked', 'wild', 'wind', 'winter', 'xanthous'
]
generic_names2 = [
    'beach', 'bear', 'bluff', 'boar', 'brook', 'butte', 'castle', 'cave', 'circle', 'cliff', 'coast', 'crag', 'creek', 'crescent', 'crevasse', 'crow', 'crown', 'dale', 'dark', 'dragon', 'dunes', 'eagle', 'elk', 'field', 'fist', 'ford', 'forest', 'fountain', 'fox', 'gale', 'gauntlet', 'glade', 'goose', 'griffin', 'grove', 'gulf', 'hall', 'hedge', 'hill', 'hold', 'hole', 'isle', 'keep', 'lake', 'light', 'lion', 'lord', 'maiden', 'march', 'mare', 'mark', 'marsh', 'maze', 'meet', 'mine', 'mirror', 'oasis', 'orchard', 'owl', 'path', 'peak', 'plain', 'point', 'pony', 'pool', 'prison', 'quest', 'reach', 'reef', 'ridge', 'ring', 'river', 'road', 'rock', 'rush', 'sea', 'serpent', 'shell', 'shield', 'shore', 'sky', 'square', 'stag', 'star', 'steed', 'stone', 'stream', 'sun', 'tear', 'tiger', 'tower', 'unicorn', 'vale', 'valley', 'wall', 'wash', 'water', 'way', 'wolf', 'wood'
]

nicknames = [
    'climber','earbender','leaper','pious','shieldbiter','zealous',
    "Ace", "Admiral", "Aggy", "Angel", "Animal", "Answer", "Aqua", "Arrow", "Artsy", "Assassin", "Babe", "Baby", "Bad Boy", "Baldy", "Bambam", "Barber", "Bash", "Basher", "Beans", "Bear", "Beard", "Beast", "Beau", "Beauty", "Belle", "Berry", "Big Boy", "Big Dog", "Bigby", "Biggie", "Bigshot", "Bing", "Bingo", "Bird", "Birds", "Bitsy", "Black Magic", "Black Widow", "Blackjack", "Blade", "Blessed", "Blondie", "Blossom", "Blue", "Blush", "Bo", "Bobo", "Bones", "Boogie", "Boomer", "Boots", "Braveheart", "Brick", "Brow", "Buck", "Bucket", "Bud", "Buddy", "Bugs", "Bull", "Bulldog", "Bullet", "Bullseye", "Bunny", "Buster", "Butch", "Butcher", "Butterfly", "Buzz", "Camille", "Candy", "Cannonball", "Captain", "Chappie", "Charisma", "Cheery", "Chef", "Chief", "Chip", "Chipper", "Chuck", "Cloud", "Cobra", "Comet", "Coocoo", "Cookie", "Coyote", "Crash", "Creed", "Creep", "Crow", "Cryo", "Crystal", "Cuddles", "Curles", "Cutie", "Cyclone", "Cyclops", "Daddy", "Dagger", "Dandy", "Dapper", "Daring", "Darlin", "Darling", "Dash", "Dawg", "Daydream", "Dazzle", "Dealer", "Deedee", "Delight", "Demon", "Devil", "Diamond", "Dice", "Digger", "Dimple", "Dino", "Dizzy", "Doc", "Dodo", "Dog", "Doggie", "Double", "Double Trouble", "Dragon", "Dream", "Ducky", "Duke", "Dumdum", "Dummy", "Dusty", "Dutch", "Dynamite", "Eagle", "Fancy", "Feathers", "Fire", "Fish", "Flame", "Flash", "Flip", "Flutters", "Fortuna", "Fox", "Freak", "Frosty", "Fury", "Fuzz", "Fuzzy", "Gator", "Gem", "Genie", "Genius", "Gentle", "Gibbs", "Gibby", "Gigi", "Gilly", "Ginger", "Glide", "Gonzo", "Goose", "Grace", "Grim", "Groovy", "Grouch", "Growl", "Guns", "Gus", "Hammer", "Handsome", "Happy", "Hawk", "Hawkeye", "Hog", "Honesty", "Honey", "Hooks", "Horse", "Hound", "Hurricane", "Ice", "Icicle", "Indie", "Iron", "Izzy", "Jackal", "Jacket", "Jackhammer", "Jade", "Jazzy", "Jelly", "Jewel", "Joker", "Jolly", "Jumbo", "Jumper", "Kiki", "Killer", "Kindle", "King", "Knight", "Landslide", "Lightning", "Lion", "Lioness", "Little", "Lock", "Loco", "Lucky", "Mac", "Machine", "Mad", "Mad Dog", "Magic", "Magica", "Magician", "Major", "Mamba", "Mania", "Maniac", "Marvel", "Mayor", "Mellow", "Memo", "Merry", "Micro", "Miracle", "Missile", "Mistletoe", "Mitzi", "Monk", "Moose", "Mouse", "Mugs", "Mugsy", "Mule", "Mutt", "Navigator", "Nimble", "Old Buck", "Oracle", "Ox", "Peanut", "Penny", "Petit", "Pig", "Piggy", "Pipi", "Pitch", "Pogo", "Poncho", "Pops", "Porky", "Pretzel", "Prince", "Princess", "Pug", "Pugs", "Punch", "Pyro", "Queen Bee", "Queenie", "Rags", "Reaper", "Rebel", "Red", "Rip", "Ripper", "Robin", "Rock", "Rogue", "Rose", "Rouge", "Ruby", "Ruin", "Rusty", "Sage", "Sailor", "Sandy", "Sassy", "Scoop", "Scruffy", "Serpent", "Shade", "Shadow", "Shark", "Sheep", "Shorty", "Shrimp", "Shy", "Silence", "Silly", "Silver", "Sizzle", "Sketch", "Skin", "Skinny", "Skip", "Skipper", "Skippy", "Slash", "Slayer", "Slick", "Slide", "Slim", "Small", "Smash", "Smasher", "Smiley", "Smitty", "Smoothie", "Snake", "Snowflake", "Spark", "Sparkle", "Sparky", "Sparrow", "Special", "Speed", "Spider", "Spike", "Spud", "Spuds", "Starfall", "Steel", "Sticks", "Stone", "Storm", "Stout", "Stretch", "Stuffy", "Sugar", "T-Bone", "Tank", "Terminator", "Thief", "Thunder", "Tiger", "Tigress", "Tiny", "Titch", "Toon", "Torch", "Trey", "Tricky", "Trouble", "Tug", "Turk", "Twinkle", "Twinkle Toes", "Twitch", "Uncle", "Undertaker", "Vanilla", "Viper", "Vulture", "Wheels", "Whopper", "Wiggles", "Wild", "Wildy", "Wiz", "Wonder", "Worm", "Yank", "Zen", "Zero", "Ziggy"
]


def nameGen(race, subrace, sex):
    name = ''
    name_int = random.randint(1,10)
    name_bool = random.choice([True,False])
    if sex == 'androgynous':
        sex = random.choice(['male','female'])
    name_key = name_data[race][sex]
    if subrace != '':
        name_key = name_data[race][subrace][sex]
    if race == 'aarakocra':
        name_key = name_data[race]
        rnd1 = random.choice(name_key['names1'])
        rnd3 = random.choice(name_key['names3'])
        if name_int < 6:
            rnd2 = random.choice(name_key['names2'])
            while rnd2 == rnd3:
                rnd2 = random.choice(name_key['names2'])
            nick = rnd1 + rnd2 + rnd3
        if name_int > 5:
            nick = rnd1 + rnd3
        nick = testSwear.testSwear(nick)
        if nick == '':
            nameGen(race,subrace,sex)
        rnd4 = random.choice(name_key['name_sounds'])
        rnd5 = random.choice(name_key['name_sounds'])
        if name_int < 6:
            rnd6 = random.choice(name_key['name_sounds'])
            name = rnd1 + '-' + rnd4 + '-' + rnd2 + '-' + rnd5 + '-' + rnd3 + '-' + rnd6
        if name_int > 5:
            name = rnd1 + '-' + rnd4 + '-' + rnd3 + '-' + rnd5
        name = testSwear.testSwear(name)
        if name == '':
            nameGen(race,subrace,sex)
        else:
            return name, nick
    if race == 'aasimar':
        name_key = name_data[race]
        rnd1 = random.choice(name_key['names1'])
        rnd3 = random.choice(name_key['names3'])
        if name_int < 6:
            rnd2 = random.choice(name_key['names2'])
            while rnd2 == rnd3:
                rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2 + rnd3
        if name_int > 5:
            name = rnd1 + rnd3
        name = testSwear.testSwear(name)
        if name == '':
            nameGen(race,subrace,sex)
        else:
            return name
    if race == 'bugbear':
        name_key = name_data[race]
        rnd1 = random.choice(name_key['names1'])
        rnd2 = random.choice(name_key['names1'])
        while rnd1 == rnd2:
            rnd2 = random.choice(name_key['names1'])
        if name_int < 6:
            rnd3 = random.choice(name_key['names2'])
            if name_int < 8:
                name = rnd3 + rnd1 + rnd2
            if name_int >= 8:
                name = rnd1 + rnd2 + rnd3
        if name_int > 5:
            name = rnd1 + rnd2
        name = testSwear.testSwear(name)
        if name == '':
            nameGen(race,subrace,sex)
        else:
            return name
    if race == 'centaur':
        if sex == 'male':
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            if name_int < 6:
                rnd2 = random.choice(name_key['names2'])
                while rnd2 == rnd3:
                    rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_int > 5:
                name = rnd1 + rnd3
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
        if sex == 'female':
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            if name_int < 6:
                rnd2 = random.choice(name_key['names2'])
                while rnd2 == rnd3:
                    rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_int > 5:
                name = rnd1 + rnd3
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
    if race == 'changeling':
        name_key = name_data[race]
        rnd1 = random.choice(name_key['names1'])
        rnd2 = random.choice(name_key['names2'])
        rnd3 = random.choice(name_key['names3'])
        while rnd1 == rnd3:
            rnd3 = random.choice(name_key['names3'])
        if rnd1 == "":
            name = rnd2 + rnd3
        if rnd1 != "":
            name = rnd1 + rnd2 + rnd3
        name = testSwear.testSwear(name)
        if name == '':
            nameGen(race,subrace,sex)
        else:
            return name
    if race == 'dragonborn':
        if sex == 'male':
            if name_int < 4:
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                name = rnd1 + rnd3
            if name_int > 3:
                rnd1 = random.choice(name_key['names1'])
                rnd2 = random.choice(name_key['names2'])
                rnd3 = random.choice(name_key['names3'])
                name = rnd1 + rnd2 + rnd3
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
        if sex == 'female':
            if name_int < 4:
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                name = rnd1 + rnd3
            if name_int > 3:
                rnd1 = random.choice(name_key['names1'])
                rnd2 = random.choice(name_key['names2'])
                rnd3 = random.choice(name_key['names3'])
                while rnd1 == rnd3:
                    rnd3 = random.choice(name_key['names3'])
                name = rnd1 + rnd2 + rnd3
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
    if race == 'dwarf':
        if sex == 'male':
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
        if sex == 'female':
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
    if race == 'elf':
        if sex == 'boy' or sex == 'girl':
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            while rnd1 == rnd2:
                rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2
        else:
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            while rnd1 == rnd3:
                rnd3 = random.choice(name_key['names3'])
            if name_bool == True:
                rnd2 = random.choice(name_key['names2'])
                while rnd2 == rnd1 or rnd2 == rnd3:
                    rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_bool == False:
                name = rnd1 + rnd3
            name = testSwear.testSwear(name)
            if name == '':
                nameGen(race,subrace,sex)
            else:
                return name
    if race == 'human':
        if subrace == 'calishite':
            for i in range(2):
                if sex == 'male':
                    rnd1 = random.choice(name_key['names1'])
                    rnd3 = random.choice(name_key['names3'])
                    if random.choice([True,False]):
                        rnd2 = random.choice(name_key['names2'])
                        name = rnd1 + rnd2 + rnd3
                    else:
                        name = rnd1 + rnd3
                    name = testSwear.testSwear(name)
                    if name == '':
                        nameGen(race, subrace, sex)
                    if i == 0:
                        myname = name
                    else:
                        pname = name
                        return myname, pname
                if sex == 'female':
                    rnd1 = random.choice(name_key['names1'])
                    rnd3 = random.choice(name_key['names3'])
                    if random.choice([True,False]):
                        rnd2 = random.choice(name_key['names2'])
                        while rnd2 == rnd3:
                            rnd2 = random.choice(name_key['names2'])
                        name = rnd1 + rnd2 + rnd3
                    else:
                        name = rnd1 + rnd3
                    name = testSwear.testSwear(name)
                    if name == '':
                        nameGen(race, subrace, sex)
                    if i == 0:
                        myname = name
                    else:
                        pname = name
                        return myname, pname
        if subrace == 'cadonian':
            if sex == 'male':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if sex == 'female':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if name != '':
                name = testSwear.testSwear(name)
                if name == '':
                    nameGen(race, subrace, sex)
                else:
                    return name
        if subrace == 'damaran':
            if sex == 'male':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    while rnd2 == rnd3:
                        rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if sex == 'female':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                while rnd1 == rnd3:
                        rnd3 = random.choice(name_key['names2'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    while rnd2 == rnd3:
                        rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if name != '':
                name = testSwear.testSwear(name)
                if name == '':
                    nameGen(race, subrace, sex)
                else:
                    return name
        if subrace == 'skan':
            if sex == 'male':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if sex == 'female':
                rnd1 = random.choice(name_key['names1'])
                rnd3 = random.choice(name_key['names3'])
                while rnd1 == rnd3:
                        rnd3 = random.choice(name_key['names3'])
                if name_int < 6:
                    rnd2 = random.choice(name_key['names2'])
                    while rnd2 == rnd3:
                        rnd2 = random.choice(name_key['names2'])
                    name = rnd1 + rnd2 + rnd3
                if name_int > 5:
                    name = rnd1 + rnd3
            if name != '':
                name = testSwear.testSwear(name)
                if name == '':
                    nameGen(race, subrace, sex)
                else:
                    return name
    else:
        return 'No Race'



def surnameGen(race, subrace, job, job_type):
    name = 'No Surname'
    name_int = random.randint(1,10)
    name_bool = random.choice([True,False])
    name_key = name_data[race]['surname']
    if subrace != '':
        name_key = name_data[race][subrace]['surname']
    job_key = job_type + '_surnames'
    if race == 'centaur':
        rnd1 = random.choice(name_key['names1'])
        rnd2 = random.choice(name_key['names2'])
        while rnd1 == rnd2:
            rnd2 = random.choice(name_key['names2'])
        name = rnd1 + rnd2
    if race == 'dragonborn':
        if name_int < 4:
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            rnd3 = random.choice(name_key['names3'])
            name = rnd1 + rnd2 + rnd3
        if name_int > 3 and name_int < 8:
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            rnd3 = random.choice(name_key['names2'])
            while rnd2 == rnd3:
                rnd3 = random.choice(name_key['names2'])
            rnd4 = random.choice(name_key['names3'])
            name = rnd1 + rnd2 + rnd3 + rnd4
        if name_int > 7:
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            rnd3 = random.choice(name_key['names2'])
            while rnd2 == rnd3:
                rnd3 = random.choice(name_key['names2'])
            rnd4 = random.choice(name_key['names2'])
            while rnd3 == rnd4:
                rnd4 = random.choice(name_key['names2'])
            rnd5 = random.choice(name_key['names3'])
            name = rnd1 + rnd2 + rnd3 + rnd4 + rnd5
    if race == 'dwarf':
        if name_bool == True:
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            while rnd1 == rnd2:
                rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2
        if name_bool == False:
            rnd1 = random.choice(name_key['names3'])
            rnd2 = random.choice(name_key['names4'])
            while rnd1 == rnd2:
                rnd2 = random.choice(name_key['names4'])
            name = rnd1 + rnd2
    if race == 'elf':
        rnd1 = random.choice(name_key['names1'])
        rnd2 = random.choice(name_key['names2'])
        while rnd1 == rnd2:
            rnd2 = random.choice(name_key['names2'])
        name = rnd1 + rnd2
    if race == 'human':
        if subrace == 'calishite':
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            if name_bool == True:
                rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_bool == False:
                name = rnd1 + rnd3
        if subrace == 'cadonian':
            rnd1 = random.choice(name_key['names1'])
            rnd2 = random.choice(name_key['names2'])
            name = rnd1 + rnd2
            if job_key in job_surnames:
                name = random.choice(job_surnames[job_key])
        if subrace == 'damaran':
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            if name_bool == True:
                rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_bool == False:
                name = rnd1 + rnd3
        if subrace == 'skan':
            rnd1 = random.choice(name_key['names1'])
            rnd3 = random.choice(name_key['names3'])
            if name_bool == True:
                rnd2 = random.choice(name_key['names2'])
                name = rnd1 + rnd2 + rnd3
            if name_bool == False:
                name = rnd1 + rnd3 
    name = testSwear.testSwear(name)
    if name == '':
        surnameGen(race, subrace, job, job_type)
    return name       



def titleGen(job):
    if job in socialGen.jobs['noble']:
        title = 'of ' + job + 's'
        return title
    elif job in socialGen.jobs['townfolk']:
        title = 'of ' + job + 's'
        return title
    else:
        return ''


if __name__ == "__main__":
    name = ''
    title = ''
    pname = ''
    surname = ''
    clan = ''

    race = 'elf'
    subrace = 'high'
    sex = 'male'
    job, job_type = socialGen.jobGen(sex)

    name = nameGen(race, subrace, sex)
    surname = surnameGen(race, subrace, job, job_type)
    title = titleGen(job)

    if len(name) == 2:
        name, pname = name
    else:
        pass

    print(name, title, pname, surname)


