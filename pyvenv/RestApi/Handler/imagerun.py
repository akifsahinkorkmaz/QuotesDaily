from PIL import Image, ImageDraw, ImageFont
from os import path
from . import textrules as trl
from django.conf import settings


# Lambdas -
static_path = "C:\\Users\\akifs\\Desktop\\QuotesDaily\\pyvenv\\RestApi\\static\\"
Font = lambda x : ImageFont.truetype("C:\\Users\\akifs\\Desktop\\QuotesDaily\\pyvenv\\RestApi\\Handler\\NotoSerif-Regular.ttf", size=x)
ImageCheck = lambda imu : True if path.isfile("%s\\download\\%s.png" %(static_path, imu)) else False


# Image Creater -
def ImageMake(date, printable, author, afont, qfont, imu, img="1.jpg"):
    try:
        img = Image.open("%s%s" %(static_path, img))
        imc = ImageDraw.Draw(img)
        imc.text((330,280), str(date), (0,0,0), anchor="ms", align="center" , font= Font(32)) 
        imc.text((330,550), printable, (0,0,0), anchor="mm", align="center", font= Font(qfont)) 
        imc.text((330,830), str(author), (0,0,0), anchor="ms", align="center", font= Font(afont)) 
        imc.text((1000,1000), (settings.FRONTURL + imu), (0,0,0), anchor="rs", align="left", font= Font(10)) 
        img.save("%s\\download\\%s.png" %(static_path, imu))
        return "static/download/%s.png" %(imu)
    except:
        return False


