import socket

def connect(ip):
	try:
		socket.setdefaulttimeout(2)
		conn = socket.socket()
		conn.connect((ip, 5252))

		#Recieve Challenge message
		p = conn.recv(65)
		print str(p) + "\n"


		#Recieve secret key
		p = conn.recv(66)
		dList = caesarDecode(p[:-1])
		print dList
		for line in dList:
			print line + '\n'

		#Send secret key to server
		secret = 'Peanut'
		conn.sendall(secret)

		#Recieve and decode 5 encoded messages
		for i in range(0,5):
			encodedMsg = conn.recv(1024)
			decodedMsg = getQuote(str(encodedMsg))
			print str(i)

			conn.sendall(decodedMsg + '\n')

		#All I do is Win
		print str(conn.recv(1024)) + "\n"

		win = generateShellCode()
		print win
		conn.sendall(win)

		conn.close()
		print "done"
	except:
		print 'failed'

# Overwrite python server file, rewrite winner.sh
# Might need to download another file from internet because of byte recieve limits
def generateShellCode():
	return "bishop; cat /tmp/elite_hacker.txt"

def getQuote(encodedMsg):
	decodedMsgList = []
	decodedMsgList = caesarDecode(str(encodedMsg)[:-1])

	for msg in decodedMsgList:
		if checkQuote(str(msg)):
			return msg
	return None

def checkQuote(quote):
	X=[]
	X.append("Here's looking at you, kid.")
	X.append("I love the smell of napalm in the morning.")
	X.append("Rosebud")
	X.append("You're gonna need a bigger boat.")
	X.append("Gentlemen, you can't fight in here! This is the War Room!")
	X.append("Listen to them. Children of the night. What music they make.")
	X.append("Attica! Attica!")
	X.append("Nobody puts Baby in a corner.")
	X.append("Plastics")
	X.append("One morning I shot an elephant in my pajamas. How he got in my pajamas, I don't know.")
	X.append("A boy's best friend is his mother.")

	if str(quote) in X:
		print "true\n"
		return True
	else:
		return False 
	
def caesarDecode(msg):
	decodeList = []

	for i in range(1,26):
		decoded = []
		for x in msg:
			if(ord(x) - i < 33):
				decoded.append(chr(ord(x) - i + 92))
			else:
				decoded.append(chr(ord(x) - i))
			
		decodeList.append(''.join(decoded).replace("|", " "))

	return decodeList

if __name__ == "__main__":
    HOST, PORT = "localhost", 5252

    connect(HOST)
