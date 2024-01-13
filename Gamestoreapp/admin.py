from django.contrib import admin
from Gamestoreapp.models import Game

class GameName(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'number', 'cat']
    
admin.site.register(Game, GameName)


