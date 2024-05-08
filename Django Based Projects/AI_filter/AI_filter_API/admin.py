from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(HomePageContent)
admin.site.register(AboutPageContent)
admin.site.register(ContactPageContent)
admin.site.register(BlogPost)
admin.site.register(UserQuery)

