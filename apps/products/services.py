import imp
from sys import getallocatedblocks
from models.products import Products
# from models.product import Product

def getAllProduct():
    products = Products.objects.all()  
    return products


def getSingleProduct(id):
    productsedit = Products.objects.get(id=id)   
    return productsedit
    

def insert(request):  
    title=request.POST.get('title')
    description=request.POST.get('description')
    price=request.POST.get('price')
    insert=Products(title=title,description=description,price=price)
    insert.save()

def update(request,id):  
    title = request.POST['title']
    description = request.POST['description']
    price = request.POST['price']
    productsupdate = Products.objects.get(id=id)
    productsupdate.title = title
    productsupdate.description = description
    productsupdate.price = price
    productsupdate.save()

def delete(id):
    productsdel = Products.objects.get(id=id)  
    productsdel.delete()  
 