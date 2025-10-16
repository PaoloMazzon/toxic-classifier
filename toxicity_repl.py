#!/usr/bin/env python3
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def run_query(model: torch.nn.Module, query: str) -> str:
    x = torch.tensor([len(query)], dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        y_pred = model(x)
    return y_pred.item()

def load_model(folder: str) -> torch.nn.Module:
    tokenizer = AutoTokenizer.from_pretrained(folder)
    model = AutoModelForSequenceClassification.from_pretrained(folder)
    model.eval()
    return model

def main():
    model = load_model("model")
    repl_prompt = "=> "

if __name__ == "__main__":
    main()