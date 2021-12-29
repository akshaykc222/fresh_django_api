from django.contrib import admin
from django.urls import path, include
from .views import (BusinessApiView, CustomerApiView, DesignationApiView,RoleAPiView,RolePermisionApiView, TaxApiView, UnitApiView, 
            UserRoleApiView,CategoryApiView,SubCategoryApiView,ProductsApiView,AppointmentApiView,UserApiView)
from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('designation/', DesignationApiView.as_view(),name="desingantions"),
    path('designation/<int:id>/', DesignationApiView.as_view()),
    # path('users/',UserApiView.as_view(),name="users"),
    path('business/',BusinessApiView.as_view(),name="business"),
    path('business/<int:id>/',BusinessApiView.as_view(),name="business"),
    path('roles/',RoleAPiView.as_view(),name="roles"),
    path('roles/<int:id>/',RoleAPiView.as_view(),name="roles"),
    path('permisions/',RolePermisionApiView.as_view(),name="permisions"),
    path('permisions/<int:id>/',RolePermisionApiView.as_view(),name="permisions"),
    path('user_roles/',UserRoleApiView.as_view(),name="user_roles"),
    path('user_roles/<int:id>/',UserRoleApiView.as_view(),name="user_roles"),
    path('categories/',CategoryApiView.as_view(),name="categories"),
    path('categories/<int:id>/',CategoryApiView.as_view(),name="categories"),
    path('sub_category/',SubCategoryApiView.as_view(),name="sub_category"),
    path('sub_category/<int:id>/',SubCategoryApiView.as_view(),name="sub_category"),
    path('products/',ProductsApiView.as_view(),name="products"),
    path('products/<int:id>/',ProductsApiView.as_view(),name="products"),
    path('appointments/',AppointmentApiView.as_view(),name="appointments"),
    path('appointments/<int:id>/',AppointmentApiView.as_view(),name="appointments"),
    path('users/',UserApiView.as_view(),name="users"),
    path('users/<int:id>/',UserApiView.as_view(),name="users"),
    path('tax/',TaxApiView.as_view(),name="tax"),
    path('tax/<int:id>/',TaxApiView.as_view(),name="tax"),
    path('unit/',UnitApiView.as_view(),name="unit"),
    path('unit/<int:id>/',UnitApiView.as_view(),name="unit"),
    path('customers/',CustomerApiView.as_view(),name="customers"),
    path('customers/<int:id>/',CustomerApiView.as_view(),name="customers"),
 path('openapi/', get_schema_view(
        title="perfect api",
        description=""
    ), name='openapi-schema'),
]
