from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.index, name='index'),
    path('post/<int:pk>', views.post, name='post'), # Integrate dynamic routing
    path('contact', views.contact, name='contact'),
    path ('about', views.about, name='about'),   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)