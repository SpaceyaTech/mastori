from django.contrib import admin
from blog.models import Stori

# Register your models here.
class StoriAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Stori, StoriAdmin)
