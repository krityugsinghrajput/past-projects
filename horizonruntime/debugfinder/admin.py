from django.contrib import admin
from .models import chapters, bookstore

# Register your models here.

class chaptersAdmin(admin.ModelAdmin):
     list_display = ("chapter", "createdby","datecreated")



class bookstoreAdmin(admin.ModelAdmin):
     list_display = ("bookname", "author","published","yearwritten")



class DebugFinderAdmin(admin.AdminSite):
    index_title = "DebugFinder Portal"
    title_header = "DebugFinder Admin Portal"
    Site_header = "DebugFinder Portal"


admin.site.register(chapters, chaptersAdmin)
admin.site.register(bookstore, bookstoreAdmin)
