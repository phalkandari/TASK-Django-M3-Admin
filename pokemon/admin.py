from django.contrib import admin
from .models import Pokemon
# Register your models here.


@admin.register(Pokemon)  # This is a decorator
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hp', 'active',)
    list_display_links = ('id', 'name',)
    list_filter = ('active',)
    readonly_fields = ('created_at', 'modified_at',)

    fieldsets = (
        (
            "general", {
                'fields': ('name', 'hp', 'active', 'type',)
            }
        ),
        (
            'Localizations', {
                'fields': ('name_ar', 'name_fr', 'name_jp',),
                'classes': ('collapse',)
            }
        ),
        (
            None, {
                'fields': ('created_at', 'updated_at',)
            }
        )
    )


# Always finish a tuple with a comma!


# Or to register your site use this (the first has to be the Model)
# admin.site.register(Pokemon, PokemonAdmin)
