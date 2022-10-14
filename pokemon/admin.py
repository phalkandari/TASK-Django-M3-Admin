from django.contrib import admin
from .models import Pokemon
# Register your models here.


@admin.register(Pokemon)  # This is a decorator
class PokemonAdmin(admin.ModelAdmin):
    list_diplay = ("name", )
