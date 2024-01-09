# qa_module.py

from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

def initialize_qa_model():
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-cased-distilled-squad')
    model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-cased-distilled-squad')
    return tokenizer, model

def extract_and_respond_qa(document, question, tokenizer, model):
    inputs = tokenizer(question, document, return_tensors='pt')
    outputs = model(**inputs)
    start_idx = torch.argmax(outputs['start_logits'])
    end_idx = torch.argmax(outputs['end_logits']) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx]))
    return answer
