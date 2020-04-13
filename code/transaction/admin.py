from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('GENERAL', {'fields':[
            'category',
            'timestamp',
        ]}),
        ('INCOMING', {'fields':[
            'currency_in_type',
            'currency_in_quantity',
        ]}),
        ('OUTGOING', {'fields':[
            'currency_out_type',
            'currency_out_quantity',
        ]}),
        ('FEES', {'fields':[
            'fee_type',
            'fee_quantity',
        ]}),
        ('OTHER', {'fields':[
            'comments',
        ]}),
    ]
    list_display = [
        'category',
        'currency_in_type',
        'currency_in_quantity',
        'currency_out_type',
        'currency_out_quantity',
        'fee_type',
        'fee_quantity',
        'timestamp',
    ]
    list_filter = [
        'category',
        'currency_in_type',
        'currency_out_type',
    ]
    list_select_related = [
        'currency_in_type',
        'currency_out_type',
        'fee_type',
    ]
    ordering = [
        'timestamp',
    ]
    radio_fields = {
        'category': admin.HORIZONTAL,
    }
    search_fields = []

    def get_queryset(self, request):
        return (
            super().get_queryset(request)
            .select_related('currency_in_type')
            .select_related('currency_out_type')
            .select_related('fee_type')
        )


admin.site.register(Transaction, TransactionAdmin)