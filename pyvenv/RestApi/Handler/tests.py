from django.test import TestCase
from . import views as fn
from . import models as db

import string
import random
import datetime
import time


class QuoteTests(TestCase):
    def data(self):
        # Keys 
        self.Keynum = 10

        # Random Author
        self.AuthorCollection = {
            "names" : [
                "",
                "name",
                "Name",
                str("".join([str(i) for i in range(10)])),
                str("".join(random.choices(string.printable, k=40))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=1))),
                str("".join(random.choices(string.printable, k=20))),
            ],      
            "surnames" : [
                "",
                "surname",
                "Surname",
                "SurName",
                str("".join([str(i) for i in range(10)])),
                str("".join(random.choices(string.printable, k=40))),
                str("".join(random.choices(string.printable, k=1))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=10))),
                str("".join(random.choices(string.printable, k=20)))
            ],      
        }
        self.AuthorSelection = {}

        # Random Quote
        self.QuoteCollection = [
            "",
            "quote!",
            "quote",
            "Quote",
            str("".join([str(i) for i in range(10)])),
            str("".join(random.choices(string.printable, k=400))),
            str("".join(random.choices(string.printable, k=1))),
            str("".join(random.choices(string.printable, k=10))),
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100))),   
            str("".join(random.choices(string.printable, k=100)))   
        ]
        self.QuoteSelection = {}

        # Random day
        self.DayCollection = [
            i for i in range(7300) # 20 years into future
        ]
        self.DaySelection = {}

        
    
    def setUp(self):
        self.data()
        y = 60*60*24 # seconds at a given day

        for i in range(self.Keynum):
            # Author
            name = random.choice(self.AuthorCollection["names"])
            surname = random.choice(self.AuthorCollection["surnames"])
            self.AuthorSelection[str(i)] = {"name": name, "surname": surname}
            # Author db
            db.Author.objects.create(name= name , surname= surname)
        
        for i in range(self.Keynum):
            # Quote
            quote = random.choice(self.QuoteCollection)
            author = random.choice(list(db.Author.objects.all()))
            self.QuoteSelection[str(i)] = {"quote": quote, "aname": author.name, "asurname": author.surname}
            # Quote db
            db.Quote.objects.create(quote= quote, Author = author)
        
        for i in range(self.Keynum):
            # QuoteBank
            quote = random.choice(list(db.Quote.objects.all()))
            day = time.time() + random.choice(self.DayCollection)*y 
            day = datetime.date.fromtimestamp(day)
            self.DayCollection.append(day)
            # QuoteBank db
            db.QuoteBank.objects.create(day=day, fQuote= quote)
    
    def test_author_str(self):
        """ Author.__str__() functions as expected! """
        for i in range(self.Keynum):
            name = self.AuthorSelection[str(i)]["name"] 
            surname = self.AuthorSelection[str(i)]["surname"] 
            s_t_r = name + " " + surname

            author = db.Author.objects.all()[i]

            self.assertEqual(s_t_r, author.__str__())
    
    def test_shared_view(self):
        """ Quote bank functions as expected! """
        for i in range(self.Keynum):

           pass