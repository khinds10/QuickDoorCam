#!/usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import shutil, time, json, string, cgi, subprocess, json, PIL, cv2, subprocess, pprint, os
import picamera
from datetime import datetime
import numpy as np
import settings as settings
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from operator import itemgetter

# get the datetime string to save the webcam image
now = datetime.now()
imageDateString = now.strftime("%m-%d-%Y-%H:%M:%S")
        
# begin the attempt to get the current weather for sunrise data (get what time the sunrises)
count = 0
font = ImageFont.truetype("/home/pi/QuickDoorCam/fonts/BitstreamVeraSans.ttf", 16)
fontSmall = ImageFont.truetype("/home/pi/QuickDoorCam/fonts/BitstreamVeraSans.ttf", 14)
camera = picamera.PiCamera()
camera.vflip = False
camera.hflip = False
        
# current weather values
weatherInfo = None
sunriseTime = ''
currentFeelsLikeTemp = ''
currentHumidity = ''
currentSummary = ''
currentWindSpeed = ''
currentCloudCover = ''
todayFeelsLikeTempHigh = ''
todayFeelsLikeTempLow = ''
todaySummary = ''

#-----------------------------------------------------------------------------------------------------------------------------
# get the temp and conditions at sunrise and conditions for the day (try 10 times in case of network outage other errors)
#-----------------------------------------------------------------------------------------------------------------------------
while count < 10:
    try:
        count = count + 1
        weatherInfo = json.loads(subprocess.check_output(['curl', settings.weatherAPIURL]))        
        sunriseTime = weatherInfo['daily']['data'][0]['sunriseTime']
        currentFeelsLikeTemp = weatherInfo['currently']['apparentTemperature']
        currentHumidity = weatherInfo['currently']['humidity']
        currentSummary = weatherInfo['currently']['summary']
        currentWindSpeed = weatherInfo['currently']['windSpeed']
        currentCloudCover = weatherInfo['currently']['cloudCover']
        todayFeelsLikeTempHigh = weatherInfo['daily']['data'][0]['temperatureMax']
        todayFeelsLikeTempLow = weatherInfo['daily']['data'][0]['temperatureMin']
        todaySummary = weatherInfo['hourly']['summary']
        break
    except (Exception):
        time.sleep(10)

#-----------------------------------------------------------------------------------------------------------------------------
# take set number of pictures in the desired time frame after sunset (set in settings)
#-----------------------------------------------------------------------------------------------------------------------------
cameraPictureTaken = settings.projectFolder + 'image.jpg'

# capture image from camera
camera.capture(cameraPictureTaken)

# draw the current conditions and time on the sunrise full image
img = Image.open(cameraPictureTaken)
draw = ImageDraw.Draw(img)
try:
    imageCurrentlyText = 'Conditions @ [' + time.strftime('%l:%M%p on %b %d %Y') + ' ] / ' + str(currentSummary) + ' / Feels Like: ' + str(int(currentFeelsLikeTemp)) + '*F [' + str(int(currentHumidity*100)) + '%]'
    imageCurrentlyText2 = 'Wind Speed: ' + str(int(currentWindSpeed)) + ' mph / Cloud Cover: ' + str(int(currentCloudCover*100)) + '%' 
    imageForecastText = 'Today\'s Forecast: High (' + str(int(todayFeelsLikeTempHigh)) + '*F) / Low (' + str(int(todayFeelsLikeTempLow)) + '*F) / ' + str(todaySummary)
except:
    imageCurrentlyText = ''
    imageCurrentlyText2 = ''
    imageForecastText = ''

# draw text on image with a drop shadow for legibility
draw.text( (11, 401), imageCurrentlyText , (0,0,0), font=font )
draw.text( (10, 400), imageCurrentlyText , (255,255,200), font=font )
draw.text( (11, 426), imageCurrentlyText2 , (0,0,0), font=font )
draw.text( (10, 425), imageCurrentlyText2 , (255,255,200), font=font )
draw.text( (11, 451), imageForecastText , (0,0,0), font=fontSmall )
draw.text( (10, 450), imageForecastText , (200,200,200), font=fontSmall )

img.save(cameraPictureTaken)

# get the current most colorful to move over to the webserver and email it
shutil.move(cameraPictureTaken, 'webcam.jpg')
shutil.copy('webcam.jpg', '/home/pi/images/'+imageDateString+'.jpg')

# upload the image to the webhost to show on sunrise mirror
subprocess.Popen( "sshpass -p '" + settings.sftpPass + "' scp -o 'StrictHostKeyChecking no' webcam.jpg " + settings.sftpUser + "@" + settings.sftpHost + ":" + settings.sftpFolder + settings.sftpFileName, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
