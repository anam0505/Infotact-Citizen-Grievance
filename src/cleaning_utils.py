import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from config import CUSTOM_STOPWORDS

nltk.download("stopwords")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
stop_words.update(CUSTOM_STOPWORDS)

def clean_text(text):
    """
    Cleans grievance text:
    - lowercase
    - remove URLs
    - remove emails
    - remove phone numbers
    - remove HTML
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