from django.contrib import admin
from django.urls import path, include

from training import views


urlpatterns = [
    path('first-view', views.first_drf_view),
    path('multi-method', views.multi_method_view),
    path('first-class-view', views.FirstClassAPIView.as_view()),
    path('multi-method-class-view', views.MultiMethodAPIView.as_view()),
    path('custom-status-code', views.CustomStatusCode.as_view()),
    path('custom-header', views.CustomHeader.as_view()),
]
