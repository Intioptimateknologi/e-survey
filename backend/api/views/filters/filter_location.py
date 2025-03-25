import django_filters as filters
from django_filters.filters import Q

from location import models

class DesaFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.CharFilter(method='filter_satker', label='Satker ID')

    class Meta:
        model = models.desa
        fields = [
            'wilayah', 'nama_desa', 'nama_kecamatan',
            'nama_kabupaten', 'nama_provinsi',
            'provinsi', 'kabupaten', 'kecamatan', 'search', 'satker'
        ]
        order_by = ['nama_desa']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(Q(nama_desa__icontains=value) | Q(nama_kecamatan__icontains=value) | Q(nama_kabupaten__icontains=value) | Q(nama_provinsi__icontains=value))

class KecamatanFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.CharFilter(method='filter_satker', label='Satker ID')

    class Meta:
        model = models.kecamatan
        fields = ['kabupaten', 'search', 'satker']
        order_by = ['nama_kecamatan']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(Q(nama_desa__icontains=value) | Q(nama_kecamatan__icontains=value) | Q(nama_kabupaten__icontains=value) | Q(nama_provinsi__icontains=value))

class KabupatenFilter(filters.FilterSet):
    search = filters.CharFilter(label='Global search', method='filter_search')
    provinsi = filters.NumberFilter(field_name='provinsi')

    class Meta:
        model = models.kabupaten
        fields = ['provinsi', 'search']
        order_by = ['nama_kabupaten']

    def filter_search(self, queryset, name, value):
        return queryset.filter(Q(nama_kabupaten__icontains=value))