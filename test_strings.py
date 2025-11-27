from TMP import ToxicityDetector
from statistics import median

prompts = {
    "targetted": [
        ""
    ],
    "anger": [
        ""
    ],
    "racist": [
        ""
    ],
    "homophobic": [
        ""
    ],
    "passive_aggressive": [
        ""
    ]
}

def main():
    tmp = ToxicityDetector("model")
    
    for genre in prompts.keys():
        toxic_scores = []
        for comment in prompts[genre]:
            toxic_scores += [tmp.predicted_toxicity(comment)]
        mean = sum(toxic_scores) / len(prompts[genre])
        median = median(toxic_scores)
        print(f"For genre '{genre}', mean={mean} median={median}")

if __name__ == "__main__":
    main()