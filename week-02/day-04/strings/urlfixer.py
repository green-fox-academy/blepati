
# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!

urlBad= "https//www.reddit.com/r/nevertellmethebots"

url = urlBad[0:4] + urlBad[4] + ":" + urlBad[5:-4] + "odds"

print(url)
