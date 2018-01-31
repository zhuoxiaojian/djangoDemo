from django.contrib import admin
from demo.models import UserInfo
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'password')
admin.site.register(UserInfo, UserInfoAdmin)
# Register your models here.
