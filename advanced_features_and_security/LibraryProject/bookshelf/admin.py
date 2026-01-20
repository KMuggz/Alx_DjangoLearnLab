from typing import Any
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.http import HttpRequest
from .models import CustomUser,Book

# Register your models here
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    
    def get_fieldsets(self, request, obj=None): # used get_fieldsets to dynamically add custom fields and avoid type-checking errors
        fieldsets = list(super().get_fieldsets(request, obj))
        fieldsets.append(
        (None, {'fields': ('date_of_birth', 'profile_photo')})
        )
        return fieldsets

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'profile_photo'
            ),
        }),
    )



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)