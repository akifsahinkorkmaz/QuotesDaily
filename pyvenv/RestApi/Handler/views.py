from distutils.log import error
from typing import Dict
from urllib import response
from django.http import JsonResponse, HttpResponse
import datetime
import random
from .models import Quote, Author, QuoteBank, State
from . import imagerun as imgr

def SetDynamicUrl() -> str:
    state = State.objects.get()
    result = hex(int(state.shareurl, base=16) + 1)[2:]
    state.shareurl = result
    state.save()
    return result

def DailyView(request, raw = False) -> Dict:
    """
        This function returns and (if can't finds one) selects Daily Quotes.
        
        * If Daily Quote is not found for the day: 
                * Selects from all quotes via random lib.
                * Creates new DaiyQuote (QuoteBank object).
                * Returns as instructed below:

        * If raw = False (default) returns (django) JsonResponse as {quote: Quote, author: Author, day=datetime.date.today}.
        * If raw = True returns Dict as {quote: Quote, author: Author, day=datetime.date.today}.
    """    
    Day = datetime.date.today()
    try: 
        DailyQuote = QuoteBank.objects.get(day = Day)
    except: 
        try: 
            quote = random.choice(list(Quote.objects.all()))
            DailyQuote = QuoteBank(day = Day, fQuote = quote, surl = SetDynamicUrl())
            DailyQuote.save()
        except:
            return HttpResponse(status = 500)
    
    Response = {
        "quote": DailyQuote.fQuote.quote,
        "author": DailyQuote.fQuote.Author.__str__(),
        "day": DailyQuote.day,
        "bg": DailyQuote.fQuote.Background,
        "shareurl": DailyQuote.surl
    }
    if raw:
        return Response
    else: 
        return JsonResponse(Response, headers= {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : "true",
                "Access-Control-Allow-Methods" : "GET",
                "Access-Control-Allow-Headers" : "Origin, Content-Type, Accept"    
        })

def ShareView(request, shareurl, raw=False):
    try: 
        DailyQuote = QuoteBank.objects.get(surl = shareurl)
        Response = {
            "quote": DailyQuote.fQuote.quote,
            "author": DailyQuote.fQuote.Author.__str__(),
            "day": DailyQuote.day,
            "bg": DailyQuote.fQuote.Background,
            "shareurl": DailyQuote.surl
        }
        if raw:
            return Response
        else: 
            return JsonResponse(Response, headers= {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : "true",
                "Access-Control-Allow-Methods" : "GET",
                "Access-Control-Allow-Headers" : "Origin, Content-Type, Accept"    
            })
    except:
        return HttpResponse(status = 404)
        
def SSIMView(request, shareurl = False):
    if shareurl:
        try:
            if imgr.ImageGet(shareurl):
                dlink = "static/%s.png" %shareurl
            else: 
                QB = ShareView(request, shareurl=shareurl, raw=True)
                dlink = imgr.ImageRun(QB["day"],QB["quote"], QB["author"].__str__(), QB["shareurl"], QB["bg"]) 
            return JsonResponse({"downloadlink" : dlink}, headers= {
                    "Access-Control-Allow-Origin" : "*",
                    "Access-Control-Allow-Credentials" : "true",
                    "Access-Control-Allow-Methods" : "GET",
                    "Access-Control-Allow-Headers" : "Origin, Content-Type, Accept"    
            })
        except:
            return HttpResponse(status = 500)
    else:
        return HttpResponse(status = 404)
    