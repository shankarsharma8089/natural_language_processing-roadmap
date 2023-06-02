### Stemming
#It is a process of reducing infected words to their word stem.
#for example if words are History and Historical the stem of these words will be Histori.
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

#converting to sentence
sentence = nltk.sent_tokenize(paragraph)
#initilizing porterstemmer lib and creating a obj of the named stemmer
stemmer = PorterStemmer()

#stemming 
for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    words = [stemmer.stem(word)for word in words if word not in set(stopwords.words('english'))]
    sentence[i] = ' '.join(words)
    print(sentence)

### Code description

#First we are importing **nltk** lib and from nltk we are importing **PorterStemmer** and **stopwords.**
#Stopwords** lib : It helps to remove words that are either repeating or does not put any value.
#stopwords.words(”english”)**in the parentheses we can change the language for which you want to find the stopwords for ex: you can write french, german if the text are in these languages.

## In for loop

#1st line**: for stemming we are using loop on all the range of length of sentence.

#2nd line**: for each sentence we will do a word tokenize which will convert all the sentence to words .
#(sentence[i])** in the loop it will take the first sentence and it will convert into words using **word_tokenize** and so on.
#”words”** variable is a list of words from each and every sentence.

#-3rd line: we write a for loop saying **for(word in words)** which means for each and every word we are going to iterate and then give a condition that  **if word not in set(stopwords.words(’english’)**this means if the word is present in the stopwords list then we are not going to take that word, if it is not present we will take that and apply stemming on that  **stemmer.stem(word).**
#-Set is used as it helps to take the unique stopwords in the english language.
#And finally join them to sentence.
    
##Lemmatization
#-It is similar to stemming but the only difference is it converts the word and give a meaningful word which can be understood by human
#-for example: if the words are History and Historical ,the lemmatized word will be History
#-for some words stemming may not give a meaningful representation but lemmatization is focused on giving a meaningful representation

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

#converting to sentence
sentence = nltk.sent_tokenize(paragraph)
#initilizing porterstemmer lib and creating a obj of the named stemmer
lemmatizer = WordNetLemmatizer()

#stemming 
for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    words = [lemmatizer.stem(word)for word in words if word not in set(stopwords.words('english'))]
    sentence[i] = ' '.join(words)
    print(sentence)
