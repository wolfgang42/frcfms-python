import sys
import fms

try:
	with open('since_id.txt', 'r') as f:
		since_id=int(f.readline())
		wasUpdated = (f.readline().strip() == 'True')
except IOError:
	# File doesn't exist
	since_id = 1
	wasUpdated = True

if sys.argv[1] == 'required' or wasUpdated:
	results = ['dummy']
	updated = False
	while len(results) != 0:
		results = fms.api.user_timeline(screen_name=fms.SCREEN_NAME, since_id=since_id, trim_user=True, count=200)
		for result in results:
			updated = True
			print result.id
			fms.db.insert(result.id, result.created_at, result.text)
			if result.id > since_id:
				since_id = result.id
	fms.db.commit()

	with open('since_id.txt', 'w') as f:
		f.write(str(since_id)+"\n")
		f.write(str(updated))
