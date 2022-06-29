from django.urls import path, re_path

from . import views

urlpatterns = [
    # homepage view
    path('', views.home, name='home'),
    # trek details
    path('<int:trek_id>/', views.trekDetail, name='trekDetail'),
    # re_path(r'^profile/(?P<username>[A-Za-z0-9]+)', views.profile)
    path('profile/<str:username>', views.profile, name='profile')
]