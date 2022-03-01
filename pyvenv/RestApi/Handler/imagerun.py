from PIL import Image, ImageDraw, ImageFont

font = lambda x : ImageFont.truetype(".\\RestApi\\Handler\\NotoSerif-Regular.ttf", size=x)
def ImageRun(date, quote, author, imu, img=1):
    try:
        img = Image.open("static/%i.jpg" %img)
        imc = ImageDraw.Draw(img)
        imc.text((320,280), date, (0,0,0), anchor="ms", align="right" , font= font(35)) 
        imc.text((20,380), quote, (0,0,0), align="left", font= font(20)) 
        imc.text((320,830), author, (0,0,0), anchor="ms", align="right", font= font(20)) 
        img.save("static/%s.jpg" %imu)
        return "static/%s.jpg" %imu
    except:
        return False

