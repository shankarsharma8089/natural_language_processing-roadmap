#-Problem with scoring words frequency is that highly frequent words start to dominate in the document but may not be useful to the model.
#-TF-iDF is used to rescale the frequency of words by how often they appear in all document, so that the score for frequent words like “the” that are frequent across all document are penalized.
#-Term Frequency: it is a scoring of frequency of the word in the current document.
#-Inverse Document Frequency:it is a scoring of how rare the word is across document.IDF of a rare term is high and IDF of a frequent term is likely to be low.

import re
from sklearn.feature_extraction.text import TfidfVectorizer



paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

text = re.sub(r'[^\w\s]', '', paragraph).lower()
words = text.split()
print(words)
# create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
# transform the words into a TF-IDF matrix
tfidf = vectorizer.fit_transform(words)
# print the TF-IDF matrix
print(tfidf)
print(words)
 
    




























    

    