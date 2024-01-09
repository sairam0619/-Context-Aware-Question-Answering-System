# acuscore.py

from sklearn.metrics import f1_score
from tqdm import tqdm

def evaluate_model(extraction_function, dataset):
    predicted_answers = []
    ground_truth_answers = []

    for data_point in tqdm(dataset, desc="Evaluating"):
        document = data_point["document"]
        question = data_point["question"]
        ground_truth_answer = data_point["answer"]

        predicted_answer = extraction_function(document, question)
        predicted_answers.append(predicted_answer)
        ground_truth_answers.append(ground_truth_answer)

    f1 = f1_score(ground_truth_answers, predicted_answers, average='micro')

    return f1
