from django.shortcuts import render

from ecomapp.models import products
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):    #to get limit no of details
        all_products=products
        if "limit" in request.query_params:
            lim=int(request.query_params.get("limit"))
            all_products=all_products[:lim]
        return Response(data=all_products)

    def post(self,request,*args,**kwargs):  #to create a new data
        data=request.data
        products.append(data)
        return Response(data=data)


class Productdetailview(APIView):
    def get(self, request, *args, **kwargs):  #to view a specvific id number data from dataset
        id=kwargs.get("id")
        item=[item for item in products if item["id"]==id].pop()
        return Response(data=item)

    def put(self, request, *args, **kwargs):
        id=kwargs.get("id")
        item=[item for item in products if item["id"]==id].pop()
        item.update(request.data)
        return Response(data=item)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in products if item["id"]==id].pop()
        products.remove(item)
        return Response(data=item)
