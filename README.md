# Text-to-Image Context Management: ICF, RCF, and SCRM Algorithms

This repository contains the implementation of the **Initial Context First (ICF)**, **Region Context First (RCF)**, and **Structured Context Retention Methods (SCRM)** algorithms, integrated into a Django web service. These algorithms are designed to manage text contexts in generative AI models for text-to-image conversion tasks.

## About

We understand the importance of transparency in research and the need to provide access to code and datasets to ensure replicability of the experimental results. However, due to the **commercial nature** of our project, some proprietary elements are not included in this public repository to protect our intellectual property.

While we cannot provide access to certain internal components such as our full dataset and the generative AI model itself, this repository contains the core algorithms that demonstrate how context management works in our text-to-image pipeline. 

For a more comprehensive experience, including the real-world use case of our algorithms, you can try our **beta version** of the commercial service at [hear](https://bit.ly/3XBfAF4).

## Project Overview

This project includes:

- **ICF Algorithm**: Adds the context of the first sentence to all subsequent sentences.
- **RCF Algorithm**: Rotates context between sentences based on a defined threshold (`delta`).
- **SCRM Algorithm**: Handles structured contexts and transitions between them using Word2Vec embeddings.
- A simple **Django REST API** to call these algorithms through HTTP requests.
  
## API Endpoints

### ICF Algorithm API

- **URL**: `/myapp/icf/`
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

- **URL**: `/myapp/rcf/`
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

- **URL**: `/myapp/scrm/`
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

3. **Download the Pre-trained Word2Vec Model**:
    The **GoogleNews-vectors-negative300.bin** model is used in the SCRM algorithm for context similarity. Due to the size of the file (approximately 1.5 GB), it cannot be included in this repository. You will need to download it manually.

    You can download the model from [GoogleNews-vectors-negative300](https://code.google.com/archive/p/word2vec/) and save it in your project directory.

    ```bash
    wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
    gunzip GoogleNews-vectors-negative300.bin.gz
    ```

4. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

## Requirements

This project requires the following Python packages, as specified in the `requirements.txt`:

```text
asgiref==3.8.1
backports.zoneinfo==0.2.1
Django==4.2
gensim==4.3.3
joblib==1.4.2
numpy==1.24.4
scikit-learn==1.3.2
scipy==1.10.1
smart-open==7.0.4
threadpoolctl==3.5.0
wrapt==1.16.0
```

## Comparison of the generated images for each Algorithms

1. **ICF Algorithm**:
    - ![fig11](https://github.com/user-attachments/assets/5944f9fe-8e67-43db-b965-3b05bdce465f)
2. **RCF Algorithm**:
    - ![fig12](https://github.com/user-attachments/assets/4237fc18-9822-4b20-aed4-d6492810852b)
3. **SCRM Algorithm**:
   ```bash
   Once, there was a hungry lion.
   The lion hunted animals every day, and the animals were terrified of him.
   One day, the animals devised a plan to stop the lion.
   They decided to send a clever rabbit to meet the lion.
   The rabbit walked very slowly towards the lion, taking his time.
   When the lion saw the rabbit arriving late, he became furious.
   The rabbit came up with an excuse to explain the delay, claiming another lion had tried to attack him.
   The lion became even angrier and demanded to be shown this supposed rival.
   The clever rabbit led the lion to a deep well.
   When the lion looked into the well, he saw his reflection in the water.
   Mistaking his reflection for another lion, he leaped into the well to fight.
   But the lion fell into the well and drowned.
   Thanks to the clever rabbit, the animals were saved.
    ```
    - For the above Scenario, comparison of the generated images for each Alorithms (RCF, SCRM, DALL-E) is as follow:   
        - **RCF Algorithm**:
            - ![rcf](https://github.com/user-attachments/assets/29c02349-30b0-4503-89cf-3f6223ad8809)
        - **SCRM Algorithm**:
            - ![scrm](https://github.com/user-attachments/assets/5071be67-5836-4ed4-981e-f7e2a951265f)
        - **DALL-E Algorithm**:
            - ![dall-e-min](https://github.com/user-attachments/assets/0417aecd-a983-409d-96cb-f98a0717825e)

