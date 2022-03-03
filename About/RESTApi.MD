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
    "shareurl": "String"
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
    "shareurl": "String"
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
example download link: "static/1113.png"

------