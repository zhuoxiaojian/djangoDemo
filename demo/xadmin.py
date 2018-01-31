'''
Created on 2018年1月26日

@author: '卓小建'
'''
from demo.models import UserInfo
import xadmin
# Register your models here.
#class FelixProjectsAdmin(admin.ModelAdmin):
class UserInfoAdmin(object):
    list_display = ('id','username', 'password')
xadmin.site.register(UserInfo, UserInfoAdmin)


