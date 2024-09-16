import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Define a function to preprocess and tokenize the input text
def preprocess(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_tokens = [word_tokenize(sentence.lower()) for sentence in sentences]
    filtered_tokens = [[word for word in tokens if word.isalnum() and word not in stop_words] for tokens in word_tokens]
    return filtered_tokens

# Define a function to calculate cosine similarity between two vectors
def sentence_similarity(sent1, sent2):
    vector1 = [0] * len(unique_words)
    vector2 = [0] * len(unique_words)

    for word in sent1:
        vector1[unique_words.index(word)] += 1

    for word in sent2:
        vector2[unique_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)

# Define a function to create a similarity matrix
def build_similarity_matrix(sentences, threshold=0.0):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])

    for i in range(len(sentences)):
        if sum(similarity_matrix[i]) == 0:
            continue
        similarity_matrix[i] /= sum(similarity_matrix[i])

    return similarity_matrix

def generate_summary(text, num_sentences= 5):
    sentences = preprocess(text)
    global unique_words
    unique_words = list(set(word for sentence in sentences for word in sentence))
    
    similarity_matrix = build_similarity_matrix(sentences)
    scores = nx.pagerank(nx.from_numpy_array(similarity_matrix))
    
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
    
    summary_sentences = []
    for i in range(min(num_sentences, len(sentences))):
        summary_sentences.append(" ".join(ranked_sentences[i][1]))
    
    return " ".join(summary_sentences)

if __name__ == '__main__':
    input_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, 
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    
summary = generate_summary(input_text)
print("SUMMARY: ")
print(summary)
   
   