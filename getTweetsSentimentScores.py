import json

WORDSENTIMENTSFILEPATH = "wordSentimentScores.txt"
TWITTERSTREAMFILEPATH = "twitterStream.txt"


def readSentimentWordsScore(wordSentimentsFile):
    wordScores = {} 

    for line in wordSentimentsFile:
        term, score  = line.split("\t")  
        wordScores[term] = int(score)  

    return wordScores


def getTweetsSentimentScores(twitterStreamFile, wordScores):
    
    tweetsScores = []

    for line in twitterStreamFile:
        l = json.loads(line)

        if "text" in l:
            tweet = l["text"]

            tweetScore = 0
            
            tweetStringWords =  tweet.encode('ascii','ignore').split(" ")
        
            for word in tweetStringWords:
                if word in wordScores:
                    tweetScore += wordScores[word]

            print tweetScore
            tweetsScores.append(tweetScore)

    return tweetsScores


if __name__ == '__main__':
    wordSentimentsFile = open(WORDSENTIMENTSFILEPATH, "r")
    twitterStreamFile = open(TWITTERSTREAMFILEPATH, "r")

    wordScores = readSentimentWordsScore(wordSentimentsFile)
    tweetsScores = getTweetsSentimentScores(twitterStreamFile, wordScores)
