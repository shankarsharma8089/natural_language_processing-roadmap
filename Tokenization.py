#In tokenization we take a paragraph or a corpse and convert it into sentence or words

### 1.1)Tokenizing sentence:
#sent_tokenize is a function inside NLTK which takes the para and convert them into different sentence
import nltk
nltk.download('punkt')

paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

sentence = nltk.sent_tokenize(paragraph)
print(sentence)

### 1.2)Tokenizing words*

#As we have above converted a corpse into a sentence now we will convert it into words
#word_tokenize is a function inside NLTK  which takes the para and convert them into words

word = nltk.word_tokenize(paragraph)
print(word)
