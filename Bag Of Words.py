#-Is is a way of extracting feature from text for use in modelling.
#-It describe the occurrence of words within a document.
#-It involves 2 things:
#—>A vocabulary of known words
#—>A measure of presence of known words

#-In this approach we look at the histogram of words within the text , considering each word count as a feature.
#-It is called as “Bag” because any information about the order or structure of words in the documents is discarded.
#-The model is concerned with whether known words occur in the document ,not where in the document.
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

wordnet = WordNetLemmatizer()
sentence = nltk.sent_tokenize(paragraph)
corpus=[]
for i in range (len(sentence)):
    paragraph = re.sub('[^a-zA-Z]',' ',sentence[i])
    paragraph = paragraph.lower()
    paragraph = paragraph.split()
    paragraph = [wordnet.lemmatize(word)for word in paragraph if not word in set(stopwords.words('english'))]
    paragraph = ' '.join(paragraph)
    corpus.append(paragraph)
    
    #creating a BOW model 
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    print(corpus)
    print(X)
    
    
### Code description:
#-corpus=[] , after cleaning all the text we will store all the sentence in corpus.
#-re.sub(’[^a-zA-Z]’),sub is a method which will replace all the character other than a-z and A-Z with spaces and sentence[i] means apply this sub method to each and every sentence.
#-^=not symbol.
#-.lower(),here we are lowering each and every sentence.
#-.split(),here we are going to do split, while doing split we will get a list of words so the variable “paragraph” will have a list of words.
#-The next line of code says if the word is not in the stopwords then do lemmatization.
#-Finally we will join all the list of words paragraph into paragraph.
#-Then we are appending to the list we have created which is called as corpus.
#-Bow model, here we are using sklearn lib and importing lib called CountVectorizer which creates histogram or the BOW documents matrix.
#-Then we create an object for this lib.
#-Fit transform creates an matrix and .array() convert corpus to array.


#simple code to understand the creation of dict of words and their occurance in BOW
sent1 = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events." 
sent2 = "kanye has released several successful albums, including 808s & Heartbreak,The Life of Pablo among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. "
sent3 = "He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

BOW1 = sent1.split(' ')
BOW2 = sent2.split(' ')
BOW3 = sent3.split(' ')
print(BOW1)
print(BOW2)
print(BOW3)
uniqewords = set(BOW1).union(set(BOW2)).union(set(BOW3))
#print(uniqewords)

#creating a dict of words and their occurace for each doc in the corpus (collection of documents)
num_of_words_in_BOW1 = dict.fromkeys(uniqewords,0)
for word in BOW1:
    num_of_words_in_BOW1[word] +=1

num_of_words_in_BOW2 = dict.fromkeys(uniqewords,0)
for word in BOW2:
    num_of_words_in_BOW1[word] +=1    
    
num_of_words_in_BOW3 = dict.fromkeys(uniqewords,0)
for word in BOW3:
    num_of_words_in_BOW1[word] +=1  


print(num_of_words_in_BOW1)
print(num_of_words_in_BOW2)
print(num_of_words_in_BOW3)

    
