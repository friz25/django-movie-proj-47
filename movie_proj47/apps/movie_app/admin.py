from django.contrib import admin, messages
from django.db.models import QuerySet
from django.contrib.auth.models import User

from .models import Movie, Director, Actor, DressingRoom

admin.site.register(Actor)
admin.site.register(Director)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']
    list_editable = []


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['year']
    prepopulated_fields = {'slug':('name', )}
    filter_horizontal = ['actors']
    # filter_vertical = ['actors']
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating', 'name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name','rating'] #+ строка поиска
    list_filter = ['name', 'currency'] # +фильтры справа

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть ?!'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачёт'
        return 'Шедевр'

    @admin.action(description='Установить валюту в Долларах')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в Евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR
        )


