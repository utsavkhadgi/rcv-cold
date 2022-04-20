from django.urls import path

from apps.products import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',views.test, name='index'),

    
    #Insert URLS
    path('productsregpage',views.productsregpage),
    path('productsinsert',views.productsinsert),

    
    # #EDIT URLS
    path('productseditpage/<int:id>', views.productseditpage), 
    path('updatepage/<int:id>',views.updatepage),   
    # # path('update/<int:id>', views.update),  

    #delete
    path('productsdelete/<int:id>', views.deleteproducts), 
]