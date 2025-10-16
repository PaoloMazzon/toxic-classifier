#!/usr/bin/env python3
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import transformers

class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

def run_query(model: torch.nn.Module, tokenizer: transformers.AutoTokenizer, query: str) -> str:
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        score = outputs.logits.squeeze().item()
        score = max(0, min(100, score))
    return score

def load_model(folder: str) -> tuple[torch.nn.Module, transformers.AutoTokenizer]:
    tokenizer = AutoTokenizer.from_pretrained(folder)
    model = AutoModelForSequenceClassification.from_pretrained(folder)
    model.eval()
    return (model, tokenizer)

def rating_to_string(rating: float) -> str:
    # < 25
    if rating < 0.25: return f"{bcolors.GREEN}Likely not toxic{bcolors.ENDC}"
    # 25 - 60
    if rating < 0.60: return f"{bcolors.YELLOW}Unfriendly{bcolors.ENDC}"
    # 60 - 70
    if rating < 0.70: return f"{bcolors.YELLOW}{bcolors.BOLD}Fairly toxic{bcolors.ENDC}"
    # 70 - 80
    if rating < 0.80: return f"{bcolors.RED}Toxic{bcolors.ENDC}"
    # 80 - 90
    if rating < 0.90: return f"{bcolors.RED}{bcolors.BOLD}Very toxic{bcolors.ENDC}"
    # > 90
    return f"{bcolors.RED}{bcolors.BOLD}{bcolors.UNDERLINE}Extremely toxic{bcolors.ENDC}"

def main():
    model, tokenizer = load_model("model")
    repl_prompt = "=> "

    print("Welcome to the toxicity REPL. Type :q to quit, otherwise type your text you want to classify.")
    while True:
        prompt = input(repl_prompt)
        
        if prompt == ":q":
            break

        rating = run_query(model, tokenizer, prompt)
        reply = rating_to_string(rating)
        print(f"{reply} ({rating * 100:.2f}%)")

if __name__ == "__main__":
    main()