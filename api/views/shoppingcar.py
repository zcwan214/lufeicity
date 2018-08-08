from django.shortcuts import render,HttpResponse
# from django.views import View
from rest_framework.viewsets import ModelViewSet
from api import serializers as app01_serializers
import json
from rest_framework.views import APIView
from api.models import CourseCategory,CourseSubCategory,\
    DegreeCourse,Teacher,Scholarship,Course,CourseDetail,OftenAskedQuestion,\
    CourseOutline,CourseChapter,CourseSection,CourseSection,CourseSection

# class CoursesView(ModelViewSet):
#     queryset=Course.objects.all()
#     serializer_class =app01_serializers.Course_serializers

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response


import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api import models
from api.serializers.shoppingcar import CarSerializer
from api.utils.response import BaseResponse


# SHOPPING_CAR = {
#     1:{
#         2:{
#             'title':'xxxx',
#             'price':1,
#             'price_list':[
#                 {'id':11,},
#                 {'id':22},
#                 {'id':33},
#             ]
#         },
#         3:{},
#         5:{}
#     },
#     2:{},
#     3:{},
# }

class ShoppingCarView(ViewSetMixin,APIView):

    def get(self,request,*args,**kwargs):
        """
        加入购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        """
        1. 接受用户选中的课程ID和价格策略ID
        2. 判断合法性
            - 课程是否存在？
            - 价格策略是否合法？
        3. 把商品和价格策略信息放入购物车 SHOPPING_CAR
        
        注意：用户ID=1
        """
        # 接受价格
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.PricePolicy.objects.all()

            # 分页
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser = CarSerializer(instance=queryset, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'


        return Response(ret.dict)