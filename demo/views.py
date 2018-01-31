from django.shortcuts import render
import json
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo.models import UserInfo
from demo.serializer import UserInfoSerializer
from django.http import request
from django.shortcuts import HttpResponse
import io,re
from django.http import JsonResponse
# PIL是python2版本的图像处理库，不过现在用Pillow比PIL强大，是python3的处理库
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import  redirect
import random
from io import BytesIO


@api_view(['GET','POST'])
def UserInfo_list(request):
    print("UserInfo_list")
#     models.UserInfoInfo.objects.create(UserInfo='yangmv',pwd='123456')
#     或者
#     obj = models.UserInfoInfo(UserInfo='yangmv',pwd='123456')
#     obj.save()
#     或者
#     dic = {'UserInfo':'yangmv','pwd':'123456'}
#     models.UserInfoInfo.objects.create(**dic)
#     UserInfo.objects.create(UserInfoname='zhuo123',password='admin123')
    if request.method=="GET":
        print("get")
        UserInfos = UserInfo.objects.all()
        serializer = UserInfoSerializer(UserInfos,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.body)
        serializer = UserInfoSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE']) #
def UserInfo_detial(request,pk):
    print("pk");
    try:
        UserInfo = UserInfo.objects.get(pk=pk)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserInfoSerializer(UserInfo)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserInfoSerializer(UserInfo,data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        UserInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.



def index(request):
    return render(request, "login.html")


# ajax登录校验回调视图函数
def login_ajax_check(request):
    # 1，获取用户输入的用户名和密码
    uname = request.POST.get('uname')
    password = request.POST.get('password')
#     # 获取用户输入的验证码
#     vcode = request.POST.get('vcode')
#     # 获取session中的验证码
#     vcode_session = request.session.get('verifycode')
#     flag = re.search(vcode, vcode_session, re.RegexFlag.IGNORECASE)
#     # 2,用户名和密码校验
    if uname == 'xiaoke' and password == '123456':
        # 保存用户的登录状态
        request.session['isLogin']=True
        request.session['uname']=uname
        request.session['password']=password
        return JsonResponse({'msg': 'ok'})
    else:
        return JsonResponse({'msg': 'fail_UserInfo'})
#     elif vcode != vcode_session:
#         return JsonResponse({'msg': 'fail_verify'})


def verify_code(request):
    print("================================================================")
    # 1，定义变量，用于画面的背景色、宽、高
    # random.randrange(20, 100)意思是在20到100之间随机找一个数
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 2，创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 3，创建画笔对象
    draw = ImageDraw.Draw(im)
    # 4，调用画笔的point()函数绘制噪点，防止攻击
    for i in range(0, 100):
        # 噪点绘制的范围
        xy = (random.randrange(0, width), random.randrange(0, height))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制出噪点
        draw.point(xy, fill=fill)
    # 5，定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 6，随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 7，构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
#     font = ImageFont.truetype('FreeMono.ttf', 23)
    # 8，构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 9，绘制4个字
    draw.text((5, 2), rand_str[0],  fill=fontcolor)
    draw.text((25, 2), rand_str[1],  fill=fontcolor)
    draw.text((50, 2), rand_str[2],  fill=fontcolor)
    draw.text((75, 2), rand_str[3],  fill=fontcolor)
    # 9，用完画笔，释放画笔
    del draw
    # 10，存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    print("rand_str:"+rand_str)
    # 11，内存文件操作
    buf = BytesIO()
    # 12，将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 13，将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# ajax登录成功视图函数
def success(request):
    # 用户已经登录
    if request.session.get('isLogin'):
        return render(request, 'success.html')
    else:
        return render(request, 'login.html')

from django.db.models import Count,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def get_ram_sum_size(asset_id):
    '''
    get the size of RAM and disk in total
    :param asset_id:  asset's id
    :return:   the size of RAM in total
    '''
    all_ram_slot = UserInfo.objects.filter(asset__id=asset_id)
    all_disk_slot = UserInfo.objects.filter(asset__id=asset_id)
    ram=0
    for slot in all_ram_slot:
        ram=ram+slot.capacity

    disk = 0
    for slot in all_disk_slot:
        disk = disk+slot.capacity
    return ram,disk

def show_asset_in_table(request):
    '''
    专门处理在服务器资产列表里面的表格信息的方法
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending
        if search:    #    判断是否有搜索字
            all_records = UserInfo.objects.filter(username__contains=search)
        else:
            all_records = UserInfo.objects.all()   # must be wirte the line code here

        if sort_column:   # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')    
            if sort_column in ['id','UserInfoname','password']:   # 如果排序的列表在这些内容里面
                if order == 'desc':   # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = UserInfo.objects.all().order_by(sort_column)

        all_records_count=all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20    # 默认是每页20行的内容，与前端默认行数一致
        try:
            pageinator = Paginator(all_records, limit)   # 开始做分页
        except Exception as e:
            print("开始做分页出错了")

        page = int(int(offset) / int(limit) + 1)    
        response_data = {'total':all_records_count,'rows':[]}   # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容


        for asset in pageinator.page(page):    
#             ram_disk = get_ram_sum_size(asset.id)    # 获取磁盘和内存的大小
            # 下面这些asset_开头的key，都是我们在前端定义好了的，前后端必须一致，前端才能接受到数据并且请求.
            response_data['rows'].append({
                "asset_id": asset.id if asset.id  else "",
                "asset_username" : asset.username if asset.username else "",
                "asset_password": asset.password if asset.password else "",
            })
            
        return  HttpResponse(json.dumps(response_data))    # 需要json处理下数据格式   

def saveORupdate(request):
    print(request)
    asset_id = request.GET.get('asset_id')
    asset_username = request.GET.get('asset_username')
    asset_password = request.GET.get('asset_password')
    response_info = {"msg":""}
    if asset_id != "" and None != asset_id:
        #models.UserInfoInfo.objects.filter(UserInfo='yangmv').update(pwd='520')
        u = UserInfo.objects.get(id=asset_id)
        u.username = asset_username
        u.password = asset_password
        u.save()
        response_info['msg'] = '信息更改成功'
    else:
        UserInfo.objects.create(username=asset_username,password=asset_password)
        response_info['msg'] = '信息保存成功'
    
    return HttpResponse(json.dumps(response_info))   


def deleteInfo(request):
    asset_id = request.GET.get('asset_id')
    response_info = {"msg":""}
    try:
        UserInfo.objects.filter(id=asset_id).delete()
        response_info['msg'] = '信息删除成功'
    except Exception as e:
        response_info['msg'] = '信息删除失败'
        
    return HttpResponse(json.dumps(response_info))

def logout(request):
    return render(request,'login.html')