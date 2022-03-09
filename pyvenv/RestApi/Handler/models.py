from django.db import models
from . import textrules as trl

# Declaration index matters !

class Author (models.Model):
    name = models.CharField(verbose_name="name", max_length=20)
    surname = models.CharField(verbose_name="surname", max_length=20)

    def __str__(self) -> str:
        return "%s %s" %(self.name, self.surname)


class Quote (models.Model):
    quote = models.TextField(verbose_name="quote", max_length=300)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    printable = models.TextField(verbose_name="printable-quote", max_length=400)
    qfont = models.IntegerField("quote-font", default=16)
    afont = models.IntegerField("author-font", default=16)

    BACKGROUND_CHOICES = [
        ("1.jpg", "diamond"),
        ("2.jpg", "heart"),
        ("3.jpg", "round"),
    ]
    Background = models.CharField(verbose_name="bg-image", choices=BACKGROUND_CHOICES, max_length=6, default="1.jpg")

    def save(self, *args, **kwargs) -> None:
        # Get printing options
        self.afont = trl.AuthFontRule(self.Author.__str__())
        q = trl.TextFormatting(self.quote)
        self.qfont = q["font"]
        self.printable = q["text"]
        super(Quote, self).save(*args, **kwargs)


class QuoteBank (models.Model):
    day = models.DateField(verbose_name="date")
    fQuote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    surl = models.SlugField(verbose_name="share-url", unique=True, max_length=4, default="1111")

    
class State (models.Model):
    shareurl = models.SlugField(verbose_name="surl_state", max_length=4, default="1111")
