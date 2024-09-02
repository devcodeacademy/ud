from django.contrib import admin
from .models import TagGroup, Tag, Premises


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class TagGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [TagInline]


class PremisesAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'area', 'price', 'availability_start_date', 'availability_end_date']
    search_fields = ['name', 'address', 'description']


admin.site.register(TagGroup, TagGroupAdmin)
admin.site.register(Premises, PremisesAdmin)
