#-In word2vec, each word is represented as a vector of 32 or more dimension instead of a signal number

###-WHY WORD2VEC
#—>Preserve relationship b/w words
#—>Deals with addition of new words in the vocabulary.
#—>Better result in lot of DL application

### HOW ARE RELATIONSHIP FORMED
#-Word2vec tries to make the word with similar context have similar embeddings.
#-For example : The kid said he would be a footballer.
#               The child said he would be a footballer.
#-In above example Kid and Child are different word with same context, so Word2Vec tries to make words with similar context have similar vector.
#-Word2Vec generates this vector from words by using 2 algorithm:
#—>Continuous Bag of Word (CBOW)——— to spell as see bow
#—>Skip Gram

import re
import gensim
import nltk
from nltk.corpus import stopwords
from gensim.test.utils import common_texts
from gensim.models import Word2Vec


paragraph = "Kanye West is an American rapper, singer, and songwriter. He was born on February 22, 1977, in Brooklyn, New York. Kanye is known for his unique style of music, which often features a catchy melody and lyrics that are often inspired by pop culture and current events. He has released several successful albums, including 808s & Heartbreak,The Life of Pabloand West Side Story, among others. Kanye is also known for his social media presence,Kanye is known for his powerful message and his ability to connect with his audience. He has often used his music to inspire others and has made a positive impact on people's lives. His message of love and acceptance has inspired countless artists and musicians around the world.Overall, Kanye West is a multi-faceted artist who has made a significant impact on the music industry and the world of entertainment. His success and popularity have inspired countless artists and musicians around the world."

#pre-processing the data
text = re.sub(r'\[[0-9]*\)',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentence = nltk.sent_tokenize(text)
sentence = [nltk.word_tokenize(sentence)for sentence in sentence]
for i in range(len(sentence)):
    sentence[i] = [word for word in sentence[i] if word not in stopwords.words('english')]
    
#initializing the model
model = Word2Vec(sentence , vector_size=100 , window=5 , min_count=1 , workers=4)
model.save('word2vec.model')

#get numpy vector of a word in your corpus 
vector = model.wv['kanye']
print(vector)

#get similar words
similiar = model.wv.most_similar('lyrics',topn=5)
print(similiar)
    
