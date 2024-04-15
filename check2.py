import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')  # Download the required data for tokenization
nltk.download('stopwords')  # Download stopwords

# Function to preprocess and tokenize code
def preprocess_and_tokenize(code):
    lines = code.split('\n')  # Tokenize into lines of code
    tokens = []
    for line in lines:
        # Split each line into words (you can customize this part further)
        words = word_tokenize(line)
        tokens.extend(words)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    return set(tokens)  # Convert tokens to a set to ensure uniqueness

# Function to calculate Jaccard similarity between two sets of words
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return (intersection / union) * 100  # Convert to percentage

# Function to read and preprocess code from a file
def read_and_preprocess_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as code_file:
            code = code_file.read()
        return preprocess_and_tokenize(code)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# User-input folder path containing code files
folder_path = input("Enter the path to the folder containing code files: ")

# Dictionary to store similarity results
similarity_results = {}

# Loop through files in the folder and compare with each other
for file_name1 in os.listdir(folder_path):
    file_path1 = os.path.join(folder_path, file_name1)
    tokens1 = read_and_preprocess_code(file_path1)
    
    if tokens1 is not None:
        for file_name2 in os.listdir(folder_path):
            file_path2 = os.path.join(folder_path, file_name2)
            tokens2 = read_and_preprocess_code(file_path2)
            
            if tokens2 is not None and file_name1 != file_name2:
                similarity = jaccard_similarity(tokens1, tokens2)
                similarity_results[(file_name1, file_name2)] = similarity

# Print similarity results
for (file1, file2), similarity in similarity_results.items():
    print(f"Similarity between {file1} and {file2}: {similarity:.2f}%")
