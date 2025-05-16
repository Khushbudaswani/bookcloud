from django.contrib import admin
from purchase.models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'quantity', 'email', 'created_at')
    search_fields = ('name', 'email', 'book')
    list_filter = ('book', 'created_at')

