from django.contrib import admin
from .models import Players, Tournaments


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'content', 'created_at', 'is_published')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'content')
    list_filter = ('is_published',)
    list_editable = ('is_published',)


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'tournament', 't_content', 'place', 'created_at', 'is_published')
    list_display_links = ('id', 'tournament')
    search_fields = ('tournament', 't_content')
    list_filter = ('is_published',)
    list_editable = ('is_published', )


admin.site.register(Players, PlayersAdmin)
admin.site.register(Tournaments, TournamentAdmin)