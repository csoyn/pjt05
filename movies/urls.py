from django.urls import path
from . import views

app_name ='movies'

urlpatterns = [
    # 전체 영화 목록 조회
    path('', views.index, name='index'),
    # Form표시 및 영화 데이터 생성
    path('create/', views.create, name='create'),

    # 단일 영화 상세 조회
    path('<int:pk>/', views.detail, name='detail'),

    # Form표시 및 영화 데이터 수정 get, post
    path('<int:pk>/update/', views.update, name='update'),

    # 단일 영화 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),



]

