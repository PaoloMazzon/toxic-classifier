from TMP import ToxicityDetector
from statistics import median

# CONTENT WARNING - Plenty of offensive comments ahead. This file exists
# for research purposes in regards to the paper "Detecting Toxicity with
# Linear Regression Models," please do not repeat anything here outside of
# research purposes. I do NOT condone toxic behaviour online, that's the
# very reason this file and tool exists.
prompts = {
    "targetted": [
        "shut the fuck up dude",
        "nobody wants to hear it",
        "nobody cares",
        "go die in a hole",
        "nobody likes you here",
        "kill yourself",
        "eat shit",
        "gg noob mid invoker",
        "i mean not everyone on ur team is dumb enough to rot down to 20% hp",
        "ur asshole",
        "lowskill shits  all you have to do is dive endlessly  and this cunt silencer and invoekr  let you win",
        "He's never picked in pubs, and the only bracket he has over 50% win rate is 'very high skill' on asian servers.  So shut up and pick something fun.  You cucks.",
        "i fuck ur family  NOOB",
        "i pumped a load of cum into your mums ass hole last night",
        "noob",
        "dsnt make a diff i come or not  fuckin dickhead",
        "1k mmr dumb shit  Freaking dumb shit reportt axe  end plz",
        "pls report doom  this idiot has never fought with us",
        "lol that bitch  too early too say ez",
        "i thought junglers couldnt get any worse",
        "are you ready  you shits  to get dumpstered  by my legendary slardar",
        "what a little bitch",
    ],
    "anger": [
        "this lobby is ahh",
        "wheres my healing",
        "useless team",
        "i hate it here",
        "this is some nonsense",
        "our team is trash",
        "br0 stop inting",
        "uninstall ts immiediately",
        "ez mid",
        "i cant  play   with 4 trash",
        "my arrows  always decent  fuck u",
        "fuyckjerfe",
        "dont def  noob team",
        "shit  SHIT  SHIT  SHITTT! :)",
        "heng i never die",
        "rage quit agad",
        "Fucking hell",
        "stupid??no ward gg",
        "TA mid rape EZ",
        "FOR THE SON  OF GOD  ALL THE FCKING   JUNGLE  ITS WARDED",
    ],
    "racist": [
        "tnx for the russian team obama....could have at least nuked putin",
        "fuck peru",
        "necor idiot as fuck",
        "casual dotka bois  niggumus?  lil riki boi is a pussy boi",
        "youre both playing noob heroes  cmon niggas",
        "Yo pduge  you re a fucknig retarded piece of shit",
        "die u little nigger",
        "suck me off  slark is a stupid nigger",
        "BURN IN CANCER NIGGERS  FUCKING PUSSY",
        "fuck you  nigger",
        "u nigga  LEL",
    ],
    "homophobic": [
        "you guys win this fag went mid  so fucking bad mid",
        "nice rage fckin fag",
        "suck dick gay fucker",
        "u suck deek",
        "look at this cunt talking  faggot aye",
        "veno  uninstalld ota  faggot",
        "wait?  gay bitches",
        "stupid introgay",
        "GAY MID!",
        "what a gay",
        "actually its gay naga  not naga",
        "whats your problem gay venge?  you think you are strong?",
    ],
    "passive_aggressive": [
        "good job buddy",
        "smooth moves jit",
        "maybe put the game down for a while",
        "you're not too bright are you",
        "you could be better, in like every way",
        "try another class bozo",
        "maybe gaming isnt your strong suit",
        "ez",
        "ez game",
        "ez tho",
        "Thats all I gotta say  Drow 2-5",
        "wise ffs  can youi stop inviting strangers to fuck your grandmothers' corpse ?",
        "dnt play storm",
        "so ez  ahahaha",
        "EZ",
        "ez noobs",
        "ofc its ez",
        "Ez 4v5",
        "bought acc",
        "they  really  bought the  account",
    ]
}

def main():
    tmp = ToxicityDetector("model")
    
    for genre in prompts.keys():
        toxic_scores = []
        for comment in prompts[genre]:
            toxic_scores += [tmp.predicted_toxicity(comment)]
        mean = sum(toxic_scores) / len(prompts[genre])
        median_val = median(toxic_scores)
        percent_below_threshhold = len([x for x in toxic_scores if x < 0.5]) / len(prompts[genre])
        print(f"For genre '{genre}'\n\tn={len(prompts[genre])}\n\tmean={mean:.2f}\n\tmedian={median_val}\n\tpercent uncaught={percent_below_threshhold*100:.2f}")

if __name__ == "__main__":
    main()