import json
import operator

TWITTERSTREAMFILEPATH = "twitterStream.txt"


def getTopTenHashtags(twitterStreamFile):
    
    hashtagsDict = {}
    totalHashtags = 0

    for line in twitterStreamFile:
        l = json.loads(line)

        if "entities" in l:
            
            if "hashtags" in l["entities"]:
                hashtags = l["entities"]["hashtags"]

                for ht in hashtags:
                    ht = ht["text"]
                    
                    if ht not in hashtagsDict:
                        hashtagsDict[ht] = 0

                    hashtagsDict[ht] += 1
                    totalHashtags += 1

    topTenHashtags = sorted(hashtagsDict.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]

    return topTenHashtags


if __name__ == '__main__':
    
    twitterStreamFile = open(TWITTERSTREAMFILEPATH)

    topTenHashtags = getTopTenHashtags(twitterStreamFile)

    for ht in topTenHashtags:
        print ht[0].encode('utf-8') + " " + str(ht[1])
