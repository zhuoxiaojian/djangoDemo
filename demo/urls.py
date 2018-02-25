'''
Created on 2018年1月26日

@author: '卓小建'
'''
from demo import views 
from django.urls import path
urlpatterns = [
    path('user/',views.UserInfo_list),
     # 登录成功url
    path('success/', views.success),
    # ajax登录url
    # ajax登录校验url
    path('login_ajax_check/', views.login_ajax_check),
    # 生产验证码图片url
    path('verify_code/', views.verify_code),
    path('asset_show_table',views.show_asset_in_table,name='show_asset_in_table'),  # 展示用户信息在bootstrap-table里面
    path('saveORupdate',views.saveORupdate,name="saveORupdate"),
    path('deleteInfo',views.deleteInfo,name="deleteInfo"),
    path('logout',views.logout,name="logout") 
        ]