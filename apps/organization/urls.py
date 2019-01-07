# -*- coding: utf-8 -*-
from django.urls import path,include,re_path
from apps.organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView

urlpatterns = [
    #课程机构列表页
    path(r'list/', OrgView.as_view(), name='org_list'),
    path(r'add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path(r'home/(?P<org_id>\d+)/',OrgHomeView.as_view(),name ='org_home'),
    re_path(r'course/(?P<org_id>\d+)/',OrgCourseView.as_view(),name ='org_course'),
    re_path(r'desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    re_path(r'teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),
    path(r'add_fav/', AddFavView.as_view(), name='add_fav'),

]