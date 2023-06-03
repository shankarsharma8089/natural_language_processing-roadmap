#To prepare input data to pass it to  models(RNNs, LSTM ,or LLMs) we do it by Converting text data in to numbers or vectors 
 
#To do so we can perform:
#1) Interger encoding 
#2)Embeddings 
 
#Integer enoding :
#step1 : create a vocablary of unique words 
#step2 : provide a index to the text and pelace these sentence with their index value 
#step3 : perform padding, if yyou have sent having different size padding helps to solve it ,

#        [text]                [providing index]        [padding]
#ex:    hey there                [1,2]                   [1,2,0]
#     what are you doing         [3,4,5]                 [3,4,5]

import numpy as np
doc = ["Kanye West is an American rapper, singer, and songwriter.",
       "He was born on February 22, 1977, in Brooklyn, New York.",
       "Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events.",
       "He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others.",
       "Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience.",
       "He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.",
       "Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."]

from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(oov_token='no' ) #oov = out of vocablary token , if their new text  added in traininig data it will get replaced with 'no'
tokenizer.fit_on_texts(doc)
print(tokenizer.word_index) #assigning index to your words 
print(tokenizer.word_counts) #finding the word count (frequeny)
print(tokenizer.document_count) # finding the number of sentences(rows) in your text data 

#creating seq for every sentence 
sequences = tokenizer.texts_to_sequences(doc)
print(sequences)

#As the seq size is different in every sentences we perform padding 
from keras.utils import pad_sequences
sequences = pad_sequences(sequences,padding='post')
print(sequences)
