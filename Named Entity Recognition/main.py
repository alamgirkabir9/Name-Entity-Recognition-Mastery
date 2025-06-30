import spacy
import json
from spacy.matcher import Matcher
import os

def load_model_with_patterns(load_dir):
    """
    Load the spaCy model and matcher patterns together.
    """
    # Load the spaCy model
    nlp = spacy.load(load_dir)
    
    # Load matcher patterns from the saved file
    patterns_file = os.path.join(load_dir, "matcher_patterns.json")
    with open(patterns_file, "r") as f:
        medical_patterns = json.load(f)
    
    # Initialize the matcher and add the patterns
    matcher = Matcher(nlp.vocab)
    for label, patterns in medical_patterns.items():
        for pattern in patterns:
            matcher.add(label, [pattern])
    
    print("Model and patterns loaded successfully.")
    
    return nlp, matcher

# Load the saved model and patterns
nlp, matcher = load_model_with_patterns("")

# Test the matcher on a new text
doc = nlp("The patient has diabetes and takes Metformin. They had an MRI scan for a brain tumor.")
matches = matcher(doc)

# Print matches with labels
for match_id, start, end in matches:
    label = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(f"Keyword: {span.text}, Label: {label}")
