from django.urls import path

from . import views

urlpatterns = [
    # homepage view
    path('', views.home, name='home'),
    # trek details
    path('<int:trek_id>/', views.trekDetail, name='trekDetail'),
]