from django.contrib import admin

from chat.models import ConvoChats

# Register your models here.

class ConvoChatsAdmin(admin.ModelAdmin):
    list_display = ('contact_date', 'message', 'phone')
    list_display_links = ('contact_date', 'message', 'phone')
    search_fields = ('contact_date', 'message')
    list_per_page = 25
admin.site.register(ConvoChats, ConvoChatsAdmin)
