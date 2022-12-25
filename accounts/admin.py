# Django packages
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Local apps
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone', 'is_admin')
    list_filter = ('is_active', 'is_admin')

    fieldsets = (
        ('Personal Info', {'fields': (
            'email', 'phone', 'password')}
        ),
        ('Permissions', {'fields': (
            'is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2')
        }),
    )

    search_fields = ('email', 'phone')
    ordering = ('email', 'phone')
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_field['is_superuser'].disabled = True
        return form

admin.site.register(User, UserAdmin)
