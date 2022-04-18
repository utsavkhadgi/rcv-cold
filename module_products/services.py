import imp
from sys import getallocatedblocks
# from .models import Product
from models.product import Product

def getAllProduct():
    products = Product.objects.all()  
    return products


def getSingleProduct(id):
    productsedit = Product.objects.get(id=id)   
    return productsedit
    

def insert(request):  
    title=request.POST.get('title')
    description=request.POST.get('description')
    price=request.POST.get('price')
    insert=Product(title=title,description=description,price=price)
    insert.save()

def update(request,id):  
    title = request.POST['title']
    description = request.POST['description']
    price = request.POST['price']
    productsupdate = Product.objects.get(id=id)
    productsupdate.title = title
    productsupdate.description = description
    productsupdate.price = price
    productsupdate.save()

def delete(id):
    productsdel = Product.objects.get(id=id)  
    productsdel.delete()  
 