# -*- coding: UTF-8 -*-

# Twitter Bot 4.0
# By Travis
# GitHub: https://github.com/TravisPooley/Twitter-Giveaway-Bot

# imports #
import tweepy
import random
from time import sleep
import sqlite3
import re
import datetime
import json
import sys
import os




# -------------------- # START ASCII ART # ------------------ #
os.system('cls')
print(' _______ ________ _______ _______ _______ _______ ______      ______ _______ _______ ')
print('|_     _|  |  |  |_     _|_     _|_     _|    ___|   __ \    |   __ \       |_     _|')
print('  |   | |  |  |  |_|   |_  |   |   |   | |    ___|      <    |   __ <   -   | |   |  ')
print('  |___| |________|_______| |___|   |___| |_______|___|__|    |______/_______| |___|  ')
print('                                                                                     ')
print('         ______ ___ ___      _______ ______ _______ ___ ___ _______ _______          ')
print('        |   __ \   |   |    |_     _|   __ \   _   |   |   |_     _|     __|         ')
print('        |   __ <\     /       |   | |      <       |   |   |_|   |_|__     |         ')
print('        |______/ |___|        |___| |___|__|___|___|\_____/|_______|_______|    V 4.2')
print('')
print('Initialising...')

# --------------------- # END ASCII ART # ------------------- #

