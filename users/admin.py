from django.contrib import admin
from django. contrib. auth. admin import UserAdmin as BaseUserAdmin
from django. contrib. auth. models import User
# Models
from  users.models import Profile
# Register your models here.

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
        list_display = ['user','website','phone_number','picture']
        list_display_links = ['user', 'phone_number']
        search_fields = ['user__email','phone_number','user__first_name']
        fieldsets = (

            ("Profile",{
                'fields':['user'],

            }),
            (
                "Others",{
                    'fields': ['website','phone_number', 'biography']
                }

            )
            ,
            ("Picture",{
                'fields':['picture'],
            }),
        )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
