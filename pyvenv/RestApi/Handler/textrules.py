import itertools

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

def TextFormat(txtarray, mw, my, islines=0):
    w = 0
    result = []
    lines = []
    if islines <= 0:
        for line in txtarray:
            for word in line:
                w = w + len(word) + 1
                if w <= mw: 
                    lines.append(word + " ")
                else:
                    wind = mw - w
                    # if 3 or less char left
                    if wind > -4 :
                        lines.append(word + " ")
                        result.append(lines)
                        lines = []
                        w = 0

                    wind = len(word) - wind
                    # if 3 or less char fit
                    if wind < 4 :
                        result.append(lines)
                        lines = [(word + " ")]
                        w = len(word + 1)
                    # break words
                    else:
                        lines.append(word[::(wind-1)]+"-")
                        result.append(lines)
                        lines = [(word[(wind-1)::] + " ")]
                        w = len(word) - wind + 2
            result.append(lines)
            lines = []
    else :
        for word in line:
                w = w + len(word) + 1
                if w <= mw: 
                    lines.append(word + " ")
                else:
                    wind = mw - w
                    # if 3 or less char left
                    if wind > -4 :
                        lines.append(word + " ")
                        result.append(lines)
                        lines = []
                        w = 0

                    wind = len(word) - wind
                    # if 3 or less char fit
                    if wind < 4 :
                        result.append(lines)
                        lines = [(word + " ")]
                        w = len(word + 1)
                    # break words
                    else:
                        lines.append(word[::(wind-1)]+"-")
                        result.append(lines)
                        lines = [(word[(wind-1)::] + " ")]
                        w = len(word) - wind + 2         

    if my <= len(result) :
        return "\n".join(["".join(i) for i in result])  
    else: return False

        



def TextFormatting(text: str) :
    result = []
    ruler = dict(font_rules)
    
    l = len(text) + 10 #h max
    
    txtarray = text.splitlines()
    txtarray = [i.split() for i in txtarray]
    
    y = len(txtarray) - 1
    
    # Find options that are not suited for l
    llist = list(ruler["l"].values())
    lind = 0
    while llist[lind] > l and lind < len(llist):
        lind += 1
    
    # Remove rules that are not an option
    if lind < len(llist):
        ruler["l"] = dict(itertools.islice(ruler["l"].items(), lind))
        ruler["w"] = dict(itertools.islice(ruler["w"].items(), lind))
        ruler["h"] = dict(itertools.islice(ruler["h"].items(), lind))
    
    # Find options that are not suited for h
    hlist = list(ruler["h"].values())
    hind = 0
    while hlist[hind] > y and hind < len(hlist):
        hind += 1
    
    # Remove rules that are not an option
    if hind < len(hlist):
        ruler["l"] = dict(itertools.islice(ruler["l"].items(), hind))
        ruler["w"] = dict(itertools.islice(ruler["w"].items(), hind))
        ruler["h"] = dict(itertools.islice(ruler["h"].items(), hind))

    # for w try biggest ->
    wlist = list(ruler["w"].values())
    wind = len(wlist)
    result = TextFormat(txtarray, wlist[wind], hlist[wind], y)
    while wind >= 0 and result == False:
        wind = wind - 1 
        result = TextFormat(txtarray, wlist[wind], hlist[wind], y)
    
    return {
        "font" : int(list(ruler["w"].keys())[wind]),
        "text" : result
    }


def AuthFontRule(text):
    l = len(text)
    if l > font_rules["w"]["20"]:
        return 16
    elif l > font_rules["w"]["24"]:
        return 20
    elif l > font_rules["w"]["28"]:
        return 24
    elif l > font_rules["w"]["32"]:
        return 28
    elif font_rules["w"]["32"] > l :
        return 32
