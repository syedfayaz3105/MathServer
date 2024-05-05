# Ex.05 Design a Website for Server Side Processing
## Date:29-04-2024

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
maths.html

<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Surface Area of Right cylinder</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body 
{
background-color:pink;
}
.edge {
width: 1440px;
margin-left: auto;
margin-right: auto;
padding-top: 250px;
padding-left: 300px;
}
.box {
display:block;
border: Thick dashed lime;
width: 500px;
min-height: 300px;
font-size: 20px;
background-color:white;
}
.formelt{
color:orange;
text-align: center;
margin-top: 7px;
margin-bottom: 6px;
}
h1
{
color:rgb(255, 0, 179);
text-align: center;
padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
<div class="box">
<h1>Surface Area of Right Cylinder</h1>
<form method="POST">
{% csrf_token %}
<div class="formelt">
Radius : <input type="text" name="base" value="{{r}}"></input>(in m)<br/>
</div>
<div class="formelt">
Height : <input type="text" name="height" value="{{h}}"></input>(in m)<br/>
</div>
<div class="formelt">
<input type="submit" value="Calculate"></input><br/>
</div>
<div class="formelt">
Area : <input type="text" name="area" value="{{area}}"></input>m<sup>2</sup><br/>
</div>
</form>
</div>
</div>
</body>
</html>
```
```
views.py

from django.shortcuts import render
def cylinderarea(request):
    context={}
    context['area'] = "0"
    context['b'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        b = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('radius=',b)
        print('height=',h)
        area  = 2 * 3.14 * int(b) * int(h) + 2 * 3.14 *int(b) * int(b)
        context['area'] = area
        context['r'] = b
        context['h'] = h
        print('area=',area)
    return render(request,'far/maths.html',context)

```
```
urls.py

from django.contrib import admin
from django.urls import path
from far import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofcylinder/',views.cylinderarea,name="areaofcylinder"),
    path('',views.cylinderarea,name="areaofcylinderroot")
]
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (13).png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-05-05 180345.png>)

## RESULT:
The program for performing server side processing is completed successfully.
