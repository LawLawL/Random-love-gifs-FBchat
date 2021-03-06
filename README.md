# Random love gifs

This is a small program that check every X seconds (or minutes or hours) if you sent a message to the person you like on Facebook. 
More exactly, if no message was sent in that interval X, then the program will send a random gif. 
You can add your own gifs to the predefined list (see the Misc section), or completely wipe it and only put yours.

## Requirements

* [fbchat](https://fbchat.readthedocs.io/en/master/install.html) version >= 1.1.1
* [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## How to use it?

First download the script:

`wget https://raw.githubusercontent.com/Magalame/Random-love-gifs-FBchat/master/random_love_gifs.py`

then launch it, for that you have several option:

- the standard way:

`python3 random_love_gifs.py`

- if you do not want to use the preloaded gif list, type

`python3 random_love_gifs.py -n`

- you could also add your own this way:

`python3 random_love_gifs.py -n -a url1.gif,url2.gif,url3.gif`

- you could indeed add gifs without erasing the preloaded list:

`python3 random_love_gifs.py -a url1.gif,url2.gif,url3.gif`

- if you'd rather do it by typing the links one by one, in a more user-friendly fashion you could go for:

`python3 random_love_gifs.py -A`

and then type them

- if you have a text file with the format 

`url.gif`

`url2.gif`

`url3.gif`

then you could use it as input by typing

`python3 random_love_gifs.py -f filename`


After the program is launched, you will first be asked about your email, the one you use for Facebook, then about your password. 

Then the program will ask you if you want to see your friend list printed. If it is the first time you use it please press yes, 
as next to each name will be printed an ID number, and you will need that number: that it the way the program recognize who you want to send gifs to, 
it is much more pratical than dealing with names because of space, accents, homonyms, etc.
Right after you'll have to type the ID we just talked about, just copy paste it. 

Afterwards you'll be asked for the active period of the program: it will only be allowed to send gifs between a certain bracket, like from 9am to 10pm. 
Please use the 24h format, or you might get a weird result.

You will also have to specify the delay we talked about at the beginning. We use a slightly different format here: "hh:mm:ss". For example, if you type "1:2:3" then the progam will check all 1 hour 2 minutes 3 secondes. Although if you type "1:20:3", the program will check every 1 hour **20** minutes 3 seconds. 

And eventually, you can type a little message you want to attach to the gif that will be sent!

## Misc

Here is the preloaded list of gifs:

https://media.tenor.co/images/564eac526a8af795c90ce5985904096e/tenor.gif

https://media.tenor.co/images/5d5565fe47af258d83b4caa2a668ccfa/tenor.gif

https://media.tenor.co/images/c3759877cdcb86e25a1d305d5ac6fe4d/tenor.gif

https://media.tenor.co/images/56ea2b419cd997350fb2d03c11ac724b/tenor.gif

https://media3.giphy.com/media/f6y4qvdxwEDx6/200_d.gif

https://media.tenor.co/images/23e82dfb8dbe7ef24e9dc8b2412411db/tenor.gif

https://media.tenor.co/images/f6f20cda181ac07db50be80cdc4fa0c8/tenor.gif

https://media.tenor.co/images/7daf1a191e6afe50c3ecf1ff446f1d4f/tenor.gif

https://media.tenor.co/images/98764169e6a3003fc1fcf1feba434724/tenor.gif

https://media.tenor.co/images/cd6f8d04b7d0e05f2d2b8ee5457cc4ee/tenor.gif

https://media.tenor.co/images/77d90206206963c6aa5b05a2aa5c8c06/tenor.gif

https://media.tenor.co/images/9c4a6d3cb294d01177a5b1e1544a5b9b/tenor.gif

https://media.tenor.co/images/0f33bdaa5c425800765624282a7f4f16/tenor.gif

https://media.tenor.co/images/fe8d18d710bfcea6ab01e59b7056716c/tenor.gif

https://media.tenor.co/images/d6b57d4ce2b21b61cf494fbf4721a149/tenor.gif

https://media.tenor.co/images/1d397e7690f2947a46a1a65a075ceae8/tenor.gif

https://media.tenor.co/images/fced7415b284c36347037637a81c2cd6/tenor.gif

https://media.tenor.co/images/98ec6d443d6a8b420e8564dcb009fbaa/tenor.gif

https://media.tenor.co/images/0098a5aeb247ab5875cff39109218294/tenor.gif

https://media.tenor.co/images/3abca7efae57819d20fd056c55407398/tenor.gif

https://media.tenor.co/images/d2612ede953556132273ee54366d7436/tenor.gif

https://media.tenor.co/images/3c5b3494a34cf070f9091785e544b33d/tenor.gif

## Todo:
* ~allow to specify the delay in hours/minutes rather than seconds~
* ~allow to type in the gifs one can add instead of relying solely on command line arguments~
* ~add the possibility to use a file as input for gif list~
