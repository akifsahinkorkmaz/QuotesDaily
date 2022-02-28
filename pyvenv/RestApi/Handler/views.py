from typing import Dict
from django.http import JsonResponse, HttpResponse
import datetime
import random
from .models import Quote, Author, QuoteBank

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
            DailyQuote = QuoteBank(day = Day, fQuote = quote)
        except:
            return HttpResponse(status = 500)
    finally:
        Response = {
            "quote": DailyQuote.fQuote.quote,
            "author": DailyQuote.fQuote.Author.__str__(),
            "day": DailyQuote.day
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


def SSIMView(request):
    pass