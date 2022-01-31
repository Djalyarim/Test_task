from django.contrib import admin

from .models import UserWeight


@admin.register(UserWeight)
class UserweightAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'day', 'weight')
    empty_value_display = '-пусто-'
