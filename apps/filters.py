from django_filters import FilterSet, DateFilter, CharFilter

from apps.models.warehouse_model import Processing


class WarehouseFilter(FilterSet):
    start_date = DateFilter(field_name='data', lookup_expr='gte')

    processing__name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Processing
        fields = ['date', 'processing']
