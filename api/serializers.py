from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer): #serializa o Usuario
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email') 


class CategorySerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) #retorna o id do relacionamento
    #user = serializers.StringRelatedField() #retorna o nome definido na class do usuario
    
    
    #read_only -> se True fixa o campo apenas como leitura    
    user = UserSerializer(read_only=True) 

    # write_only-> se True fixa o campo apenas como Escrita
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user') 

    class Meta:
        model = Category
        #fields = '__all__' 
        fields = ('id','name', 'description','user', 'user_id')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                    write_only=True, source='categories', many=True )
    class Meta:
        model = Product
        fields = ('id', 'name', 'price','categories', 'categories_id')
