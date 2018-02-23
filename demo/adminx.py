'''
Created on 2018年1月26日

@author: '卓小建'
'''
from demo.models import UserInfo
import xadmin
# Register your models here.
#class FelixProjectsAdmin(admin.ModelAdmin):
# class UserInfoAdmin(object):
#     list_display = ('id','username', 'password')
# xadmin.site.register(UserInfo, UserInfoAdmin)
from xadmin import views


class UserInfoAdmin(object):
    list_display = ['username', 'password']
    search_fields = ['username', 'password']
    list_filter = ['username', 'password']

xadmin.site.register(UserInfo,UserInfoAdmin)


class GlobalSettings(object):
    site_title="后台管理系统"
    site_footer="广东原昇信息科技有限公司"
    menu_style="accordion"
xadmin.site.register(views.CommAdminView,GlobalSettings)

