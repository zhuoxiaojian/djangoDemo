from django.contrib import admin
from demo.models import UserInfo,Blog,Author,Entry
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'password')
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
# Register your models here.
