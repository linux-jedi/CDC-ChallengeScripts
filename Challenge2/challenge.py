#Embedded file name: ./128.py
import SocketServer
import sys
from random import randint
from thread import *
import commands
DEBUG = 0

class TitanTCP(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.
    
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    @staticmethod
    def caesar(message):
        encoded = []
        C = randint(1, 26)
        for x in message:
            if ord(x) + C > 125:
                encoded.append(chr(ord(x) + C - 92))
            else:
                encoded.append(chr(ord(x) + C))

        return ''.join(encoded)

    @staticmethod
    def itoString(I):
        english = {1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine',
         10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen'}
        leet = {1: '0n3',
         2: 'tw0',
         3: 'thr33',
         4: 'f0ur',
         5: 'f1v3',
         6: 's1x',
         7: 's3v3n',
         8: '8ght',
         9: 'n1ne',
         10: 't3n',
         11: 'Yo-Leven',
         12: 'twelves',
         13: '13teen'}
        if randint(1, 2) == 1:
            return leet.get(I)
        return english.get(I)

    @staticmethod
    def newProblem():
        answer = 0
        problem = ''
        C = randint(1, 13)
        D = randint(1, 13)
        E = randint(1, 13)
        first = randint(0, 1)
        second = randint(0, 1)
        if first == 0:
            answer = C + D
            problem = TitanTCP.itoString(C) + ' + ' + TitanTCP.itoString(D)
        else:
            answer = C - D
            problem = TitanTCP.itoString(C) + ' - ' + TitanTCP.itoString(D)
        if second == 0:
            answer = answer + E
            problem = problem + ' + ' + TitanTCP.itoString(E)
        else:
            answer = answer - E
            problem = problem + ' - ' + TitanTCP.itoString(E)
        if DEBUG:
            return ['One Plus One', 2]
        else:
            return [problem, answer]

    @staticmethod
    def elite():
        E = 'e'
        F = 'F'
        a = 'a'
        y = 'y'
        r = 'r'
        z = 'z'
        if 7 == 12:
            return 'The Key is: Red Herring'
        if 18 == 344:
            return 'The Key is: Blonde Squirrel'
        return "Feels good, don't it?\nThe Key is: " + F + 'o' + z + z + 'y B' + E + a + r + '\n'

    def handle(self):
        self.answer = ''
        self.handle = ''
        if DEBUG:
            self.request.settimeout(1200)
        else:
            self.request.settimeout(120)
        try:
            self.request.send('Welcome to TITAN 128 Challenge.\n')
            self.request.send('Program to complete, Hack 2 Learn')
            a3 = 'fee'
            a1 = 'Co'
            a2 = 'f'
            a4 = 'losers'
            self.request.send(TitanTCP.caesar('The Answer is: ' + a1 + a3[0] + a3 + ' is For ' + a1[0] + a4) + '\n')
            self.answer = self.request.recv(64).strip()
            if self.answer == a1 + a3[0] + a3 + ' is For ' + a1[0] + a4:
                z = 0
                if DEBUG:
                    kk = 2
                else:
                    kk = 50
                while z < kk:
                    z = z + 1
                    quote = ''
                    p, a = TitanTCP.newProblem()
                    self.request.send(p + '\n')
                    quote = self.request.recv(512)
                    if DEBUG:
                        print str(len(quote)) + '\n'
                    if len(quote) == 128:
                        self.request.send(TitanTCP.elite())
                        self.request.close()
                        return
                    if not quote[:-1] == str(a):
                        self.request.send('FAILED: Suck Less\n')
                        self.request.close()
                        return

                self.request.sendall('*** Completed Phase 1 ***\nWhat is your handle?\n')
                self.handle = self.request.recv(1024)
                print 'HANDLE: ' + self.handle[:-1] + ' : ' + str(hash(self.handle)) + '\n'
                p = self.handle + ' code is: ' + str(hash(self.handle)) + '\n'
                self.request.sendall(str(p))
                self.request.close()
            else:
                self.request.sendall('FAILED: Suck Less\n')
                self.request.close()
        except:
            self.request.sendall('FAILED: TOO SLOW\n')
            self.request.close()


if __name__ == '__main__':
    HOST, PORT = ('0.0.0.0', 2600)
    server = SocketServer.ThreadingTCPServer((HOST, PORT), TitanTCP)
    try:
        server.serve_forever()
    except:
        server.shutdown()
