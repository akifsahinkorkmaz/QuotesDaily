import itertools

# Font Rule -
font_rules = {
    "w": {
        "16": 42,
        "20": 32,
        "24": 28,
        "28": 24,
        "32": 20,
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
        "28": 156, 
        "32": 112, 
    }
}

def TextFormat(txtarray, mw, my):
    w = 0
    result = []
    lines = []

    for line in txtarray:
        for word in line:
            w = w + len(word)
            if w <= mw: 
                lines.append(word + " ")
                if w < mw : w = w + 1
            else:
                wind = mw - w
                # if 3 or less char left
                if wind > -4 :
                    lines.append(word)
                    result.append(lines)
                    lines = []
                    w = 0
                else:
                    wind =  len(word) + wind
                    # if 3 or less char fit     
                    if wind < 4 :
                        result.append(lines)
                        lines = [(word + " ")]
                        w = len(word) + 1 
                    # break words
                    elif wind > 3:
                        lines.append(word[::(wind-1)]+"-")
                        result.append(lines)
                        lines = [(word[(wind)::] + " ")]
                        w = len(word) - wind 
        result.append(lines)
        lines = []

    if my >= len(result) :
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
    lind = len(llist) - 1

    while llist[lind] < l and lind >= 0:
        lind =  lind - 1
    
    # Remove rules that are not an option
    if lind < len(llist):
        ruler["l"] = dict(itertools.islice(ruler["l"].items(), lind+1))
        ruler["w"] = dict(itertools.islice(ruler["w"].items(), lind+1))
        ruler["h"] = dict(itertools.islice(ruler["h"].items(), lind+1))
    

    # Find options that are not suited for h
    hlist = list(ruler["h"].values())
    hind = len(hlist) - 1

    while hlist[hind] < y and hind >= 0:
        hind = hind - 1
    
    # Remove rules that are not an option
    if hind < len(hlist):
        ruler["l"] = dict(itertools.islice(ruler["l"].items(), hind+1))
        ruler["w"] = dict(itertools.islice(ruler["w"].items(), hind+1))
        ruler["h"] = dict(itertools.islice(ruler["h"].items(), hind+1))


    # for w try biggest ->
    wlist = list(ruler["w"].keys())
    wkind = len(wlist)-1
    wind = wlist[wkind]
    result = TextFormat(txtarray, ruler["w"][wind], ruler["h"][wind])
    while wkind >= 0 and result == False:
        wkind = wkind - 1 
        wind = wlist[wkind]
        result = TextFormat(txtarray, ruler["w"][wind], ruler["h"][wind])
    
    return {
        "font" : int(wind),
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
