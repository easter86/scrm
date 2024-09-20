from myapp.views.extract_context import extract_context


def rcf_algorithm(sentences, delta):
    """
    Processes sentences using the RCF method. Depending on the sentence index,
    the context is rotated using the modulus of delta.
    Args:
    - sentences: A list of input sentences
    - delta: Threshold for changing context
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

    # Step 2: Apply the RCF context modification logic
    for i in range(n):
        if n > delta:
            # Rotate context using modulus with delta
            S_cxt[i] += W_cxt[i % delta]
        else:
            # Add context from the first sentence
            S_cxt[i] += W_cxt[0]

        S_input[i] = S_cxt[i]  # Reconstruct the input sentence with added context

    # Return processed sentences
    return S_input
