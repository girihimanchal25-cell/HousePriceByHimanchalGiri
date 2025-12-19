from django.shortcuts import render
from .models import HouseData
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import pandas as pd
from sklearn.linear_model import LinearRegression

def home(request):
    return render(request, 'home.html')

def file(request):
    return render(request, 'file.html')

def addData(request):
    if request.method == "POST":
        TempArea = request.POST.get('Area')
        TempPrice = request.POST.get('Price')
        tempObj = HouseData(Area = TempArea ,Price = TempPrice)
        tempObj.save()
        return HttpResponse("data saved please add more data if you have ...")
    return render(request,'adddata.html')

def readData(request):
    data = HouseData.objects.all()
    return render(request,'readData.html',{'data':data})
    
def deletedetails(request,id):  
    data = get_object_or_404 (HouseData,id=id)
    data.delete()
    return render(request,'delete.html')

# def done():
#     return render(request,'done.html')

#housedata model name
def addfromcsv(request):
    if request.method == "POST" and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("invalid response")
        
        data = pd.read_csv(csv_file)

        for _, row in data.iterrows():
            HouseData.objects.create(
                Area= row["Area"],
                Price= row["Price"]
            )

        return HttpResponse("CSV data saved into database")
    return render(request,'uploadCsv.html')

import numpy as np
import openpyxl

def addfromexcel(request):
    if request.method == "POST" and request.FILES.get('Excel_file'):
        Excel_file = request.FILES['Excel_file']
        print(Excel_file)
        if not Excel_file.name.endswith('.xlsx'):
            return HttpResponse("invalid response")
        data = pd.read_excel(Excel_file,engine='openpyxl')
        data = pd.DataFrame(data)
        for _, row in data.iterrows():
            HouseData.objects.create(
                Area= row["Area"],
                Price= row["Price"]
            )
            HouseData.save()
        return HttpResponse("Excel data saved into database")
    return render(request,'uploadexcel.html')

def update(request,id):
    data= HouseData.objects.get(id=id)
    if request.method=="POST":
       data.Area=request.POST.get("Area")
       data.Price=request.POST.get("Price")
       data.save()
       return HttpResponse("Updated!")
    return render(request,'updatepage.html',{"data":data})

def prediction(request):
    if request.method == "POST":
        data=HouseData.objects.all().values("Area","Price")
        df=pd.DataFrame(data)
        x =df[["Area"]].dropna()
        y =df[["Price"]].dropna()
        model = LinearRegression()
        model.fit(x,y)
        area_value = float(request.POST.get("Area"))
        predicted_price = model.predict([[area_value]])
        return HttpResponse (predicted_price)
    return render(request,'prediction.html')

