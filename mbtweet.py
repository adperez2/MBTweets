import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Monterey Bay"
limit = 3000
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content,tweet.likeCount])

df = pd.DataFrame(tweets,columns=["Date", "Username", "Tweet", "LikeCount"])
print(df)

df.to_csv("mbtweet.csv")