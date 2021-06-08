from django.contrib import admin
from posts.models import Posts
# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user', 'photo']
    search_fields = ['title', 'user']
    fieldsets = (
    ("Post",{
        'fields': ['title','user','profile', 'photo']
    }),

    )
