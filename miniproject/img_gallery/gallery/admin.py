from django.contrib import admin
from.models import blogger,post

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','contact')
#     list_display=(' title','date','content')
admin.site.register(blogger,BookAdmin)
admin.site.register(post)
