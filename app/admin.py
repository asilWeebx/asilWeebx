from django.contrib import admin

from app.models import Course, Best, Top, Quality, Contact, Course_Regis, Text_to_Youtube

# Register your models here.
admin.site.register(Course)
admin.site.register(Best)
admin.site.register(Top)
admin.site.register(Quality)
admin.site.register(Text_to_Youtube)
admin.site.register(Contact)
admin.site.register(Course_Regis)