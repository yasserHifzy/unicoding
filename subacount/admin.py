from django.contrib import admin
from subacount.models import Account,Transaction,JournalEntery
class Acount_admin(admin.ModelAdmin):
    list_display=["name","parant","type","code","fullcode"]
    search_fields=["name","code","fullcode"]
    list_filter=["type"]
    ordering=["fullcode"]

admin.site.register(Account,Acount_admin)
admin.site.register(Transaction)
admin.site.register(JournalEntery)
