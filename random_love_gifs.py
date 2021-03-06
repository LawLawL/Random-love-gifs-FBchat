# -*- coding: UTF-8 -*-

from fbchat import Client, __version__
from fbchat.models import *
import datetime
import random
import time
import sys
import argparse
import getpass
import os
#------------------------checks for version
if int(__version__.split('.')[0]) <= 1:
    if int(__version__.split('.')[1]) <1:
        raise Exception('The version of the fbchat library is too old. This program requires version 1.1.1 at least.')

#------------------------Parsing arguments

parser = argparse.ArgumentParser()
parser.add_argument('-s','--start_time', action="store", dest="start_time", help="Starting time of the gif-sending period")
parser.add_argument('-p','--stop_time', action="store", dest="stop_time", help="Stoping time of the gif-sending period")
parser.add_argument('-P','--password', action="store", dest="password", help="Your facebook password")
parser.add_argument('-e','--email_address', action="store", dest="address", help="Your email address")
parser.add_argument('-d','--destination_user', action="store", dest="destination", help="The user ID of the person you want to send gifs to")
parser.add_argument('-a','--add_gif', action="store", dest="more_gif", help="Gifs you want to add")
parser.add_argument('-m','--message', action="store", dest="message", help="The message you want to send with the gif")
parser.add_argument('-n','--new_gif_list', action="store_true", dest="new_list", help="Use this switch if you don't want to use the pre-registered gif list")
parser.add_argument('-D','--delay', action="store",dest="delay",help="Determines the delay between each verification")
parser.add_argument('-A','--add_from_prompt', action="store_true", dest="prompt", help="Use this switch if you want to be prompted what gifs you want to add")
parser.add_argument('-f','--file', action="store",dest="file",help="Input file for gif list")


args = parser.parse_args()


#------------------------Writes gif database

more_gif = []

if args.more_gif:
    for i in args.more_gif.split(','):
#        print("i:",i)
        if i.split('.')[-1] != "gif":
            print("The url address for a gif you add must end with a \'.gif\', so \'" + i + "\' will not be added")
        else:
            more_gif.append(i)
			
if args.file:
    try:
        file = open(args.file, "rt",newline='')
    except Exception as e:
        raise e
    for i in file.read().splitlines():
#        print(i)
        if i.split('.')[-1] != "gif":
            print("The url address for a gif you add must end with a \'.gif\', so \'" + i + "\' from file \'" + args.file + "\' will not be added")
        else:
            more_gif.append(i)  
	 

if args.prompt:
    print("Please type the links of the gifs you want to add, one by one (enter one, then press Enter, then another one etc).\nType \"end\" when you're done.")
    link = ""
    while True:
        link = input(">")
        if link == "end":
            break
        if link.split('.')[-1] != "gif":
            print("The url address for a gif you add must end with a \'.gif\', so \'" + link + "\' will not be added")
        else:
            more_gif.append(link)

#print(more_gif)

if args.new_list:
    gifs = []
else: #default gif list
    gifs= ["https://media.tenor.co/images/564eac526a8af795c90ce5985904096e/tenor.gif",
       "https://media.tenor.co/images/5d5565fe47af258d83b4caa2a668ccfa/tenor.gif",
       "https://media.tenor.co/images/c3759877cdcb86e25a1d305d5ac6fe4d/tenor.gif",
       "https://media.tenor.co/images/56ea2b419cd997350fb2d03c11ac724b/tenor.gif",
       "https://media3.giphy.com/media/f6y4qvdxwEDx6/200_d.gif",
       "https://media.tenor.co/images/23e82dfb8dbe7ef24e9dc8b2412411db/tenor.gif",
       "https://media.tenor.co/images/f6f20cda181ac07db50be80cdc4fa0c8/tenor.gif",
       "https://media.tenor.co/images/7daf1a191e6afe50c3ecf1ff446f1d4f/tenor.gif",
       "https://media.tenor.co/images/98764169e6a3003fc1fcf1feba434724/tenor.gif",
       "https://media.tenor.co/images/cd6f8d04b7d0e05f2d2b8ee5457cc4ee/tenor.gif",
       "https://media.tenor.co/images/77d90206206963c6aa5b05a2aa5c8c06/tenor.gif",
       "https://media.tenor.co/images/9c4a6d3cb294d01177a5b1e1544a5b9b/tenor.gif"]

