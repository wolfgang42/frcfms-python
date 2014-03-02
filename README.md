Retrieve data from the [@frcfms](http://twitter.com/frcfms) twitter feed.
See it in action at [http://www.linestarve.com/frc/fms](http://www.linestarve.com/frc/fms).
Pull requests welcome!

## Configuration ##

You will need to get a Twitter API account, and set up a credentials.py file like so:

    CONSUMER_KEY="##KEY##"
	CONSUMER_SECRET="##SECRET##"
	ACCESS_TOKEN="##TOKEN##"
	ACCESS_TOKEN_SECRET="##TOKENSECRET##"

You will also need to create a `tweets.sqlite` file with `sqlite3 tweets.sqlite < create_tweets.sql`

## Usage ##
`listener.py` is designed to run constantly and update the database when a tweet arrives, using the Twitter stream API.
`periodic_get.py` should be run occasionally, to get any updates the listener may have missed. It takes an argument,
one of `required` or `optional` which tells it whether it needs to update or can skip the update if an update didn't
happen last time it checked. This allows it to update more frequently when matches are actually going on, and less
when nothing is happening. The recommended schedule is `required` once an hour, and `optional` every fifteen minutes.
