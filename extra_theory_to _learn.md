
| RULE-BASED NLP | STATISTICAL NLP |
| --- | --- |
|    PROS |                 PROS   |
| -Easy to debug | -easy to scale  |
| -Does not require much training  | -learn by itself |
| -understand language | -Fast development |
|     CONS |                 CONS |
| slow parsing | -difficult to debug |
| -moderate coverage | -no understanding  |
| require skill developer | -require large data |


## Components of NLP 


![components of nlp](https://github.com/shankarsharma8089/natural_language_processing-roadmap/assets/126678340/e8ab6bf5-f0e2-48e8-afbf-c2812defa012)

-Ambiguity: The quality of being open to more than one interpretation; inexactness.

ONE HOT VECTOR:
-One bit ‘1’ and all other ‘0’

VECTOR LENGHT:
-Number of words in language

## Steps for making a BOW :

—>Collect data: 

-for example the data is: 
 i am the best of all time

 i am the worst of all time

 i am the coolest of all people

 i am the cringest man on earth

##### -NOTE: Treat each line as a separate “document”

#### —>Design Vocabulary:

-make the list of unique words (ignoring case and punctuation)

-i, am, the , best , of , all, time, worst , coolest , people, cringest , man , on , earth

-this vocabulary has 14 words from the corpus containing 28 words.

#### —>Create a document vector:

-the objective here is to convert free text into vector

-A scoring method has to be taken to mark the presence of words as a boolean value,0 for absent, 1 for present

-converting first line into binary vector:

i=1

am=1 

the=1 

best=1 

of=1 

all=1 

time=1 

worst=0 

coolest=0 

people=0

cringest=0 

man=0

on=0 

earth=0

and for the other document

i am the worst of all time=[1 1 1 0 1 1 1 1 0 0 0 0 0 0]

i am the coolest of all people=[1 1 1 0 1 1 0 0 1 1 0 0 0 0]

and so on,

**—>Managing Vocabulary:**

-As the vocabulary size increases so does the vector representation of documents

-This results in a vector with lots of zeros scores which is called as sparse vector or sparse representation.

-Sparse vectors require more memory and computational resources when modelling.

#### To decrease the size of the vocabulary there are cleaning techniques**

—>Ignoring punctuation

—>Ignoring frequent words that does not contain much information

—>Fixing misspelled words

—>Reducing words to their stem

## CBOW(Continuous Bag of Word)
-In this algorithm we predict the target word from the context

##WORKING:
###Step1:At start we encode each word as one hot vector 
###Step2:Iterating over the sentence to do so we select a window size
    
   -we need to select a window size for iterating our sentence.

   -Let consider it to be 3 for this example.

   -Liverpool FC are a football team      

   -The window size is marked with red background

-In CBOW we try to predict the center word from the context word
-As the number size is 3 and the center word is the word we need to predict using the 2 word surrounding it, to do this we use a simple NN(Neural Network)
-Here we will put ‘Liverpool’ and ‘are’ as input to NN to find the middle word ‘FC’.

![WhatsApp Image 2022-09-02 at 9 23 20 AM](https://github.com/shankarsharma8089/natural_language_processing-roadmap/assets/126678340/5611c966-5d12-45e4-a3ca-6eddd69d7725)

## SKIP-GRAM

-Here we predict the context word from the target.

### WORKING:

-We choose the window size and give the center word as input trying to predict the context words.

-The weights are updated in a similar way as CBOW


![WhatsApp Image 2022-09-02 at 9 23 20 AM (1)](https://github.com/shankarsharma8089/natural_language_processing-roadmap/assets/126678340/4c2c255a-b4c4-4be0-b00b-e035ab2a815b)


