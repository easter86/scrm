from myapp.views.extract_context import extract_context


def icf_algorithm(sentences):
    """
    Processes sentences using the ICF method. The context of the first sentence is added to all sentences.
    Args:
    - sentences: A list of input sentences
    """

    n = len(sentences)
    S_input = sentences[:]  # Copy of input sentences
    S_cxt = []  # List to store sentence contexts
    W_cxt = []  # List to store extracted context words

    # Step 1: Process each sentence to extract context
    for i in range(n):
        # Separate sentences into unit sentences (this might involve tokenization or NLP processing)
        sentence_context = extract_context(sentences[i])
        S_cxt.append(sentence_context)
        W_cxt.append(sentence_context)

    # Step 2: Add context from the first sentence to all sentences
    for i in range(n):
        S_cxt[i] += W_cxt[0]  # Add context from the first sentence
        S_input[i] = S_cxt[i]  # Reconstruct the input sentence with added context

    # Return processed sentences
    return S_input
