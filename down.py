import urllib2
import os

if not os.path.isfile('words.txt'):
	print 'need to download words.txt ! Please wait as the file is of 12 mb'
	response = urllib2.urlopen('http://m.uploadedit.com/ba3s/148007135258.txt')
	html = response.read()
	f=open('words.txt', 'w')
	f.write(html)
	f.close()
else: 
	print 'file found'