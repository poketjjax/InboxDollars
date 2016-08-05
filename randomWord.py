import urllib2

def getRandomWord():
	return urllib2.urlopen("http://randomword.setgetgo.com/get.php").read()
