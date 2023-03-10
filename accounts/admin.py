from .models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'is_active', 'is_vendor', 'is_superuser']
    list_display_links = ('email', 'username')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ['password']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)