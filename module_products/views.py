
from itertools import product
from multiprocessing import context
from django.http import request
import requests


from turtle import title
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect  
from models.product import Product
from .services import delete, getAllProduct, getSingleProduct, insert, update
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products =  getAllProduct() 
    paginator = Paginator(products,3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {
        'products':products,
    }
    html_template = loader.get_template('module_products/products.html')
    return HttpResponse(html_template.render(context, request))

    

#Goes to Product Registraton page    productsreg.html
def productsregpage(request): 
    context = {}  
    html_template = loader.get_template('module_products/productsreg.html')
    return HttpResponse(html_template.render(context, request))



#Insert data from productsreg.html page
def productsinsert(request):      
    if request.method == "POST":     
        if hasError(request) is True:
             return redirect("/module_products/productsregpage")
        else:
            insert(request)
    return redirect("/module_products")
        
    
# Update Page Request Function
def productseditpage(request, id):  
    productsedit = getSingleProduct(id)
    context = {
        'productsedit':productsedit
    }
    
    html_template = loader.get_template('module_products/productsedit.html')
    return HttpResponse(html_template.render(context, request)) 


#Update Function
def updatepage(request,id):  
    productsedit = getSingleProduct(id)
    context = {
        'productsedit':productsedit
    }
    
    if hasError(request) is True:
        html_template = loader.get_template('module_products/productsedit.html')
        return HttpResponse(html_template.render(context, request))    
    else:      
        update(request,id)
        return redirect("/module_products")


#Delete Function
def deleteproducts(request,id):  
    delete(id)
    return redirect("/module_products") 




#Validate Registration and Edit Form
def hasError(request):
    title=request.POST.get('title')
    description=request.POST.get('description')
    price=request.POST.get('price') 

    if len(title) <= 0 or len(title)>100:
        messages.warning(request, 'Invalid details.....!!! Please enter the title less than 100 length')
        has_error = True
    elif len(description) <= 0 or len(description)>500:
        messages.warning(request, 'Invalid details.....!!! Please enter the decription less than 500 length')
        has_error = True
      
    elif price.isnumeric() is False:   
        messages.warning(request, 'Invalid details.....!!! Please enter the correct price')
        has_error = True
    else:
        has_error = False
    return has_error



    
        

