from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PatientSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)#eta user er name int teke int e convert kore
    class Meta:
        model = models.Patient
        fields = '__all__'

class registrationSerializer(serializers.ModelSerializer):
    confiram_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confiram_password']

    def save(self):
        username = self.validated_data['username']    
        email = self.validated_data['email']    
        password = self.validated_data['password']    
        password2= self.validated_data['confiram_password']
        first_name= self.validated_data['first_name']
        last_name= self.validated_data['last_name']

        if password != password2:
            raise serializers.ValidationError({'error' : "password dos't match"})    
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error' : "Email Already Exists"})    
        
        account = User(username = username, email = email, first_name = first_name, last_name = last_name)
           
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
class userLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)   
    password = serializers.CharField(required = True)   