# app.py

from flask import Flask, render_template, request
from qa_module import initialize_qa_model, extract_and_respond_qa

app = Flask(__name__)
tokenizer, model = initialize_qa_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    if request.method == 'POST':
        document = request.form['document']
        question = request.form['question']
        response = extract_and_respond_qa(document, question, tokenizer, model)
        return render_template('index.html', document=document, question=question, response=response)

if __name__ == '__main__':
    app.run(debug=True)
