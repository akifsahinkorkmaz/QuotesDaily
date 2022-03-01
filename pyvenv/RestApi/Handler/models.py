from pickle import TRUE
from django.db import models

# Declaration index matters !

class Author (models.Model):
    name = models.CharField(verbose_name="name", max_length=40)
    surname = models.CharField(verbose_name="surname", max_length=40)

    def __str__(self) -> str:
        return "%s %s" %(self.name, self.surname)

class Quote (models.Model):
    quote = models.CharField(verbose_name="quote", max_length=400)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)

class QuoteBank (models.Model):
    day = models.DateField(verbose_name="date")
    fQuote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    surl = models.SlugField(verbose_name="share-url", unique=True, max_length=4, default="1111")

class State (models.Model):
    shareurl = models.SlugField(verbose_name="surl_state", max_length=4, default="1111")
