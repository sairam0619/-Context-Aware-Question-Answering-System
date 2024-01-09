# -Context-Aware-Question-Answering-System

This repository contains a simple Question Answering (QA) web application using Flask and Hugging Face Transformers. The application utilizes the DistilBERT model for question answering.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Context-Aware-Question-Answering-System allows users to input a document and a question, and the application responds with the relevant answer. It uses the DistilBERT model from Hugging Face Transformers to perform the question answering task.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Flask
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Context-Aware-Question-Answering-System.git
   cd  Context-Aware-Question-Answering-System
Install the required dependencies:
pip install -r requirements.txt

Run the Flask web application:
python app.py

Open your web browser and go to http://localhost:5000.

Input a document and a question in the provided form and click "Get Answer" to see the response.

## Structure
acuscore.py: Evaluation script using F1 score.
app.py: Flask web application for the Question Answering interface.
qa_module.py: Module for question answering functionality with DistilBERT.
model_evaluation.py: Example usage of the evaluation script on a labeled dataset.
index.html: HTML template for the web application.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please follow the Contributing Guidelines.
## output 

![Screenshot 2024-01-09 211855](https://github.com/sairam0619/-Context-Aware-Question-Answering-System/assets/104977246/53ee3c81-3b74-4cc5-a127-149685a4e567)
![Screenshot 2024-01-09 211733](https://github.com/sairam0619/-Context-Aware-Question-Answering-System/assets/104977246/dc6afeb0-5fe9-4e45-8f01-36a90094f060)
