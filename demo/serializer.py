'''
Created on 2018年1月26日

@author: admin
'''
from rest_framework import serializers
from demo.models import UserInfo
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id',"username","password")
