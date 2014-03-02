import fms
import tweepy
import json, dateutil.parser
from pprint import pprint

class FmsListener(tweepy.streaming.StreamListener):
	def on_data(self, dstr):
		data=json.loads(dstr)
		try:
			# We have to check this because filter(follow=[@frcfms]) also gives
			# mentions etc. Grr!
			if data['user']['screen_name'] == 'frcfms':
				if data['truncated']:
					print "E: Truncated!"
				fms.db.insert(data['id'],
						dateutil.parser.parse(data['created_at']), data['text'])
				fms.db.commit()
		except ValueError:
			# Aack kafck.... this data doesn't make sense!
			# Print it out and let our owner sort out the mess.
			pprint(data)
			
		return True
	
	def on_error(self, error):
		print error
		return True

# Start listening to the stream
tweepy.Stream(fms.auth, FmsListener()).filter(follow=[fms.USER_ID])