for i in more_gif:
    gifs.append(i)

#print(gifs)

while not args.address:
    args.address = input("Please enter your email adress:")

while not args.password:
    if any('SPYDER' in name for name in os.environ) or "pythonw.exe" in sys.executable:
        args.password = input("Please enter your password: ")
    else:
        args.password = getpass.getpass("Please enter your password: ")



#-----------------------------------------Printing friend list
try:
    client = Client(args.address, args.password)
except ConnectionError:
    print("Could not connect, please check your connection")
    os._exit(0)
except FBchatUserError:
    print("Wrong password/email combinaison")
    os._exit(0)

choice = ""
while choice.lower() != "y" and choice.lower() != "n":
    choice = input("Do you want to print your friends list, with their ID? (Press \'y\' if you're not sure) [y/n]:")

if choice.lower() == "y":
    def getKey(user):
        return user.name

    users = client.fetchAllUsers()
    print("Name\t\t\t\t| ID")
    for user in sorted(users,key=getKey): 
	    #next lines are just for formatting 
        a=4
        if len(user.name) > 6:
            a = 3
        if len(user.name) > 14:
            a = 2
        if len(user.name) > 22:
            a = 1
        if len(user.name) > 30:
            a = 0
        if user.uid != "0" and user.uid != 0:
            print(user.name,a*"\t",user.uid)
#-----------------------------------------------

while not args.destination:
    args.destination = input("Please enter the user ID of the person you want to send gifs to:")

while not args.start_time:
    args.start_time = input("Please specify at what hour should the program\033[92m start\033[00m being active (in a 24h format, like \'13:00\') >")

while not args.stop_time:
    args.stop_time = input("Please specify at what hour should the program\033[91m stop\033[00m being active >")

while not args.delay:
    args.delay = input("Please specify what should be the delay between two checks with the format hh:mm:ss >")

args.message = input("If you want to attach a message with your gif, please write it:")

#parsing start/stop time

time_start_hour = int(args.start_time.split(':')[0])
time_start_min = int(args.start_time.split(':')[1])
time_stop_hour = int(args.stop_time.split(':')[0])
time_stop_min = int(args.stop_time.split(':')[1])

delay_hour = int(args.delay.split(':')[0])
delay_min = int(args.delay.split(':')[1])
delay_sec = int(args.delay.split(':')[2])

#base = datetime.time(0,0)
delais = datetime.timedelta(hours=delay_hour, minutes=delay_min, seconds=delay_sec).seconds
#-----------------------------------------------
#just a useful function to print while using infinite while loops
def printf(text):
    sys.stdout.write(str(text)+"\n")
    sys.stdout.flush()

while True:
    printf("---------------------------New loop---------------------------")
    messages = client.fetchThreadMessages(thread_id=args.destination, limit=200) #fetches until 200 messages, just to be sure 
    for message in messages:
        if message.author == client.uid: #we automatically get the last message sent
            del messages
            break

    time_last_message = datetime.datetime.fromtimestamp(int(message.timestamp[:-3])) #converts the timestamp that the fbchat library returns, we chop off the last three digits because they're not recognize by the python function
    time_now = datetime.datetime.now()

	# display info
    printf("Last message: \"" + message.text + "\" @ " + str(time_last_message)) 
    printf("Current time: " + str(time_now.time()))
    printf("Difference: " + str((time_now-time_last_message).seconds) + " seconds")

    if time_now.time() > datetime.time(time_start_hour, time_start_min) and time_now.time() < datetime.time(time_stop_hour, time_stop_min): #if we're in the time range allowed

        if (time_now-time_last_message).seconds > delais: #if the last message is more than the defined delay, then we 
            index=random.randint(0,len(gifs)-1) # choose a random gif
            printf("\033[92m{}".format("Sending image #") + str(index) +"\033[00m") #print info about the gifs
            client.sendRemoteImage(gifs[index], message=Message(text=args.message), thread_id=args.destination, thread_type=ThreadType.USER) #send it
            printf("\033[92m{}\033[00m".format("Image sent")) #print confirmation

        else:
            printf("\033[91m{}\033[00m".format("Last message sent less than the specified delay")) #else print why it didn't send

    printf("Sleeping during " + str(delais) + " seconds")
    time.sleep(delais)
