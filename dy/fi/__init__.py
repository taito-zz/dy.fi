import urllib2

ip = urllib2.urlopen('http://ipcheck.ieserver.net').read()

conf_path = '{}/conf.txt'.format('/'.join(__file__.split('/')[:-1]))
