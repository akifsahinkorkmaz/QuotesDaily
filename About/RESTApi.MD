# Rest Api Endpoints

------
## Daily Quote:

url: "/" (empty-base)

example url: "api.com/"  

content: Json | 500 error

structure: 
-
```json
{
    "quote": "String",
    "author": "String",
    "day": "String",
    "shareurl": "String",
    
    "printable": "String",
    "qfont": 16,
    "afont": 16,
    "bg": "String",
}
```
------

## Share Link:

url: "/< slug: share - link >" 

example url: "api.com/1113"  

content: Json | 404 error

structure: 
-
```json
{
    "quote": "String",
    "author": "String",
    "day": "String",
    "shareurl": "String",
    
    "printable": "String",
    "qfont": 16,
    "afont": 16,
    "bg": "String",
}
```

------

## Server Side Image Manipulation Link:

url: "/ssim/< slug: share - link >" 

example url: "api.com/ssim/1113"  

content: Json | 404 error | 500 error

structure: 
-
```json
{
    "downloadlink": "String",
}

```
example download link: "static/download/1113.png"

------

## Image Download:

url: "/static/download/< slug: share - link >.png" 

example url: "api.com/static/download/1113.png"  

content: Image | 404 error | 500 error

------