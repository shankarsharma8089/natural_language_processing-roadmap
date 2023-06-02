##ONE HOT VECTOR:
#-One bit ‘1’ and all other ‘0’

##VECTOR LENGHT:
#-Number of words in language

### CBOW(Continuous Bag of Word)
#-In this algorithm we predict the target word from the context

##WORKING:
#Step1:At start we encode each word as one hot vector 
#Step2:Iterating over the sentence to do so we select a window size
    -we need to select a window size for iterating our sentence.

#     -Let consider it to be 3 for this example.

#    -Liverpool FC are a football team      

#     -The window size is marked with red background

#-In CBOW we try to predict the center word from the context word
#-As the number size is 3 and the center word is the word we need to predict using the 2 word surrounding it, to do this we use a simple NN(Neural Network)
#-Here we will put ‘Liverpool’ and ‘are’ as input to NN to find the middle word ‘FC’.

![WhatsApp Image 2022-09-02 at 9 23 20 AM](https://github.com/shankarsharma8089/natural_language_processing-roadmap/assets/126678340/5611c966-5d12-45e4-a3ca-6eddd69d7725)
