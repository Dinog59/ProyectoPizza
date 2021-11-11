from django.contrib import admin
from django.contrib.admin.decorators import register
from inventario.models import InventoryAccount, InventoryTransaction

# Register your models here.

class InventoryTransactionInline(admin.TabularInline):
    model=InventoryTransaction
    readonly_fields=('created_on', )

@admin.register(InventoryAccount)
class InventoryAccountAdmin(admin.ModelAdmin):

    readonly_fields = ('sum',)
    inlines=[InventoryTransactionInline]