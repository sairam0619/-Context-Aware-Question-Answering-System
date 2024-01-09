# model_evaluation.py

from acus import evaluate_model
from qa_module import extract_and_respond_qa

labeled_dataset = [
    {"document": "Hugging Face is a company that specializes in Natural Language Processing models.", "question": "What is Natural language", "answer": "Natural Language Processing models"},
]

f1_score_result = evaluate_model(extract_and_respond_qa, labeled_dataset)
print("F1 Score:", f1_score_result)
