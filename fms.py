import tweepy
import sqlite3, atexit
import credentials

SCREEN_NAME='frcfms'

class _Database:
	def __init__(self):
		self._db=sqlite3.connect('tweets.sqlite')
	def insert(self, tweet_id, created_at, text):
		# TODO also parse the tweets?
		try:
			self._db.execute("INSERT INTO raw_tweets VALUES (?, ?, ?);", 
					(str(tweet_id), created_at.isoformat(), text))
		except sqlite3.IntegrityError: # Tweet already inserted
			# TODO should we handle this another way?
			# (Perhaps check if the data is the same)
			pass
	
	def commit(self):
		self._db.commit()
	
	def close(self):
		self.commit()
		self._db.close()

db = _Database()

@atexit.register
# We can't register this on _Database because @atexit doesn't pass in self
def _close_db():
	db.close()

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Get the User ID from the FMS's screen name
USER_ID = api.get_user(screen_name=SCREEN_NAME).id

