from django.shortcuts import render
from .serializer import ProductSerializer
from rest_framework.views import APIView
from .models import Products
from rest_framework.response import Response
# Create your views here.


class ProductAPIView(APIView):

    def get(self, req):
        products_list = Products.objects.all()
        return Response({'products':ProductSerializer(products_list, many=True).data})

    def post(self, req):
        serializer = ProductSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cost = validated_data.get('title', instance.cost)

    def put(self,req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({'error': 'Objectdoes not exists'})

        serializer = ProductSerializer(data=req.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self,req,*args, **kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error': 'Method DELETE not alowed'})

        products_list = Products.objects.get(pk=pk)
        products_list.delete()

        return Response({'post':'delete post ' + str(pk)})