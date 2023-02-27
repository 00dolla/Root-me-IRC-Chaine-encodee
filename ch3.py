import socket
import string
import time
import math
import base64
import zlib

SERVER = 'server_name'
PORT = 6667 
NICKNAME = 'bot_name'
CHANNEL = 'channel_name'


def main():
    global IRC
    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IRC.connect((SERVER, PORT))
    Listener()
    IRC.close()


def send_data(command):
    IRC.send(bytes(command + '\n', 'UTF-8'))


def joinchan(chan):
    send_data('JOIN ' + chan)
    ircmsg = ""
    while ircmsg.find("is now your displayed host") == -1:
        ircmsg = IRC.recv(2048).decode("UTF-8")
        # DEBUG # print(ircmsg)


def rot13(phrase):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in phrase)


def Listener():
    send_data("USER " + NICKNAME + " " + NICKNAME + " " + NICKNAME + " " + NICKNAME)
    send_data('NICK ' + NICKNAME)
    joinchan(CHANNEL)
    send_data('PRIVMSG candy !ep3')
    while (1):
        ircmsg = IRC.recv(2048).decode("UTF-8")
        # DEBUG # print(ircmsg)
        data = ircmsg.split(':')[2]
        decoded = rot13(data)
        IRC.send(bytes("PRIVMSG candy !ep3 -rep %s" % decoded + '\n', 'UTF-8'))
        ircmsg = IRC.recv(2048).decode("UTF-8")
        print('Password: %s' % ircmsg.split('password ')[1])


main()