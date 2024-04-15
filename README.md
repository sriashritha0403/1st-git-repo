# PLAG CHECK
PLAGIARISM DETECTING MODEL 

Executive Summary: 
The provided Python script aims to analyze the similarity between code files in a specified folder 
using the Jaccard similarity metric. The Jaccard similarity is computed based on the sets of pre
processed and tokenized words derived from the code files. The process involves tokenizing code 
into lines and then further into words, removing stop words, and calculating the Jaccard similarity 
between each pair of code files. 

Code Structure and Functions: 
1. Preprocessing and Tokenization: 
• The preprocess_and_tokenize function takes a code snippet as input, tokenizes it 
into lines, further tokenizes each line into words, and removes English stop words. 
The result is a set of unique tokens. 
2. Jaccard Similarity Calculation: 
• The jaccard_similarity function computes the Jaccard similarity between two sets of 
words using the formula: ∣A∩B∣∣A∪B∣×100∣A∪B∣∣A∩B∣×100. 
3. Reading and Preprocessing Code from a File: 
• The read_and_preprocess_code function reads a code file, catches potential errors, 
and returns the pre-processed and tokenized set of words. It handles 
FileNotFoundError and general exceptions. 
4. Main Script: 
• The script prompts the user for the path to a folder containing code files. 
• It iterates through the files in the specified folder, comparing each file with every 
other file (excluding self-comparisons). 
• For each pair of files, it calculates the Jaccard similarity and stores the results in a 
dictionary. 

Usage and Input: 
• Users are prompted to input the path to the folder containing code files. 
• The script then processes each file, calculating Jaccard similarity between pairs of code files. 
• Results are stored in a dictionary (similarity_results), mapping file pairs to their respective 

Jaccard similarity percentages. 
Output: 
• The script outputs the similarity results in the form of a printed report. 
• Each result includes the names of the compared files and the calculated Jaccard similarity 
percentage. 

Error Handling: 
• The script gracefully handles FileNotFoundError and other potential exceptions during file 
reading and processing. 
• If an error occurs, it prints an informative message indicating the issue. 

Recommendations and Customization: 
• Users can customize the tokenization process further according to specific requirements. 
• Consider additional preprocessing steps or adjustments to the stopwords list for improved 
relevance to the code analysis. 

Conclusion: 
The provided Python script offers a simple yet effective method for comparing the similarity between 
code files within a specified folder. The Jaccard similarity metric provides a quantitative measure of 
the overlap in unique tokens between code files, aiding in code analysis and similarity assessment. 
Note: Ensure that the required NLTK data is downloaded before running the script by using the 
nltk.download commands at the beginning of the script. 

Resources used: 
1. Geekforgeeks – for reference of the structure 
2. ChatGPT- to correct my errors in the code and for documentation purpose

