from instabot import Bot 
from time import sleep
import os 
import shutil
import random
import instaloader
import math
from instapy import InstaPy
from textblob import TextBlob

# Scraping Bot
HASHTAG_ARRAY = ["waterpollution", "waterquality", "marineconservation", "marinelife"] # more hashtags can be added here
FOLLOW_COMMENTER_ARRAY = ['natgeo','oceana', 'unitednations', 'marine_biologist_daily', 'noaa', 'fisheriesoceanscan'] # more accounts can be added here

post_limit = 10 # maximum number of posts to make
usernames = [] # array for usernames of posts
POST_CAPTIONS = [] # array of captions
LOOP_COUNT = 1 # 
SLEEP_DURATION = 180 + math.ceil(random.random() * 100 + 1)

for k in range(LOOP_COUNT):

    for p in HASHTAG_ARRAY: # cleaning up folders
        shutil.rmtree("#" + p, ignore_errors=True)
    # LOGIN FOR WEBSCRAPING AND POSTING
    # session = InstaPy(username="roboticactivist", password="Pppppppp").login()

    # for m in FOLLOW_COMMENTER_ARRAY: # go through commenters on each account and follow a fe
    #     session.follow_commenters([m], amount=1, daysold=10, max_pic = 1, sleep_delay=SLEEP_DURATION)

    # # ENDING SESSION 
    # session.end()
    # sleep(SLEEP_DURATION)

    j = HASHTAG_ARRAY[k]
    #for j in HASHTAG_ARRAY: # iterating through multiple loops #THIS IS MEANT TO STAY COMMENTED 
    usernames.clear()
    POST_CAPTIONS.clear()
    x = 0 # counter for posts

    L = instaloader.Instaloader(filename_pattern="image"+str(x))
    hashtag = instaloader.Hashtag.from_name(L.context, j)

    for post in hashtag.get_posts(): # for loop to grab posts and usernames
        L = instaloader.Instaloader(filename_pattern="image"+str(x))
        L.download_post(post, target= "#" + str(j))
        username = post.owner_username
        usernames.append(username)
        x+=1
        if x == post_limit: 
            break 

    # Posting Bot
    imageBot = Bot() 
    imageBot.login(username="roboticactivist", password="Pppppppp")
    captions = ["Check out this eye-opening post!\n", "This really says a lot about society...\n", "Here is another excellent post...\n", "Follow this account for more interesting posts\n", "Support local charities!\n", "Stay safe out there.\n", "This account is dedicated to bringing the most important news to our viewers around the world.\n"]
    listofFiles = os.listdir(path="#"+ j)

    # getting captions
    for i in listofFiles:
        if i[-4:] == ".txt":
            temp = open("#" + j + "\\" + i, encoding = "utf8")
            contents = temp.read()
            POST_CAPTIONS.append(contents)
            
    currentNum = -1
    y = 0
    for i in listofFiles:
        print(y)
        #POST_CAPTIONS[y] = "test"
        if i[-4:] == ".jpg":
            currentImg = i
            y = int(i[5]) 
            originalCaption = TextBlob(POST_CAPTIONS[y])
            if originalCaption.sentiment.polarity > 0.7:
                POST_CAPTIONS[y] = POST_CAPTIONS[y].replace("#" + j, "")
                imageBot.upload_photo("#" + j + "\\" + currentImg,  caption = (captions[math.floor(random.random() * len(captions))] + "\n \n" + POST_CAPTIONS[y] + "\nPost from: @" + usernames[y]))
            else:
                POST_CAPTIONS[y] = POST_CAPTIONS[y].replace("#" + j, "")
                imageBot.upload_photo("#" + j + "\\" + currentImg,  caption = (captions[math.floor(random.random() * len(captions))] + "\n \n" + "\nPost from: @" + usernames[y]))
            sleep(2)
    print("Next hashtag")
    
    sleep(SLEEP_DURATION)

