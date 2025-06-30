import spacy
import json
import os
from spacy.matcher import Matcher

def save_model_with_patterns(nlp, patterns, save_dir):
    """
    Save the spaCy model along with matcher patterns.
    """
    # Save the spaCy model
    nlp.to_disk(save_dir)
    
    # Save matcher patterns as a JSON file
    patterns_file = os.path.join(save_dir, "matcher_patterns.json")
    with open(patterns_file, "w") as f:
        json.dump(patterns, f)

    print(f"Model and patterns saved at: {save_dir}")

# Dictionary to store patterns with labels
medical_patterns = {
    "DISEASE": [
    # Your original entries
    [{"LOWER": "covid"}, {"LOWER": "19"}],
    [{"LOWER": "diabetes"}],
    [{"LOWER": "cancer"}],
    [{"LOWER": "hypertension"}],
    [{"LOWER": "pneumonia"}],
    [{"LOWER": "asthma"}],
    [{"LOWER": "flu"}],
    [{"LOWER": "tuberculosis"}],
    
],
    "BODY_PART": [
    [{"LOWER": "lungs"}],
    [{"LOWER": "kidney"}],
    [{"LOWER": "brain"}],
    [{"LOWER": "liver"}],
    [{"LOWER": "stomach"}],
    
]
}

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Save the model and patterns
save_model_with_patterns(nlp, medical_patterns, "saved_model_with_patterns")

# python -m spacy download en_core_web_sm
