import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once
nltk.download("stopwords")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """
    Clean complaint text:
    - lowercase
    - remove urls/emails/phone numbers/html
    - remove punctuation
    - remove stopwords
    - lemmatize words
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\d{10}", "", text)
    text = re.sub(r"<.*?>", "", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)