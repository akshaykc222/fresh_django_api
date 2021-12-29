import re
from django.db.models.base import Model
from django.http import request, response
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from .models import Appointments, Business, Categories, CustomUser, Customers, Desingation, Products, Role, RolePermissions, SubCategories, Tax, Unit, UserRoles
from .serialzers import AppointmentSerializer, CategorySerialzer, CustomerSerializer, DesingationSerialzer, ProductSerialzer, RolePermisionSerializer, RoleSerializers,BusinessSerializer, SubCategorySerialzer, TaxSerializer, UnitSerializer, UserRoleSerialzer, UserSerialzer






class DesignationApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    serializer_class=DesingationSerialzer
    queryset = Desingation.objects.all()
    lookup_field="id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = DesingationSerialzer(queryset, many=True)
            return Response({"designations":serializer.data},status=status.HTTP_200_OK)
    def post(self,request):
      
        return self.create(request)
    
    def perform_create(self, serializer):
        serializ=self.request.data
        name=serializ.get("name","")
        query_set=Desingation.objects.filter(name=name)
        print(f"name:{name} set {query_set}")
        if query_set:
            raise serializers.ValidationError({"error":"data already exists","status":status.HTTP_208_ALREADY_REPORTED})
        
        return serializer.save(created_user=self.request.user)

    def put(self,request,id=None):
        return self.update(request,id)


# class UserApiView(generics.GenericAPIView,mixins.ListModelMixin):
#     serializer_class=UserDetailsSerializer
#     queryset=CustomUser.objects.all()
#     def get(self,request):
#         queryset = self.get_queryset()
#         serializer = UserDetailsSerializer(queryset)
#         return Response({"designations":serializer.data},status=status.HTTP_200_OK)

class BusinessApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=BusinessSerializer
    queryset=Business.objects.all()

    lookup_field="id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = BusinessSerializer(queryset,many=True)
            return Response({"business":serializer.data},status=status.HTTP_200_OK)
    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serialz=self.request.data
        name=serialz.get('name','')
        queryset=Business.objects.filter(name=name)
        if queryset:
            raise serializers.ValidationError({"error":"business already exists"})
        return serializer.save(created_user=self.request.user)
    
    def put(self,request,id=None):
        return self.update(request,id)


class RoleAPiView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin
                ,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=RoleSerializers
    queryset=Role.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serialz=self.request.data
        name=serialz.get('role_name','')
        queryset=Role.objects.filter(role_name=name)
        if queryset:
            raise serializers.ValidationError({"error":"role already exists"})
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = RoleSerializers(queryset,many=True)
            return Response({"roles":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

#Role prmission class is to define sepcific permission for roles
class RolePermisionApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=RolePermisionSerializer
    queryset=RolePermissions.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serialz=self.request.data
        name=serialz.get('page_name','')
        queryset=RolePermissions.objects.filter(page_name=name)
        if queryset:
            raise serializers.ValidationError({"error":"role already exists"})
        return serializer.save(created_user=self.request.user)
    
    def get(self,requet,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = RolePermisionSerializer(queryset,many=True)
            return Response({"roles":serializer.data},status=status.HTTP_200_OK)
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

##assigning created role and permission class to user
class UserRoleApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = UserRoleSerialzer
    queryset = UserRoles.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = UserRoleSerialzer(queryset,many=True)
            return Response({"user roles":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
    
class CategoryApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = CategorySerialzer
    queryset = Categories.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = CategorySerialzer(queryset,many=True)
            return Response({"categories":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
    
class SubCategoryApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = SubCategorySerialzer
    queryset = SubCategories.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:

            queryset = SubCategories.objects.filter(category=id)
            serializer = SubCategorySerialzer(queryset,many=True)
            return Response({"SubCategories":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
    
class ProductsApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = ProductSerialzer
    queryset = Products.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            queryset = Products.objects.filter(subCategory=id)
            serializer = ProductSerialzer(queryset,many=True)
            return Response({"products":serializer.data},status=status.HTTP_200_OK)
        else:
            queryset = self.get_queryset()
            serializer = ProductSerialzer(queryset,many=True)
            return Response({"products":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

class AppointmentApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointments.objects.all()

    lookup_field="id"

    def post(self,request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = AppointmentSerializer(queryset,many=True)
            return Response({"appointments":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

class UserApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = UserSerialzer
    queryset = CustomUser.objects.all()

    lookup_field="id"

    def post(self,request):
        data = request.data
        
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = UserSerialzer(queryset,many=True)
            return Response({"users":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)



class CustomerApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.all()

    lookup_field="id"

    def post(self,request):
        data = request.data
        
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = CustomerSerializer(queryset,many=True)
            return Response({"customers":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)


class TaxApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()

    lookup_field="id"

    def post(self,request):
        data = request.data
        
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = TaxSerializer(queryset,many=True)
            return Response({"tax":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)


class UnitApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    lookup_field="id"

    def post(self,request):
        data = request.data
        
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = UnitSerializer(queryset,many=True)
            return Response({"customers":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)