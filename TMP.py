import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import transformers
import numpy as np
import re

class ToxicityDetector:
    # Sample blacklist, this is not an effective blacklist
    BLACKLIST = [
        "dumb",
        "leet",
        "tosser",
        "unc",
        "vro",
        "dumbahh",
        "ahh",
        "ligma",
        "fuck",
        "shit",
        "piss",
        "ass",
        "asshole",
        "dick",
        "bitch",
        "cunt",
        "kys",
    ]

    def __init__(self, model_folder: str):
        self.model, self.tokenizer = self.__load_model(model_folder)

    def predicted_toxicity(self, query: str) -> float:
        model_prediction = self.__run_query(query)
        blacklist_prediction = self.__highest_similarity(query)
        return max(blacklist_prediction, model_prediction)

    def __run_query(self, query: str) -> float:
        inputs = self.tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=256)
        with torch.no_grad():
            outputs = self.model(**inputs)
            score = outputs.logits.squeeze().item()
            score = max(0, min(100, score))
        return score

    # Returns the highest similarity between the word and something in the blacklist
    def __highest_similarity(self, query: str) -> float:
        highest = 0
        for word in re.split(r"[_\s]+", query):
            for black_word in self.BLACKLIST:
                sim = self.__word_similarity(black_word, word)
                highest = max(sim, highest)
        return highest

    # Returns similarity between two words, accounting for intentional obfuscation
    def __word_similarity(self, word1: str, word2: str) -> float:
        def normalize_char(c):
            c = c.lower()
            return {
            '3': 'e', '@': 'a', '4': 'a', '1': 'l',
            '!': 'i', '0': 'o', '$': 's', '7': 't', '5': 's'
            }.get(c, c)

        def normalize(word):
            return ''.join(normalize_char(c) for c in word if c.isalnum())

        a = normalize(word1)
        b = normalize(word2)

        if not a:
            return 1.0 if not b else 0.0
        if not b:
            return 0.0

        # Ensure a is the shorter string
        if len(a) > len(b):
            a, b = b, a

        len1 = len(a)
        len2 = len(b)

        prev = np.arange(len1 + 1)
        curr = np.zeros(len1 + 1, dtype=int)

        for j in range(1, len2 + 1):
            curr[0] = j
            for i in range(1, len1 + 1):
                cost = 0 if a[i - 1] == b[j - 1] else 1
                curr[i] = min(curr[i - 1] + 1,
                            prev[i] + 1,
                            prev[i - 1] + cost)
            prev, curr = curr, prev

        dist = prev[len1]
        max_len = max(len1, len2)
        return 1.0 - dist / max_len

    def __load_model(self, folder: str) -> tuple[torch.nn.Module, transformers.AutoTokenizer]:
        tokenizer = AutoTokenizer.from_pretrained(folder)
        model = AutoModelForSequenceClassification.from_pretrained(folder)
        model.eval()
        return (model, tokenizer)
