from django.urls import path

from . import views

urlpatterns = [
    # homepage view
    path('', views.home, name='home'),
    # trek details
    path('<int:trek_id>/', views.trekDetail, name='trekDetail'),
    # re_path(r'^profile/(?P<username>[A-Za-z0-9]+)', views.profile)
    path('profile/<str:username>', views.profile, name='profile'),
    #login 
    path('login/', views.login, name='login'),
    #dologin
    path('dologin/', views.dologin, name='dologin'),
    # blank page
    path('blank/', views.blank, name='blank')
    
]