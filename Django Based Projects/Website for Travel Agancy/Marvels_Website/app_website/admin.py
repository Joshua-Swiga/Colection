from django.contrib import admin
from .models import Home_Page, About_Page, Services_Page, Events_Page, Inquiries_and_Messages, Blog_Posts

# Register your models here.



admin.site.register(Home_Page)
admin.site.register(About_Page)
admin.site.register(Services_Page) 
admin.site.register(Events_Page)
admin.site.register(Inquiries_and_Messages)
admin.site.register(Blog_Posts)

