import time
import tweepy

auth = tweepy.OAuthHandler('wD9pT4YS3LT2rx8gB4J3A2oOR', 'XpWidG2zDITP2mkPZwfWXuF6MbgA3hsgzXozm54C4GynFqEvYT')
#auth.set_access_token('	33310738-NKfIGpJ878L13A82yRgYuAkItkQshOFcLotzsMPuU', 'sAnYF29jhGgHu9g30l3KWmUUZtDz7DoJGkrHaI7rcRsaA')

api = tweepy.API(auth)

ids = [
]for page in tweepy.Cursor(api.friends_ids, screen_name="chelseawa1ks").pages():
    ids.extend(page)
    time.sleep(60)

print ids