from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns=[
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('sucess/', views.sucess, name='sucess'),
    path('blog_post/<int:pk>', views.individual_post, name='individual_post'),
    path('event/<int:pk>', views.individual_event, name='individual_event'),
    path('calender/', views.calender, name='calender'), 


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)