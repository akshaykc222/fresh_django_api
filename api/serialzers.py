from rest_framework import serializers
from rest_framework.settings import DEFAULTS
from .models import Categories, CustomUser, Customers, Desingation, Products, Role,Business, RolePermissions, SubCategories, Tax, Unit, UserRoles,Appointments


class RoleSerializers(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Role
        fields = ('id','role_name','created_date','created_user')

class BusinessSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = ('id','name','address','pin_code','country','state','city','tax1','created_user','created_date')
    
    # def update(self, instance, validated_data):
    #     instance.id=validated_data.get('id',instance.id)

    #     return super().update(instance, validated_data)

# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = ('name','code','phone','symbol','currency')

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class DesingationSerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model=Desingation
        fields=('id','name','created_user','created_date')

class UserRoleSerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model=UserRoles
        fields=('id','role','business','user','created_date','created_user')

class RolePermisionSerializer(serializers.ModelSerializer):
     created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
     class Meta:
        model = RolePermissions
        fields=('id','role','create','edit','delete','update','created_date','created_user')

class CategorySerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Categories
        fields =  '__all__'

class SubCategorySerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = SubCategories
        fields =  '__all__'

class ProductSerialzer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Products
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Appointments
        fields = '__all__'

class TaxSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Tax
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Unit
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    created_user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Customers
        fields = '__all__'