# - # START VALIDATATION AND CONFIRMATION OF CONFIG DATA # - #
# Open config file
try:
    # Importing file
    with open('config.js', 'r') as configFile:
        # Reading File
        configFile = configFile.read()
        # Removing comments from config
        configFile = re.sub("//.*","",configFile,flags=re.MULTILINE)
        # Saving the config into program
        config = json.loads(configFile)
                            
        

    # Validating config value for consumerKey
    try:
        # Setting config value for consumerKey
        consumerKey = str(config['consumerKey'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"consumerKey" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for consumerSecret
    try:
        # Setting config value for consumerSecret
        consumerSecret = str(config['consumerSecret'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"consumerSecret" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        sys.exit()

    # Validating config value for accessToken
    try:
        # Setting config value for accessToken
        accessToken = str(config['accessToken'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"accessToken" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
         # Stop Bot Running
        sys.exit()

    # Validating config value for acessTokenSectret
    try:
        # Setting config value for acessTokenSectret
        acessTokenSectret = str(config['acessTokenSectret'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"acessTokenSectret" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for daysTokeep
    try:
        # Setting config value for daysTokeep
        days_to_keep = int(config['daysTokeep'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"daysTokeep" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for amountToScan
    try:
        # Setting config value for amountToScan
        amountToScan = int(config['amountToScan'])
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"amountToScan" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()
        
    # Validating config value for scanInterval 
    try:
        # Setting config value for scanInterval
        scanInterval = int(config['scanInterval'])
        nextScanStart = (datetime.datetime.now() + datetime.timedelta(minutes = scanInterval))
        # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"scanInterval" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for checkMessagesInterval 
    try:
        # Setting config value for checkMessagesInterval
        checkMessagesInterval = int(config['checkMessagesInterval'])
        nextMessageScanStart = (datetime.datetime.now() + datetime.timedelta(minutes = 0))
        # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"checkMessagesInterval" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for amountToScanMessages 
    try:
        # Setting config value for amountToScanMessages
        amountToScanMessages = int(config['amountToScanMessages'])
        # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"amountToScanMessages" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for ghostmode 
    try:
        # Setting config value for ghostmode
        if config['ghostmode'] == 'True':
            ghostmode = True
        elif config['ghostmode'] == 'False':
            ghostmode = False
        else:
            print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"ghostmode" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
            sys.exit()

        # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"ghostmode" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()

    # Validating config value for printMode 
    try:
        # Setting config value for printMode
        if config['printMode'] == 'True':
            printMode = True
        elif config['printMode'] == 'False':
            printMode = False
        else:
            print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"printMode" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
            sys.exit()
     # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"printMode" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()


    # Validating config value for tradeLink 
    try:
        # Setting config value for tradeLink
       tradeLink = config['tradeLink']
    # Validation exception
    except (ValueError, KeyError):
        tradeLink = 'NOT DEFINED';



    # Validating config value for tagUSers
    try:
        # Setting config value for tagUSers
       #slave accounts
        tagUsers = []
        for slave in config['slaveAccounts']:
            tagUsers.append(slave)
    # Validation exception
    except (ValueError, KeyError):
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'"slaveAccounts" is not defined or is invalid in config, check the config make sure it looks like the config in the example here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/blob/master/SetupGuide.md')
        # Stop Bot Running
        sys.exit()
except IOError:
        # Error logging
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'no config file found, download an example config file here: https://github.com/TravisPooley/Twitter-Giveaway-Bot/')
        # Stop Bot Running
        sys.exit()

# - # END VALIDATATION AND CONFIRMATION OF CONFIG DATA # - #


# --------------- # START TWITTER LOGIN # ----------------- #

# using user login infomation to setvup the bots authentication #
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, acessTokenSectret)
auth.secure = True
api = tweepy.API (auth)
# ---------------- # END TWITTER LOGIN # ------------------ #

print('CURRENTLY TESTING: '+tradeLink)
# ------------- # START VARIBALE ASSIGNMENT # ------------- #


start_time = datetime.datetime.now()
lastGeneralSave = (datetime.datetime.now() + datetime.timedelta(minutes = 1))
# Value that stores the amount of retweet actions
reTweets = int(0)
# Value that stores the amount of favorite actions
favorites = int(0)
# Value that stores the amount of follow actions
follows = int(0)
# Value that stores the amount of errors
errors = int(0)
# Value that stores the amount giveaways scanned
scanned = int(0)
# Value that stores the amount of comments
comments = int(0)
# Value that stores the amount of tweets that are skipped due to being substandard
skips = int(0)
# Value that stores the amount of replies
replys = int(0)
# Value that stores the amount of tweets that are skipped due to being already scanned
skipalready = int(0)
# Value that stores the amount of tweets that are skipped due to being spam
skipspam = int(0)
# Value that stores the amount of tweets that are skipped due to the username being blocked
skipname = int(0)
# Value that stores the amount of new tweets found to be spam
newspam = int(0)
# Value that was supposed to be tempary to store the image url
image = "None"
# Value of the amount of giveaways won
wins = int(0)
# Vaule of the amount of direct messages scanned
dms = int(0)
# defining replys to send the user if they message the bot saying it won #
messages = [
    "Hey I think I won the giveaway",
    "I'm the winner of the giveaway",
    "Hey, I blieve I won the giveaway.",
    "I won the giveaway",
    "I'm the winner of the latest giveay",
    "I belive I'm the winner of the latest giveay",
    "I won the latest giveay",
    "I'm pretty sure I'm the winner of the latest giveay",
    "I won the giveaway"
]
# -------------- # END VARIBALE ASSIGNMENT # -------------- #





# --------------- # START DATABASE SETUP # ---------------- #
conn = sqlite3.connect('Bot1.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS General(Retweets, Favourites, Follows, Replies, Scanned, Found, STweets, BTweets, BUsers, Errors, Time, RunTime TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Errors(Code, Time, TweetID TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Tweets(ID, Username, Tweet, Time, Actions, FullName, ProfilePicture, TweetPicture TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Message(MessageId, RecipicantID, Username, RealName, ProfilePicture, Flags, Message, MessageTime, SaveTime TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS BlockedUsers(Username, FullName, UserID, ProfilePicture, Reason, Time, UnBlockTime TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Whitelist(Username, FullName, UserID, ProfilePicture, Reason, Time TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS BlockedTweets(BlockedtweetText, Reason TEXT)')

# ---------------- # END DATABASE SETUP # ----------------- #


print('set up complete')


class TwitterBot:
    def showStats(self):
        print('')
        print('found: ' + str(scanned - skips))
        print('errors: ' + str(errors))
        print('scanned: ' + str(scanned))
        print('retweets: ' + str(reTweets))
        print('follows: ' + str(follows))
        print('replies: ' + str(replys))
        print('favorites: ' + str(favorites))
        print('total skipped: ' + str(skips))
        print('blocked tweets: ' + str(skipspam))
        print('blocked users tweets: ' + str(skipname))
        print('spam tweets discorvered: ' + str(newspam))
        print('tweets scanned multiple times: ' + str(skipalready))
        end_time = datetime.datetime.now()
        print('Run Time: ' + '{}'.format(end_time - start_time))
        print('Time Now: ' + str(datetime.datetime.now()))
        lastGeneralSave = (datetime.datetime.now() + datetime.timedelta(minutes = 1))
        print('finished')
        print('')


        print('                                   &@@@@@@@@@@@          &           Twitter Bot')
        print('   @%                           .@@@@@@@@@@@@@@@@/  &@@@@            -----------')
        print('  &@@@/                        @@@@@@@@@@@@@@@@@@@@@@@@              Version: 4.2')
        print('  @@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@ /@@@           Tweets Found:')
        print('  @@@@@@@@@(                 @@@@@@@@@@@@@@@@@@@@@@@@@@@#            Errors Found')
        print('  @@@@@@@@@@@@@              @@@@@@@@@@@@@@@@@@@@@@@@@.              Amount Scanned')
        print('   @@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@                Amount Of Retweets')
        print('    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                Amount Of Follows')
        print('  .   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                Amount Of Replies')
        print('  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                Amount Of Favorites')
        print('  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%      ')
        print('   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       ')
        print('     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        ')
        print('       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#        ')
        print('           (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         ')
        print('       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#          ')
        print('        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,           ')
        print('          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             ')
        print('             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.              ')
        print('                @@@@@@@@@@@@@@@@@@@@@@@@@@,                ')
        print('            &@@@@@@@@@@@@@@@@@@@@@@@@@@@                   ')
        print('(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                       ')
        print('   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                         ')
        print('        /@@@@@@@@@@@@@@@@@@@#                              ')






    def CleanAccount(self):
        while True:
            try:
                # Defining the date and time of cut off
                cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days_to_keep)
                print('')
                print('Startigng Cleaing Opperations')
                currentOperation = 'None';

                print('')
                print('Starting Unfriending Opperation')
                currentOperation = 'Unfriending'
                # Getting all of the users the account is following
                friend = tweepy.Cursor(api.friends).items()
                # Loop through all users
                for user in friend:
                    # Checking if account has been followed for longer than cut off
                    if user.created_at < cutoff_date:
                        # Unfollow User
                        api.destroy_friendship(user.id)
                        # Logging in console
                        if printMode == True:
                            print("Unfollowing: @"+user.screen_name+", UserID: " + str(user.id))
                print('Unfriending Opperation Complete')

                print('')
                print('Starting Tweet Deletion Opperations')
                currentOperation = 'Tweet Deletion'
                # Defining the tweets that the account has posted
                timeline = tweepy.Cursor(api.user_timeline).items()
                # Looping through all tweets
                for tweet in timeline:
                    # Check if tweet was created before cut off
                    if tweet.created_at < cutoff_date:
                        # Check if the user wants to log the infomation to console
                        if printMode == True:
                            # Log the infomation to console
                            print("Deleting " + str(tweet.id))
                        # Perform action
                        api.destroy_status(tweet.id)
                print('finished deleting tweets')

                print('')
                print('Starting Favorite Deletion Opperations')
                currentOperation = 'Favorite Deletion'
                # Getting all of the tweets the user has favorited
                favorites = tweepy.Cursor(api.favorites).items()
                # Looping through all the tweets
                for tweet in favorites:
                    # Check if tweet was created before the cut of date
                    if tweet.created_at < cutoff_date:
                        if printMode == True:
                            print("Unfavoring " + str(tweet.id))
                        api.destroy_favorite(tweet.id)
                print('finished deleting favorites')


            except tweepy.TweepError as ERR:
                print('')
                if str(ERR) == str("[{u'message': u'Rate limit exceeded', u'code': 88}]"):
                    print("error rate limit hit")
                    print("waiting 2 minutes before testing limits")
                    sleep(120)
                    print('Attempting to Continue '+currentOperation+' Opperations')
                    continue
                else:
                    print('unexpected error')
                    sleep(30)
                    print('Attempting to Continue '+currentOperation+' Opperations')
                    continue





    def GiveAwaySearch(self):
        print('')
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Startigng giveaway scan")
        print('')
        try:
            for tweet in tweepy.Cursor(api.search, q='steam OR key giveaway OR win follow -filter:retweets',tweet_mode='extended').items(amountToScan):
                    # ---------------- # START INFOMATION DEFINITION # ---------------- #
                    # Defining Tweets Creators Name
                    tweettext = tweet.full_text.lower()
                    # Defining Tweets Id
                    tweetid = tweet.id
                    # Defining Tweets Creators Screen Name
                    tweetname = tweet.user.screen_name
                    # Defining Tweets Creators User Id
                    userid = tweet.user.id
                    # Defining Tweets Creators Name
                    tweetfullname = tweet.user.name
                    # Defining Tweets Creators Profile Picture
                    tweetProfilePicture = tweet.user.profile_image_url_https
                    # Defining Tweets Flag Level
                    tweetFlagLevel = int(0)
                    # Defining Actions To Be Performed
                    tweetActions = []
                    # ----------------- # END INFOMATION DEFINITION # -----------------  #

                    # -------------- # START DATABASE SAFTEY OPERATIONS # -------------- #
                    # Removing Unsafe Charaters From Tweet
                    tweettext = (tweettext.encode('ascii',errors='ignore'))
                    tweettext = str(tweettext.decode("utf-8"))
                    tweettext = str(tweettext).replace("'", "")
                    tweettext = tweettext.replace('"', '')
                    # Removing Unsafe Charaters From Tweet Creators Screen Name
                    tweetname = (tweetname.encode('ascii',errors='ignore'))
                    tweetname = str(tweetname.decode("utf-8"))
                    tweetname = tweetname.replace("'", "")
                    tweetname = tweetname.replace('"', '')
                    # Removing Unsafe Charaters From Tweet Creators Full Name
                    tweetfullname = (tweetfullname.encode('ascii',errors='ignore'))
                    tweetfullname = str(tweetfullname.decode("utf-8"))
                    tweetfullname = tweetfullname.replace("'", "")
                    tweetfullname = tweetfullname.replace('"', '')
                    # --------------- # END DATABASE SAFTEY OPERATIONS # --------------- #
                    # ------------------ # START DATABASE OPERATIONS # ----------------- #

                    # Checking Database To See If Tweet Has Already Been Ccanned
                    for check in c.execute("select EXISTS(SELECT 1 FROM Tweets WHERE ID='" + str(tweetid) + "')").fetchall():
                        if(check[0] > 0):
                            tweetFlagLevel = tweetFlagLevel + 100
                            tweetActions.append('Tweet text appeared in the tweet database [ALREADY SCANNED]')

                    # Checking If Current Tweet Is In The Black Listed Tweets List
                    for check in c.execute("select EXISTS(SELECT 1 FROM BlockedTweets WHERE BlockedtweetText='" + str(tweettext) + "')").fetchall():
                        if(check[0] > 0):
                            tweetFlagLevel = tweetFlagLevel + 1
                            tweetActions.append('Tweet text appeared in the blocked tweet database {BLOCKED TWEET]')

                    # Check If Current User From Tweet Is In The Black Listed Users
                    for check in c.execute("select EXISTS(SELECT 1 FROM BlockedUsers WHERE Username='" + str(tweetname) + "')").fetchall():
                        if(check[0] > 0):
                            tweetFlagLevel = tweetFlagLevel + 1
                            tweetActions.append('Tweet user appeared in the blocked user database {BLOCKED USER]')

                    # Check If Current User From Tweet Is Spamming Giveaways
                    for check in c.execute("select EXISTS(SELECT 1 FROM BlockedUsers WHERE Username='" + str(tweetname) + "')").fetchall():
                        if(check[0] == 0):
                            for check in c.execute("SELECT COUNT(*) from Tweets where Username LIKE '" + str(tweetname) + "'").fetchall():
                                if(check[0] > 15):
                                    for check in c.execute("SELECT COUNT(*) from Whitelist where Username LIKE '" + str(tweetname) + "'").fetchall():
                                        if(check[0] == 0):
                                            print('BLOCCKING USER '+ str(tweetname))
                                            tweetActions.append('User has made too many giveaways {BLOCKING USER]')
                                            tweetFlagLevel = tweetFlagLevel + 1
                                            c.execute('INSERT INTO BlockedUsers (Username, FullName, UserID, ProfilePicture, Reason, Time, UnBlockTime) VALUES("' + str(tweetname) + '","' + str(tweetfullname) + '","' + str(userid) + '","' + str(tweetProfilePicture)+ '","' + str('User has been found in tweets over 15 times') + '","' + str(datetime.datetime.now())+ '","' + str('Never') + '")')


                    # Check through database to see if current tweet text appears multiple times
                    # First check if tweet is in the blocked tweet databse
                    for check in c.execute("select EXISTS(SELECT 1 FROM BlockedTweets WHERE BlockedtweetText='" + str(tweettext) + "')").fetchall():
                        # Check if it is not in blocked tweets database
                        if(check[0] < 1):
                            # Count the occurnces of the tweets text in the database
                            for check in c.execute("SELECT COUNT(*) from Tweets where Tweet LIKE '" + str(tweettext) + "'").fetchall():
                                # If the current tweet is found more than x times in the database
                                if check[0] > 15:
                                    # Append actions for debuging
                                    tweetActions.append('Tweet has been found too many times {BLOCKING TWEET]')
                                    # Seting the flag level so the tweet does not get actions done to it
                                    tweetFlagLevel = tweetFlagLevel + 1
                                    # Append the tweets text to the database of all blocked tweets
                                    c.execute('INSERT INTO BlockedTweets (BlockedtweetText, Reason) VALUES("' + str(tweettext) + '","' + str('Tweet has been found 15 times in the tweet database')+ '")')



                    # ------------------- # END DATABASE OPERATIONS # ------------------ #

                    # ------------ # START PRELIMINARY BLOCKING OPERATIONS # ----------- #

                    # Check if tweet is a retweet
                    if tweettext.startswith("retweeted"):
                        # Seting the flag level so the tweet does not get actions done to it
                       tweetFlagLevel = tweetFlagLevel + 1
                           # Append actions for debuging
                       tweetActions.append('Tweet appears to be a retweet [RETWEET]')
                   # Check if tweet is a reply
                    if tweettext.startswith("@"):
                        # Seting the flag level so the tweet does not get actions done to it
                        tweetFlagLevel = tweetFlagLevel + 1
                            # Append actions for debuging
                        tweetActions.append('Tweet appears to be a reply [REPLY]')
                    # Check if tweet is a reply
                    if tweet.is_quote_status == True:
                        # Seting the flag level so the tweet does not get actions done to it
                        tweetFlagLevel = tweetFlagLevel + 1
                            # Append actions for debuging
                        tweetActions.append('Tweet appears to be a quote [QUOTE]')
                    if "keyword" in tweettext:
                        tweetFlagLevel = tweetFlagLevel + 1
                        # Append actions for debuging
                        tweetActions.append('requires external actions [keyword in stream]')

                    # Checking if acoount is an account setup to expose giveaway seeking bots
                    # Defining the keywords that are found in the annoying bots names
                    blockednames = ['spotting', 'sp0tting', 'bot', 'b0t']
                    # Loop through all blocked names
                    for blockedname in blockednames:
                        # Check if current users name contains the blocked keywords
                        if blockedname in tweetname:
                            # Check if the user is already blocked in the database
                            for check in c.execute("select EXISTS(SELECT 1 FROM BlockedUsers WHERE Username='" + str(tweetname) + "')").fetchall():
                                # Check if it is not in database
                                if(check[0] == 0):
                                    # Append the users infoamtion into the blocked users databse
                                    c.execute('INSERT INTO BlockedUsers (Username, FullName, UserID, ProfilePicture, Reason, Time, UnBlockTime) VALUES("' + str(tweetname) + '","' + str(tweetfullname) + '","' + str(userid) + '","' + str(tweetProfilePicture)+ '","' + str('Full name contains ') + str(tweetname) + '","' + str(datetime.datetime.now())+ '","' + str('Never') + '")')
                                    conn.commit()
                                    # Seting the flag level so the tweet does not get actions done to it
                                    tweetFlagLevel = tweetFlagLevel + 1
                                    # Appeding to the actions of tweet for debuging
                                    tweetActions.append('User getting blocked {BLOCKED]')

                    # ------------- # END PRELIMINARY BLOCKING OPERATIONS # ------------ #

                    # ------------- # START PERFORMING TWITTER OPERATIONS # ------------ #


                    # Checking if tweet meets standards for primary actions
                    if tweetFlagLevel == 0:
                        if printMode == True:
                            print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Found New Tweet From: @" + str(tweetname) + ' at: ' + str(tweetid))
                        # Checking if rewteeting is required to enter
                        retweeetKeyWords = ['-rt ', ' rt ', 'retweet', 're-tweet ']
                        for check in retweeetKeyWords:
                            if check in tweettext:
                                # Checking if bot has already performed retweet action CLIENT SIDE
                                if "RETWEET" not in tweetActions:
                                    # Checking if bot has already performed retweet action SERVER SIDE
                                    if tweet.retweeted == False:
                                        # Checking if bot is not in ghost mode before performing actions
                                        if ghostmode == False:
                                            # Twitter action retweet tweet
                                            api.retweet(tweetid)
                                # appending retweet to the list of actions performed
                                tweetActions.append('RETWEET')

                    # Checking if tweet meets standards for primary actions
                    if tweetFlagLevel == 0:
                        # Checking if rewteeting is required to enter
                        favoriteKeyWords = ['favorite', 'like', 'fav', 'heart']
                        for check in favoriteKeyWords:
                            if check in tweettext:
                                # Checking if bot has already performed retweet action CLIENT SIDE
                                if "FAVORITE" not in tweetActions:
                                    # Checking if bot has already performed retweet action SERVER SIDE
                                    if tweet.favorited  == False:
                                        # Checking if bot is not in ghost mode before performing actions
                                        if ghostmode == False:
                                            # Twitter action favorite tweet
                                            api.create_favorite(tweetid)
                                # appending retweet to the list of actions performed
                                tweetActions.append('FAVORITE')



                    # Checking if tweet meets standards for primary actions
                    if tweetFlagLevel == 0:
                        # Checking if tagging is required to enter
                        if "tag " in tweettext.replace('instagram', ''):
                            # Checking if bot has already performed tag action CLIENT SIDE
                            if "TAG" not in tweetActions:
                                print('tweet')
                                befor_keyowrd, keyword, after_keyword = tweettext.partition('tag')
                                # Checking if bot is not in ghost mode before performing actions
                                if ghostmode == False:
                                    # Checking a certain amount of accounts need to be tagged
                                    if str(after_keyword[1]).isdigit() == True:
                                        print('digit')
                                        if int(after_keyword[1]) <= len(tagUsers):
                                            numberOfTags = int(after_keyword[1])
                                        else:
                                           numberOfTags = len(tagUsers)
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), numberOfTags))), str(tweetid))
                                    # Checking ifa single account need to be tagged
                                    elif str(after_keyword[1]) == "a":
                                        print('a')
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), 1))), str(tweetid))
                                    elif str(after_keyword[1]) == "two":
                                        print('two')
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), 2))), str(tweetid))
                                    elif str(after_keyword[1]) == "three":
                                        print('three')
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), 3))), str(tweetid))
                                    elif str(after_keyword[1]) == "some":
                                        print('some')
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), 3))), str(tweetid))
                                    # Checking if should use radnom tagging fallback
                                    # str(after_keyword[1]) != "a" and str(after_keyword[1]).isdigit() == False
                                    else:
                                        # Twitter action follow user
                                        print('else')
                                        api.update_status(str('@' + str(tweetname) + ''.join(random.sample(set(tagUsers), 3))), str(tweetid))
                                        
                                # appending tag to the list of actions performed
                                tweetActions.append('TAG')

                    #if tweetFlagLevel == 0:
                    #    if "" in tweettext:
                    #        if "" not in tweetActions:
                    #            if ghostmode == False:
                    #                if

                    # Checking if tweet meets standards for primary actions
                    if tweetFlagLevel == 0 and "RETWEET" in tweetActions or "FAVORITE" in tweetActions:
                        # Checking if following is required to enter
                        if "follow" in tweettext:
                            # Checking if bot has already performed follow action CLIENT SIDE
                            if "FOLLOW" not in tweetActions:
                                # Checking if bot has already performed retweet action SERVER SIDE
                                if tweet.user.following == False:
                                    # Checking if bot is not in ghost mode before performing actions
                                    if ghostmode == False:
                                        # Twitter action follow user
                                        api.create_friendship(userid)
                                # appending retweet to the list of actions performed
                                tweetActions.append('FOLLOW')

                    # Checking if tweet meets standards for primary actions
                    if tweetFlagLevel == 0:
                        # Checking if sending tradelink is required to enter
                        if "tradelink" in tweettext:
                            if tradeLink != "NOT DEFINED":
                                # Checking if action has already been performed
                                if "STEAMLINK" not in tweetActions:
                                    # Checking if Actions Are Allowed
                                    if ghostmode == False:
                                        # Performing Action
                                        api.update_status(str('@' + str(tweetname) +" "+tradeLink), str(tweetid))
                                    # appending action to list of actions performed
                                    actions.append('STEAMLINK')

                    # Checking if tweet was flgged
                    if tweetFlagLevel == 0:
                        # Checking if there was no actions performed on tweet
                        if "FOLLOW" or "RETWEET" not in tweetActions:
                            tweetActions.append('NOT ENOUGH KEY WORDS TO PERFORM ACTIONS')


                    # -------------- # END PERFORMING TWITTER OPERATIONS # ------------- #

                    # ---------------- # START FINAL SAVING OPERATIONS # --------------- #
                    # Checking if tweet passed all flagging tests
                    if tweetFlagLevel < 99:
                        # appending the tweets data to the database
                        c.execute('INSERT INTO Tweets (ID, Username, Tweet, Time, Actions, FullName, ProfilePicture, TweetPicture) VALUES("' + str(tweetid) + '","' + str(tweetname) + '","' + str(tweettext) + '","' + str(datetime.datetime.now())+ '","' + str(tweetActions) + '","' + str(tweetfullname)+ '","' + str(tweetProfilePicture) + '","' + str(image) + '")')
                        conn.commit()

                    # ----------------- # END FINAL SAVING OPERATIONS # ---------------- #

        # Error Handling
        except tweepy.TweepError as e:
            print(e.reason)
            # Checking if account has been restricted
            if "326" in e.reason:
                # Error logging
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'your account has been locked! ERROR CODE: '+e.reason)
                # Stop Bot Running
                sys.exit()
            # Checking if account has been restricted
            if "write" in e.reason:
                print('error')
                sleep(4444)
            # Checking if account has hit rate limits
            if "429" in e.reason:
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Rate limit hit waiting 2 minutes")
                # sleeping program for 2 minutes before performing any more actions
                sleep(120)
            # Checking if the author of the tweet has blocked the bot
            if "blocked" in e.reason:
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Encountered a user who has blocked the current account adding to database")
                c.execute('INSERT INTO BlockedUsers (Username, FullName, UserID, ProfilePicture, Reason, Time, UnBlockTime) VALUES("' + str(tweetname) + '","' + str(tweetfullname) + '","' + str(userid) + '","' + str(tweetProfilePicture)+ '","' + str('Revenge') + '","' + str(datetime.datetime.now())+ '","' + str('Never') + '")')
                conn.commit()
            if "already" in e.reason:
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > Actions performed multiple times on same tweet")
                c.execute('INSERT INTO Tweets (ID, Username, Tweet, Time, Actions, FullName, ProfilePicture) VALUES("' + str(tweetid) + '","' + str(tweetname) + '","' + str(tweettext) + '","' + str(datetime.datetime.now())+ '","' + "ERROR: "  + str(tweetActions) + '","' + str(tweetfullname)+ '","' + str(tweetProfilePicture) + '")')
                conn.commit()








        print('')
        print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Finishd giveaway scan")
        print('')






    def mentionChecker(self):
        pass
    
    def checkDirectMessages(self):
        # function for saving direct messages and respoding with automated responses
        print('')
        print('Startigng Scan On Direct Messages')
        print('')
        #if (random.randint(0, 10) == 10):
        #    directMessages = tweepy.Cursor(api.sent_direct_messages,tweet_mode='extended').items(50)

        try:
            directMessages = tweepy.Cursor(api.direct_messages,tweet_mode='extended').items(amountToScanMessages)
            for direct in directMessages:

                # ---------------- # START INFOMATION DEFINITION #----------------  #
                # Defining Senders Id
                recipicantID = direct.sender.id
                # Defining Id
                directId = direct.id
                # Defining Sent Time
                directTime = direct.sender.created_at
                # Defining Senders Real Name
                directName = direct.sender.name
                # Defining Senders Screen Name
                directScreenName = direct.sender.screen_name
                # Defining Senders Profile Picture
                directProfilePicture = direct.sender.profile_image_url
                # Defining Direct Messages Text
                directText = direct.text
                # Flag Level
                flagLevel = int(0)
                # message actions
                messageActions = []

                # ----------------- # END INFOMATION DEFINITION #----------------  #
                # -------------- # START DATABASE SAFTEY OPERATIONS # -------------- #
                # Removing Unsafe Charaters From The Message
                directText = (directText.encode('ascii',errors='ignore'))
                
                directText = str(directText.decode("utf-8"))
                directText = directText.replace("'", "")
                directText = directText.replace('"', '')
                # Removing Unsafe Charaters From Message Senders Name
                directName = (directName.encode('ascii',errors='ignore'))
                
                directName = str(directName.decode("utf-8"))
                directName = directName.replace("'", "")
                directName = directName.replace('"', '')
                #  Unsafe Charaters From Tweet Creators Screen Name
                directScreenName = (directScreenName.encode('ascii',errors='ignore'))
                directScreenName = str(directScreenName.decode("utf-8"))
                directScreenName = directScreenName.replace("'", "")
                directScreenName = directScreenName.replace('"', '')
                # --------------- # END DATABASE SAFTEY OPERATIONS # --------------- #
                # ---------------- # START DATABASE OPERATIONS #----------------  #

                # Searching For Direct Message In Database
                c.execute("select EXISTS(SELECT 1 FROM Message WHERE MessageId='" + str(directId) + "')")
                # Checking If Direct Message Has Already Been Scanned
                for oldDirect in c.fetchall():
                    if oldDirect[0] == 0:
                  
                        c.execute('INSERT INTO Message (MessageId, RecipicantID, Username, RealName, ProfilePicture, Flags, Message, MessageTime, SaveTime) VALUES("' + str(directId) + '","' + str(recipicantID) + '","' + str(directScreenName) + '","' + str(directName) + '","' + str(directProfilePicture) + '","' + str("test") + '","' + str(directText) + '","' + str(directTime) + '","' + str(datetime.datetime.now()) + '")')
                        conn.commit()
                    else:
                        flagLevel = int(100);

                # ---------------- # End DATABASE OPERATIONS #----------------  #

                # ---------------- # START AUTO RESPONSE #----------------  #
                        # add elif satements
                        # Automatic Tradelink Sending
                if flagLevel < 99:
                    print('New Direct Message')
                    print('')
                    print(directText)
                    keyWordsForTradeLink = ['tradelink', 'trade-link', 'trade link', ' tl ']
                    for keyWord in keyWordsForTradeLink:
                        if keyWord in directText:
                            if tradeLink != "NOT DEFINED":
                                if ghostmode == False:
                                    api.send_direct_message(recipicantID, text = tradeLink)

                    keyWordsForWin = ['winner', 'won', 'congratulations', 'congrats']
                    winResposes = ['Wow, did I win', 'Am I the winner of the competetion', 'Did I actually win?', 'I believe I am the winner of the giveaway']
                    for keyWord in keyWordsForWin:
                        if keyWord in directText:
                            if 'WON' not in messageActions:
                                if ghostmode == False:
                                    api.send_direct_message(recipicantID, text = random.choice(winResposes))
                                messageActions.append('WON')
                                print('sending')
                       
                # ----------------- # END AUTO RESPONSE #----------------  #

            print('Finished Scan On Direct Messages')
            print('')

            
        except tweepy.TweepError as ERR:
            print(ERR)
            if "326" in e.reason:
                # Error logging
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - ERROR > "+'your account has been locked! ERROR CODE: '+e.reason)
                # Stop Bot Running
                sys.exit()
            # Checking if account has hit rate limits
            if "429" in e.reason:
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Rate limit hit waiting 2 minutes")
                # sleeping program for 2 minutes before performing any more actions
                sleep(120)
            # Checking if the author of the tweet has blocked the bot
            if "blocked" in e.reason:
                print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Encountered a user who has blocked the current account adding to database")
                c.execute('INSERT INTO BlockedUsers (Username, FullName, UserID, ProfilePicture, Reason, Time, UnBlockTime) VALUES("' + str(tweetname) + '","' + str(tweetfullname) + '","' + str(userid) + '","' + str(tweetProfilePicture)+ '","' + str('Revenge') + '","' + str(datetime.datetime.now())+ '","' + str('Never') + '")')
                conn.commit()











                

TwitterBot = TwitterBot()
print ("Active Account: '"+api.me().name+"'")
print('')

#TEST
nextScanStart = (datetime.datetime.now() + datetime.timedelta(minutes = 0))  

while True:


    # PRINT METHOD
    #print("["+str(datetime.datetime.now()).split(".")[0]+"] - INFO > Starting tweet scan")
    if datetime.datetime.now() >= nextMessageScanStart:
        TwitterBot.checkDirectMessages()
        nextMessageScanStart = (datetime.datetime.now() + datetime.timedelta(minutes = checkMessagesInterval))
    elif datetime.datetime.now() >= nextScanStart:
        TwitterBot.GiveAwaySearch()
        nextScanStart = (datetime.datetime.now() + datetime.timedelta(minutes = scanInterval))

    #TwitterBot.CleanAccount()





    # every x time
    #
    #sleep(300)







