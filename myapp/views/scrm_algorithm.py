from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from myapp.views.extract_context import extract_context

# Load pre-trained Word2Vec model (Google News)
# You can download the model using gensim's API if you don't have it locally
# Make sure to use the correct path to the model
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)


def scrm_algorithm(sentences, delta):
    """
    This function processes sentences to identify context similarity and handle context transitions.
    Args:
    - sentences: A list of input sentences
    - delta: The threshold for context similarity
    """

    n = len(sentences)
    S_input = sentences[:]  # Copy of input sentences
    S_cxt = []  # List to store sentence contexts
    W_cxt = []  # List to store extracted context words
    cxtIndex = 1  # Initialize context index

    # Step 1: Process each sentence to extract context using Word2Vec embeddings
    for i in range(n):
        # Separate sentences into unit sentences (this might involve tokenization or NLP processing)
        sentence_context = extract_context(sentences[i])  # Extract words as context
        S_cxt.append(sentence_context)
        W_cxt.append(sentence_context)

    # Step 2: Compare context similarity and handle transitions using Word2Vec embeddings
    for i in range(n - 1):  # Compare each sentence with the next
        similarity = calculate_similarity(W_cxt[i], W_cxt[i + 1], model)  # Calculate similarity using Word2Vec

        if similarity > delta:
            # Add current context to the sentence if similarity exceeds threshold
            S_cxt[i] += W_cxt[cxtIndex - 1]  # Add context to the current sentence
            S_input[i] = S_cxt[i]  # Reconstruct the input sentence with added context
        else:
            # Update context index and add new context for the next sentence
            cxtIndex = i + 1
            S_cxt[i] += W_cxt[cxtIndex - 1]  # Add the new context to the sentence
            S_input[i] = S_cxt[i]  # Reconstruct the input sentence with added context

    # Step 3: Return the processed input ready for generative AI
    return S_input


def calculate_similarity(context1, context2, model):
    """
    Calculate cosine similarity between two contexts using Word2Vec embeddings.
    Args:
    - context1: List of words (tokens) from the first sentence
    - context2: List of words (tokens) from the second sentence
    - model: Pre-trained Word2Vec model
    """

    # Get the Word2Vec embeddings for the words in context1 and context2
    vector1 = sentence_to_vector(context1, model)
    vector2 = sentence_to_vector(context2, model)

    # Calculate cosine similarity between the two sentence vectors
    if vector1 is not None and vector2 is not None:
        similarity = cosine_similarity([vector1], [vector2])[0][0]
    else:
        similarity = 0  # If no vectors are found, assume no similarity

    return similarity


def sentence_to_vector(sentence, model):
    """
    Convert a sentence into a single vector by averaging the Word2Vec vectors of the words in the sentence.
    Args:
    - sentence: List of words (tokens)
    - model: Pre-trained Word2Vec model
    """
    vectors = []

    for word in sentence:
        if word in model.key_to_index:
            vectors.append(model[word])  # Get Word2Vec vector for the word

    if len(vectors) > 0:
        # Average the word vectors to get a sentence vector
        return np.mean(vectors, axis=0)
    else:
        return None  # Return None if no word vectors were found
