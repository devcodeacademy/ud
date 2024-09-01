from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'inn', 'is_staff', 'is_active')  # Add custom fields here
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'full_name', 'inn')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'inn', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email', 'full_name', 'inn')
    ordering = ('username',)


admin.site.register(CustomUser, UserAdmin)
