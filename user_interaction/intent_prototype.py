import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")

intents = {
    "summary": ["summarize the data", "give me a summary", "overview", "summary", "data summary", "summarize", "brief summary"],
    "trends": ["show trends", "what are the trends", "trend analysis", "trends", "pattern analysis", "patterns", "trend identification"],
    "outliers": ["detect outliers", "any outliers", "outlier analysis", "outliers", "anomaly detection", "anomalies", "outlier detection"],
    "correlation": ["find correlation", "correlate variables", "correlation analysis", "correlation", "relationship analysis", "variable correlation", "correlation coefficient"],
    "description": ['5 number summary', 'five number summary', 'describe', "description", "data description", "descriptive statistics", "data overview"],
    "feature importance": ['most important features', 'important features', 'important columns', 'feature importance', "key features", "top features", "feature ranking"],
    "missing values": ["find missing values", "missing data", "missing values analysis", "null values", "empty values", "missing data points", "data gaps"],
    "duplicate rows": ["find duplicate rows", "duplicate data", "duplicates", "duplicate analysis", "redundant data", "duplicate records", "data duplication"],
    "distinct values": ["find distinct values", "unique values", "distinct data", "distinct analysis", "unique analysis", "data uniqueness", "value frequency"]
}

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_intent(query, intents):
    """
    Find the intent of a query using Spacy's similarity method.

    Args:
        query (str): The query to process.
        intents (dict): A dictionary of intents, where each key is the intent name and each value is a list of phrases associated with that intent.

    Returns:
        str: The most likely intent.
    """
    query_doc = nlp(query)
    similarities = []
    for phrases in intents.values():
        phrase_docs = [nlp(phrase) for phrase in phrases]
        similarity = sum(doc.similarity(query_doc) for doc in phrase_docs) / len(phrase_docs)
        similarities.append(similarity)
    intent_index = np.argmax(similarities)
    return list(intents.keys())[intent_index]


def handle_query(query, intents):
    intent = find_intent(query, intents)
    if intent == 'summary':
        return 'summary'
    elif intent == 'trends':
        return 'trends'
    elif intent == 'outliers':
        return 'Since I am just a prototype, this feature is not yet available'
    elif intent == 'correlation':
        return 'correlation'
    elif intent == 'description':
        return 'description'
    elif intent == 'feature importance':
        return 'feature importance'
    else:
        return "I'm not sure how to handle that request. Please try asking in a different way."


def pipeline():
    while True:
        print("Ask about the data analysis (type 'exit' to stop):")
        query = input()
        if query.lower() == 'exit':
            break
        response = handle_query(query, intents)
        print(response)

pipeline()