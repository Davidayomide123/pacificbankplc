from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_number']  # Specify fields to display in the admin list
    search_fields = ['user__username']  #

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'image_display')

    def image_display(self, obj):
        return obj.image.url if obj.image else None

admin.site.register(Details, YourModelAdmin)