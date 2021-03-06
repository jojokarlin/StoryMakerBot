#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

character = [
    "girl",
    "boy",
    "hero",
    "heroine",
    "sacrificial redeemer",
    "teen crusader",
    "zombie",
    "witch",
    "wizard",
    "werewolf",
    "vampire",
    "teen",
]

adverb = [
    "accidentally",
    "always",
    "angrily",
    "anxiously",
    "awkwardly",
    "badly",
    "blindly",
    "boastfully",
    "boldly",
    "bravely",
    "brightly",
    "cheerfully",
    "coyly",
    "crazily",
    "defiantly",
    "deftly",
    "deliberately",
    "devotedly",
    "doubtfully",
    "dramatically",
    "dutifully",
    "eagerly",
    "elegantly",
    "enormously",
    "evenly",
    "eventually",
    "exactly",
    "faithfully",
    "finally",
    "foolishly",
    "fortunately",
    "frantically",
    "frequently",
    "gleefully",
    "gracefully",
    "happily",
    "hastily",
    "honestly",
    "hopelessly",
    "hourly",
    "hungrily",
    "innocently",
    "inquisitively",
    "irritably",
    "jealously",
    "justly",
    "kindly",
    "lazily",
    "loosely",
    "madly",
    "merrily",
    "mortally",
    "mysteriously",
    "nervously",
    "never",
    "obediently",
    "obnoxiously",
    "occasionally",
    "often",
    "only",
    "perfectly",
    "politely",
    "poorly",
    "powerfully",
    "promptly",
    "quickly",
    "rapidly",
    "rarely",
    "really",
    "regularly",
    "rudely",
    "safely",
    "seldom",
    "selfishly",
    "seriously",
    "shakily",
    "sharply",
    "silently",
    "slowly",
    "solemnly",
    "sometimes",
    "speedily",
    "steadily",
    "sternly",
    "technically",
    "tediously",
    "tenderly",
    "terrifically",
    "tightly",
    "totally",
    "tremendously",
    "unexpectedly",
    "usually",
    "victoriously",
    "vivaciously",
    "warmly",
    "wearily",
    "weekly",
    "wildly",
    "yearly",
    ]

verb = [
   	
    "dine",	
    "gasp",	
    "huff",	
    "sigh",	
    "snap",	
    "guffaw",	
    "snicker",	
    "bellow",	
    "holler",	
    "howl",	
    "lament",	
    "shriek",	
    "wail",	
    "blabber",	
    "bluster",	
    "gush",	
    "scoff",	
    "snuffle",	
    "arrive",	
    "exit",	
    "journey",	
    "mount",	
    "burrow",	
    "sink",	
    "gel",	
    "evolve",	
    "gloat",	
    "wallow",	
    "dwell",	
    "spatter",	
    "spew",	
    "sprinkle",
    "float",	
    "glide",	
    "lounge",	
    "amble",	
    "creep",	
    "dawdle",	
    "lope",	
    "stagger",	
    "bolt",	
    "scurry",	
    "flounce",	
    "stroll",	
    "stride",	
    "meander",	
    "plod",	
    "saunter",	
    "wander",	
    ]

preposition = [
    "on",
    "with",
    "after",
    "beside",
    "along with",
    "instead of",
    "for",
    "behind",
    ]

adj = [
    "hungry",
    "furious",
    "wandering",
    "magical",
    "mysterious",
    "peculiar",
    "bizarre",
    "freak",
    "rambunctious",
    "cantankerous",
    "mediocre",
    "mellifluous",
    "malicious",
    "malignant",
    "benevolent",
    "repulsive",
    "colossal",
    "hissing",
    "crooked",
    "faint",
    "zealous",
    "clandestine",
    "witty",
    "wizened",
    "dusty",
    "destructive",
    "miserable",
    "baleful",
    "blustering",
    "capricious",
    "colorful",
    "dashing",
    "furtive",
    "finnicky",
    "gregarious",
    "gullible",
    "humble",
    "harried",
    "jovial",
    "jocular",
    "kinetic",
    "liminal",
    "listless",
    "lugubrious",
    "dour",
    "dubious",
    "fickle",
    "loquacious",
    "nascent",
    "polite",
    "querulous",
    "rascally",
    "strident",
    "strict",
    "troubled",
    "tenacious",
    "contrite",
    "trivial",
    "vivacious",
    "virulent",
    "tyrannical",
    "wistful",
    
        ]
obj = [
    "girl",
    "king",
    "dog",
    "giant",
    "robot",
    "zombie",
    "boy",
    "snake",
    "dragon",
    "boy",
    "mother",
    "stepmother",
    "stepfather",
    "father",
    "grandfather",
    "vampire",
    "dictator",
    "bullies",
    "mean girls",
    "adults",
    "environmental agency",
    
    
    ]

def story_gen():
    return("A %s %s %ss %s a %s %s." %(random.choice(character),random.choice(adverb),random.choice(verb),random.choice(preposition), random.choice(adj),random.choice(obj)))

print(story_gen())

tfile = open("tweets.txt", "w")
for numtweets in range(0,100):
    tfile.write(story_gen())
    tfile.write("\n")

tfile.close()
