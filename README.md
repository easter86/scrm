# Text-to-Image Context Management: ICF, RCF, and SCRM Algorithms

This repository contains the implementation of the **Initial Context First (ICF)**, **Region Context First (RCF)**, and **Structured Context Retention Methods (SCRM)** algorithms, integrated into a Django web service. These algorithms are designed to manage text contexts in generative AI models for text-to-image conversion tasks.

## About

We understand the importance of transparency in research and the need to provide access to code and datasets to ensure replicability of the experimental results. However, due to the **commercial nature** of our project, some proprietary elements are not included in this public repository to protect our intellectual property.

While we cannot provide access to certain internal components such as our full dataset and the generative AI model itself, this repository contains the core algorithms that demonstrate how context management works in our text-to-image pipeline. 

For a more comprehensive experience, including the real-world use case of our algorithms, you can try our **beta version** of the commercial service at [https://beta.maccai.kr](https://beta.maccai.kr).

## Project Overview

This project includes:

- **ICF Algorithm**: Adds the context of the first sentence to all subsequent sentences.
- **RCF Algorithm**: Rotates context between sentences based on a defined threshold (`delta`).
- **SCRM Algorithm**: Handles structured contexts and transitions between them using Word2Vec embeddings.
- A simple **Django REST API** to call these algorithms through HTTP requests.

## API Endpoints

### ICF Algorithm API

- **URL**: `/api/icf/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
      "sentences": [
        "Sentence 1.",
        "Sentence 2.",
        "Sentence 3."
      ]
    }
    ```
- **Response**:
    ```json
    {
      "processed_sentences": [
        "Sentence 1 with context.",
        "Sentence 2 with context.",
        "Sentence 3 with context."
      ]
    }
    ```

### RCF Algorithm API

- **URL**: `/api/rcf/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
      "sentences": [
        "Sentence 1.",
        "Sentence 2.",
        "Sentence 3."
      ],
      "delta": 2
    }
    ```
- **Response**:
    ```json
    {
      "processed_sentences": [
        "Sentence 1 with rotated context.",
        "Sentence 2 with rotated context.",
        "Sentence 3 with rotated context."
      ]
    }
    ```

### SCRM Algorithm API

- **URL**: `/api/scrm/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
      "sentences": [
        "Sentence 1.",
        "Sentence 2.",
        "Sentence 3."
      ],
      "delta": 0.8
    }
    ```
- **Response**:
    ```json
    {
      "processed_sentences": [
        "Sentence 1 with structured context.",
        "Sentence 2 with structured context.",
        "Sentence 3 with structured context."
      ]
    }
    ```

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the dependencies**:
    Ensure you have Python 3.x installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

## Requirements

This project requires the following Python packages, as specified in the `requirements.txt`:

```text
Django==4.2
djangorestframework==3
