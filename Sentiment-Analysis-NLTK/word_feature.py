import nltk
def get_word_features(weets):
    all_words = []
    for (words, sentiment) in weets:
        all_words.extend(words)
    print (wordlist)
    wordlist = nltk.FreqDist(all_words)
    word_features = []
    for feature in wordlist:
        if wordlist[feature] > 10000:
            word_features.append(feature)
    print (word_features)
    print(len(word_features))
        #return word_features
weets=['hello','pos']
get_word_features(weets)

