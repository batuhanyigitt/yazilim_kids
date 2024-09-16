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
    University of The Adam Mickiewicz University in Poznań announces a competition 
    for applications for mobility of first- and second-cycle students 
    under bilateral agreements in the summer semester 2023/24, 
    financed by the Erasmus+ Educational Mobility program with partner countries. 20 people will receive funding!
    Each person participating in mobility qualified for the mobility will receive funding from 
    the University in the form of individual support (scholarship) in the amount of EUR 700 per month to cover the costs of the stay.
    Each person participating in mobility qualified for the trip will receive an additional lump sum for 
    travel costs depending on the distance they must cover from the place of departure to the place of mobility.E-mail applications requesting funding can be submitted from September 15 to October 15, 2023 to the following address: bilateral@amu.edu.pl
    ATTENTION! This period applies to all applicants and depends in part
    on the deadlines for nominations to partner universities.
    These were established by partner universities and result from their internal spring semester dates. 
    You must follow them to be able to go on exchange.
    EXAMPLE No. 1: I am applying to a university in the USA (Appalachian State University),
    where the deadline for nomination from Adam Mickiewicz University is September 28 this year. 
    I must submit the required documents by e-mail (application, cover letter, Learning Agreement + optional language certificate or, 
    if applicable, approval from the supervisor of the bachelor's/master's thesis) to the UAM coordinator by September 28, 2023.
    EXAMPLE No. 2: I am applying to a university in Japan (Tokyo University of Foreign Studies), 
    where the deadline for nomination from Adam Mickiewicz University is November 8 this year. 
    I must submit the required documents by e-mail (application, cover letter, Learning Agreement + optional language certificate or, 
    if applicable, approval from the supervisor of the bachelor's/master's thesis) to the UAM coordinator by October 15, 2023.
    Please remember to meet all recruitment requirements for the exchange program at the partner university, 
    as well as meet the nomination deadline (the deadline by which the partner university accepts the application for studies from the UAM coordinator). 
    The rules for participating in the exchange program and the list of required documents can be found here.
    The trip must be completed by July 31, 2024.
    The minimum period of stay at the partner university is 2 months.
    List of eligible partner countries and universities along with the nomination deadlines that must be met by AMU (2023).
    """
    
summary = generate_summary(input_text)
print("SUMMARY: ")
print(summary)
   
   
   
   
   
    
    
# Define a function to generate a summary
def generate_summary(text, num_sentences=5):
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

if __name__ == "__main__":
    input_text = """
    University of The Adam Mickiewicz University in Poznań announces a competition 
    for applications for mobility of first- and second-cycle students 
    under bilateral agreements in the summer semester 2023/24, 
    financed by the Erasmus+ Educational Mobility program with partner countries. 20 people will receive funding!
    Each person participating in mobility qualified for the mobility will receive funding from 
    the University in the form of individual support (scholarship) in the amount of EUR 700 per month to cover the costs of the stay.
    Each person participating in mobility qualified for the trip will receive an additional lump sum for 
    travel costs depending on the distance they must cover from the place of departure to the place of mobility.E-mail applications requesting funding can be submitted from September 15 to October 15, 2023 to the following address: bilateral@amu.edu.pl
    ATTENTION! This period applies to all applicants and depends in part
    on the deadlines for nominations to partner universities.
    These were established by partner universities and result from their internal spring semester dates. 
    You must follow them to be able to go on exchange.
    EXAMPLE No. 1: I am applying to a university in the USA (Appalachian State University),
    where the deadline for nomination from Adam Mickiewicz University is September 28 this year. 
    I must submit the required documents by e-mail (application, cover letter, Learning Agreement + optional language certificate or, 
    if applicable, approval from the supervisor of the bachelor's/master's thesis) to the UAM coordinator by September 28, 2023.
    EXAMPLE No. 2: I am applying to a university in Japan (Tokyo University of Foreign Studies), 
    where the deadline for nomination from Adam Mickiewicz University is November 8 this year. 
    I must submit the required documents by e-mail (application, cover letter, Learning Agreement + optional language certificate or, 
    if applicable, approval from the supervisor of the bachelor's/master's thesis) to the UAM coordinator by October 15, 2023.
    Please remember to meet all recruitment requirements for the exchange program at the partner university, 
    as well as meet the nomination deadline (the deadline by which the partner university accepts the application for studies from the UAM coordinator). 
    The rules for participating in the exchange program and the list of required documents can be found here.
    The trip must be completed by July 31, 2024.
    The minimum period of stay at the partner university is 2 months.
    List of eligible partner countries and universities along with the nomination deadlines that must be met by AMU (2023).
    """

    summary = generate_summary(input_text)
    print("Summary:")
    print(summary)






import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.cluster.util import cosine_distance
import numpy as np 
import networkx as np

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_tokens = [word_tokenize(sentence.lower()) for sentence in sentences]
    filtered_sentence = [[word for word in tokens if word.isalnum() and word not in stop_words] for tokens in word_tokens]
    return filtered_sentence
    
def sentence_similarity(sent1, sent2):
    vector1 = [0] * len(unique_words)
    vector2 = [0] * len(unique_words)
    
    for word in sent1: 
        vector1[unique_words.index(word)] += 1
        
    for word in sent2:
        vector2[unique_word.index(word)] += 1
        
def build_similarity_matrix(sentences, threshold=0.0):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] - sentence_similarity(sentences[i], sentences[j])
            
    for i in range(len(sentences)):
        if sum(similarity_matrix[i]) == 0:
            continue
        similarity_matrix[i] /= sum(similarity_matrix[i])
        
    return similarity_matrix
