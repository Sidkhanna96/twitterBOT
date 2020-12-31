import os
import tweepy
import random
import datetime
from dotenv import load_dotenv
load_dotenv()

DIR_NAME = r"C:\Users\Test\Desktop\headlineBOT\Images"

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def getImagePath(imageFolder):
    filePath = DIR_NAME + "\\" + imageFolder
    file_list = os.listdir(filePath)
    imagePath = ""
    if(imageFolder == "headline"):
        imagePath = filePath + "\\" + file_list[random.randint(0, len(file_list)-1)]
    elif(imageFolder == "daysMeme"):
        today = datetime.date.today().strftime("%d-%B")
        for f in file_list:
            if today in f:
                imagePath = filePath + "\\" + f

    return imagePath 
    

def update_status_image(imagePath):
    if imagePath:
        try:
            api.update_with_media(imagePath)
            print('Update Status Successful')
        except Exception as e:
            print("Error: ", e)
    else:
        print('No imagePath provided')


if __name__ == "__main__":
    imagePath = getImagePath('headline')
    update_status_image(imagePath)

    imagePath = getImagePath('daysMeme')
    update_status_image(imagePath)
