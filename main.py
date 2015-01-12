import sys, getpass

import requests
from bs4 import BeautifulSoup

base = sys.argv[1]

if not base.endswith("/"):
	base += "/"

while True:
	credentials = {
		"login": raw_input("Username: "),
		"password": getpass.getpass("Password: ")
	}

	login = requests.post(base + "login/login", data=credentials, allow_redirects=False)

	if login.status_code != 303:
		print "Incorrect credentials"
	else:
		session = login.cookies
		break

print session