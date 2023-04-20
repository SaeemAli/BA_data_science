from textblob import TextBlob
import pandas as pd

def linearSearch(array, x):

    # Going through array sequencially
    for i in range(0, len(array)):
        if (array[i] == x):
            return i
    return -1

def findPolar(df, heading):
    uniqueVal = df[heading].unique()
    polarity = [0 for i in range(len(uniqueVal))]
    count = [0 for i in range(len(uniqueVal))]

    for i in range(len(df)):
        x = linearSearch(uniqueVal, df.loc[i, heading])
        if x != -1:
            text = TextBlob(df.loc[i, "reviews"])
            s = text.sentiment
            polarity[x] += s.polarity
            count[x] += 1

    for j in range(len(polarity)):
        print(uniqueVal[j], ": " , polarity[j]/count[j])
        data["Category"].append(uniqueVal[j])
        data["Sentiment"].append(polarity[j]/count[j])


data = {"Category": [], 
        "Sentiment":[]}

df = pd.read_csv("data/BA_reviews.csv")
findPolar(df, "Recommend")
findPolar(df, "Type of Traveler")
findPolar(df, "Seat Type")
result = pd.DataFrame(data)
result.to_csv("data/sentiment.csv")