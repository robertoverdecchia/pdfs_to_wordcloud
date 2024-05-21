import os
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def create_wordcloud(directory, exclude_words, img_width, img_height, important_words, capitalized_words, unimportant_words):
    text = ""
    lemmatizer = WordNetLemmatizer()

    # Read all PDFs in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            with open(os.path.join(directory, filename), 'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                for page_num in range(len(pdfReader.pages)):
                    pageObj = pdfReader.pages[page_num]
                    text += pageObj.extract_text()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = word_tokenize(text)

    # Convert all words to lower case and lemmatize them
    words = [lemmatizer.lemmatize(word.lower()) for word in words]

    # Remove numbers, words with no semantic meaning, words ending with "ed", and single character words
    words = [word for word in words if word.isalpha() and word not in exclude_words and not word.endswith('ed') and len(word) > 1]

    # Count the frequency of each word
    word_freq = Counter(words)

    # Increase the frequency of important words
    for word in important_words:
        if word in word_freq:
            word_freq[word] *= 2  # Increase the frequency by a factor of 2

    # Decrease the frequency of unimportant words
    for word in unimportant_words:
        if word in word_freq:
            word_freq[word] //= 2  # Decrease the frequency by a factor of 2

    # Capitalize specific words
    for word in capitalized_words:
        if word.lower() in word_freq:
            word_freq[word] = word_freq.pop(word.lower())

    # Create and configure the wordcloud
    wordcloud = WordCloud(width = img_width, height = img_height,
                          background_color ='white',
                          stopwords = exclude_words,
                          min_font_size = 10,
                          color_func=lambda *args, **kwargs: "black",
                          font_path='/System/Library/Fonts/Times.ttc').generate_from_frequencies(word_freq)

    # Display the wordcloud
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    plt.show()

# Define the list of words to be excluded
exclude_words = set(stopwords.words('english'))

# Define list of words to be excluded
exclude_words.update(['b', 'per', 'et', 'two', 'conference', 'due', 'possible', 'provide', 'considered', 
                      'available', 'eg', 'et', 'may', 'via', 'table', 'lago', 'among', 'using', 'set',
                      'would', 'however', 'high', 'p', 'j', 'ii', 'described', 'international', 'also',
                      'ieee', 'review', 'often', 'reported', 'provided', 'open', 'phase', 'questions', 'fig',
                      'group', 'presented', 'online', 'vol', 'provided', 'level', 'ie', 'art', 'main',
                      'figure', 'see', 'related', 'projects', 'application', 'overall', 'required', 'according',
                      'de', 'al', 'selection', 'potential', 'iii', 'towards', 'security', 'namely', 'example',
                      'papers', 'paper', 'us', 'one', 'many', 'pp', 'rather', 'addition', 'consider',
                      'number', 'higher', 'scenario', 'systematic', 'tion', 'ones', 'answer', 'different',
                      'section', 'acm', 'hence', 'multiple', 'make', 'items', 'cases', 'con', 'additional',
                      'study', 'wa', 'could', 'le', 'adoption', 'question', 'mean', 'game', 'journal', 'ha', 'doe',
                      'work', 'use', 'point', 'within', 'instead', 'question', 'mean', 'game', 'journal', 'ha'])

# Convert all words in the set to lower case
exclude_words = set(word.lower() for word in exclude_words)

# Specify the width and height of the image
img_width = 1500
img_height = 600

# Define important words to be emphasized 
important_words = []

# Define the words to be capitalized
capitalized_words = []

# Define words to be given less importance
unimportant_words = [] 

# Call the function with the directory containing the PDFs
create_wordcloud('folder/with/pdfs', exclude_words, img_width, img_height, important_words, capitalized_words, unimportant_words)
