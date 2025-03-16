# 🌟 Import Required Libraries
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# ✅ Uncomment these lines if running for the first time to download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')s

# ----------------------------------
# 🌟 Step 1: Preprocessing Function
# ----------------------------------

def preprocess(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    # Lowercase the text
    text = text.lower()

    # Tokenize words
    words = word_tokenize(text)

    # Remove punctuation and keep only alphabetic words
    words = [word for word in words if word.isalpha()]

    # Remove stopwords like 'is', 'the', 'what'
    words = [word for word in words if word not in stop_words]

    # Lemmatize words (reduce to base form)
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words back to string
    return ' '.join(words)

# -----------------------------------
# 🌟 Step 2: Load Dataset and Preprocess
# -----------------------------------

# Load the Vastu question-answer dataset
data = pd.read_csv("vastu_questions_answers.csv")

# Preprocess each question in the dataset
data['Processed_Question'] = data['Question'].apply(preprocess)

# (Optional) Save processed data for future use
data.to_csv('vasthu_preprocessed.csv', index=False)

# -----------------------------------
# 🌟 Step 3: Vectorize Dataset Questions
# -----------------------------------

# Create TF-IDF Vectorizer and fit on processed questions
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Processed_Question'])

# -----------------------------------
# 🌟 Step 4: Chatbot Loop to Handle User Queries
# -----------------------------------

print("Welcome to Vastu Chatbot! Ask me anything about Vastu (Type 'exit' to quit)")

while True:
    # Take user input
    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Thank you! Have a great day! 😊")
        break

    # ✅ Preprocess User Input
    input_processed = preprocess(user_input)

    # Vectorize user input
    input_vector = vectorizer.transform([input_processed])

    # Calculate cosine similarity with dataset questions
    cosine_similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()

    # Find best match index and score
    best_match_index = cosine_similarities.argmax()
    best_match_score = cosine_similarities[best_match_index]

    # --------------------------
    # 🌟 Step 5: Respond with Answer or Ask to Rephrase
    # --------------------------

    # Threshold for confidence (adjustable)
    threshold = 0.2

    if best_match_score > threshold:
        # If confident, show matched question and answer
        print("\nChatbot:")
        print("Q:", data.loc[best_match_index, 'Question'])
        print("A:", data.loc[best_match_index, 'Answer'])
        print("Confidence Score:", round(best_match_score, 2))
    else:
        # If not confident, apologize and ask to rephrase
        print("\nChatbot: Sorry, I couldn't understand your question. Please try asking in another way.")

