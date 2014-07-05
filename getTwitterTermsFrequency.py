import json

TWITTERSTREAMFILEPATH = "twitterStream.txt"


def getTermsFrequency(twitterStreamFile):
    
    termsFrequencies = {}
    total = 0

    for line in twitterStreamFile:
        l = json.loads(line)

        if "text" in l:
            tweet = l["text"]
            tweetStringWords =  tweet.encode('ascii','ignore')
            tweetStringWords = tweetStringWords.replace('\n', '').split(" ")

            for word in tweetStringWords:
                if word not in termsFrequencies:
                    termsFrequencies[word] = 0
                
                termsFrequencies[word] += 1
                total += 1

    for term in termsFrequencies.items():
        print term[0] + " " + str(float(term[1])/float(total))
        term[1] = float(term[1])/float(total)

    return termsFrequencies


if __name__ == '__main__':
    
    twitterStreamFile = open(TWITTERSTREAMFILEPATH)

    termsFrequencies = getTermsFrequency(twitterStreamFile)


