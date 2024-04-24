from django.contrib import admin

from color.models import Palette, Color


class ColorInline(admin.TabularInline):
    model = Color
    readonly_fields = ('name',)
    extra = 0


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    inlines = (ColorInline,)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    autocomplete_fields = ('palette',)
    list_filter = ('palette',)
    list_display = ('name', 'palette')
    readonly_fields = ('name',)
    list_display_links = ('name', 'palette',)
