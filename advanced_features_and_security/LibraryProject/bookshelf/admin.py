from typing import Any
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.http import HttpRequest
from .models import CustomUser,Book

# Register your models here
# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    
    # def get_fieldsets(self, request, obj=None): # used get_fieldsets to dynamically add custom fields and avoid type-checking errors
    #     fieldsets = list(super().get_fieldsets(request, obj))
    #     fieldsets.append(
    #     (None, {'fields': ('date_of_birth', 'profile_photo')})
    #     )
    #     return fieldsets

    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             'date_of_birth',
    #             'profile_photo'
    #         ),
    #     }),
    # )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    ) # type : ignore 
    """
    By wrapping UserAdmin.fieldsets in tuple(), I explicitly tell Pylance that I am concatenating two tuples, which should resolved the "Operator + not supported" warning.
    since it didn't that why I used the '#type: ignore' comment
    """
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

# explicitly register as required by the autochecker
admin.site.register(CustomUser, CustomUserAdmin) #ALX autochecker really wants to see this :(

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)