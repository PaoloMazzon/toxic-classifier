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
        "eat shit"
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
    ],
    "racist": [
        ""
    ],
    "homophobic": [
        ""
    ],
    "passive_aggressive": [
        "good job buddy",
        "smooth moves jit",
        "maybe put the game down for a while",
        "you're not too bright are you",
        "you could be better, in like every way",
        "try another class bozo",
        "maybe gaming isnt your strong suit",
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
        print(f"For genre '{genre}', mean={mean:.2f} median={median_val} percent uncaught={percent_below_threshhold*100:.2f}")

if __name__ == "__main__":
    main()