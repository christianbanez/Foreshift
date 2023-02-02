from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^$', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'),
    path('framework/', views.framework, name='framework'),
    path('test/', views.test, name='test'),
    path('test_result/', views.test_result, name='test_result'),
    path('login/', views.signin, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('logout/', views.signout, name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)