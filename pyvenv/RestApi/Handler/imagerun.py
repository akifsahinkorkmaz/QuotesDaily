from PIL import Image, ImageDraw, ImageFont
from os import path

# Lambdas -
Font = lambda x : ImageFont.truetype("C:\\Users\\akifs\\Desktop\\QuotesDaily\\pyvenv\\RestApi\\Handler\\NotoSerif-Regular.ttf", size=x)
ImageGet = lambda imu : True if path.isfile("static/%s.jpg" %imu) else False
real_path = "C:\\Users\\akifs\\Desktop\\QuotesDaily\\pyvenv\\static\\"


# Font Rule -
font_rules = {
    "w": {
        "16": 40,
        "20": 30,
        "24": 26,
        "28": 22,
        "32": 18,
    },

    "h" : {
        "16": 9,
        "20": 8,
        "24": 7,
        "28": 6,
        "32": 5,
    },

    "l": {
        "16": 400, 
        "20": 270, 
        "24": 208, 
        "28": 154, 
        "32": 108, 
    }
}

def TextManipulation(forcedlines, arraylike, w, f) -> str:
        result = ""
        letter = 0
        if forcedlines>1:
            for lines in arraylike:
                for words in lines:
                    letter = letter + len(words)
                    if letter < w:
                        result = result + words + " "
                    else:
                        letter = len(words)
                        result = result + "\n" + words + " "
                result = result + "\n" 
        else:
            for words in arraylike:
                letter = letter + len(words)
                if letter < w:
                    result = result + words + " "
                else:
                    letter = len(words)
                    result = result + "\n" + words + " "
        result.replace(" \n", "\n")
        return {
            "text": result,
            "font": f
        }

def FontRule(text: str):
    forcedlines = text.count("\n")
    l = len(text)
    w = max([len(i) for i in text.split(" ")])
    if forcedlines >= 1 :
        arraylike = text.split("\n")
        for i in range(len(arraylike)):
            arraylike[i] = arraylike[i].split(" ")
    else: 
        arraylike = text.split(" ")

    # If f-16 is only option for length or forcedlines
    if l > font_rules["l"]["20"] or forcedlines > font_rules["h"]["20"]:
        return TextManipulation(forcedlines, arraylike, font_rules["w"]["16"], "16")  
        
    # If f-20 is an option for length or forcedlines
    elif font_rules["l"]["24"] < l < font_rules["l"]["20"] or forcedlines > font_rules["h"]["24"]:
        return TextManipulation(forcedlines, arraylike, font_rules["w"]["20"], "20")  

    # If f-24 is an option for length or forcedlines
    elif  font_rules["l"]["28"] < l < font_rules["l"]["24"] or forcedlines > font_rules["h"]["28"]:
        return TextManipulation(forcedlines, arraylike, font_rules["w"]["24"], "24")  
    
    # If f-28 is an option for length or forcedlines
    elif  font_rules["l"]["32"] < l < font_rules["l"]["28"] or forcedlines > font_rules["h"]["32"]:
        return TextManipulation(forcedlines, arraylike, font_rules["w"]["28"], "28")  
    
    # If f-32 is an option for length or forcedlines
    elif  l < font_rules["l"]["32"]:
        return TextManipulation(forcedlines, arraylike, font_rules["w"]["32"], "32") 

def AuthFontRule(text):
    l = len(text)
    if l > font_rules["w"]["20"]:
        return 16
    elif font_rules["w"]["20"] > l > font_rules["w"]["24"]:
        return 20
    elif font_rules["w"]["24"] > l > font_rules["w"]["28"]:
        return 24
    elif font_rules["w"]["28"] > l > font_rules["w"]["32"]:
        return 28
    elif font_rules["w"]["32"] > l :
        return 32


# Image Creater -
def ImageRun(date, quote, author, imu, img=1):
    try:
        img = Image.open("%s%d.jpg" %(real_path, img))
        imc = ImageDraw.Draw(img)
        imc.text((330,280), str(date), (0,0,0), anchor="ms", align="center" , font= Font(32)) 
        quote_dict = FontRule(str(quote))
        imc.text((330,550), quote_dict["text"], (0,0,0), anchor="mm", align="center", font= Font(int(quote_dict["font"]))) 
        imc.text((330,830), str(author), (0,0,0), anchor="ms", align="center", font= Font(AuthFontRule(str(author)))) 
        img.save("%s%s.png" %(real_path, imu))
        return "%s%s.jpg" %(real_path, imu)
    except:
        return False


