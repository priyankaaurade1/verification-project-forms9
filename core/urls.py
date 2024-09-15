from . import views
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


urlpatterns = [
path('',views.dashboard, name="dashboard"),  
path('login/' , views.render_login, name="login"),
path("logout/", LogoutView.as_view(), name="logout"),
path('register/', views.render_register, name='register'),

]

