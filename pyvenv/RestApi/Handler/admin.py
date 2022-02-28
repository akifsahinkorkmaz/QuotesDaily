from django.contrib import admin
from .models import Quote, Author, QuoteBank

# Register your models here.
admin.site.register([Quote, Author, QuoteBank])