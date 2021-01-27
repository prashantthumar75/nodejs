from django.urls import path
from .views import RegisterView, TmpView, LogView\
    , ShowView, UserDetailView, UserUpdateView, LogOutView


urlpatterns=[
    path('', RegisterView.as_view()),
    path('template/', TmpView.as_view(template_name='list.html'), name='template'),
    path('accounts/login/', LogView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('list/', ShowView.as_view(template_name='list.html'), name='list'),
    path('update/<int:pk>', UserUpdateView.as_view(template_name='update.html'), name='list'),
    path('detail/<int:pk>',UserDetailView.as_view(template_name='detail.html'), name='list'),
]