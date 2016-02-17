import socket

#The key is fozzy bear
def solve(string):
    tokenizedString = string.split()

    key = {'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'thirteen':13,
        '0n3':1,
        'tw0':2,
        'thr33':3,
        'f0ur':4,
        'f1v3':5,
        's1x':6,
        's3v3n':7,
        '8ght':8,
        'n1ne':9,
        't3n':10,
        'Yo-Leven':11,
        'twelves':12,
        '13teen':13,}

    if tokenizedString[1] == "+":
        if tokenizedString[3] == "+":
            return key[tokenizedString[0]] + key[tokenizedString[2]] + key[tokenizedString[4]]
        else:
            return key[tokenizedString[0]] + key[tokenizedString[2]] - key[tokenizedString[4]]
    else:
        if tokenizedString[3] == "-":
            return key[tokenizedString[0]] - key[tokenizedString[2]] - key[tokenizedString[4]]
        else:
            return key[tokenizedString[0]] - key[tokenizedString[2]] + key[tokenizedString[4]]
            

def connect(HOST,PORT):
    try:
        #connect to server
        socket.setdefaulttimeout(2)
        conn = socket.socket()
        conn.connect((HOST, PORT))
        print "Connection Established\n"

        #Send the correct password
        password = "Coffee is For Closers"
        print str(conn.recv(1024))
        print str(conn.recv(1024)) + "\n"
        conn.sendall(password)

        #Start Loop
        i = 0
        while i < 50:
            i = i +1
            
            problem = str(conn.recv(1024))
            print problem
            answer = solve(problem)
            print answer
            conn.sendall(str(answer) + "\n")
        print str(i) + " Questions Answered\n"

        #Input Handle
        print str(conn.recv(1024))
        conn.sendall("Bishop\n")
        print str(conn.recv(1024))


    except:
        print "failed"

def connectElite(HOST,PORT):
    try:
        #connect to server
        socket.setdefaulttimeout(2)
        conn = socket.socket()
        conn.connect((HOST, PORT))
        print "Connection Established\n"

        #Send the correct password
        password = "Coffee is For Closers"
        print str(conn.recv(1024))
        print str(conn.recv(1024)) + "\n"
        conn.sendall(password)

        #Get Key
        print str(conn.recv(1024))
        specialString = str('a' * 128)
        conn.sendall(specialString)
        print str(conn.recv(1024))



    except:
        print "Failed elite challenge"


if __name__ == "__main__":
    HOST, PORT = "localhost", 2600

    connect(HOST, PORT)
    connectElite(HOST,PORT)
