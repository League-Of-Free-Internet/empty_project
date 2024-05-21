from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import ImageURL, News


class NewsImageURLInline(admin.TabularInline):
    """
    Позволяет отображать и добавлять несколько URL-ссылок для новостей
    в виде горизонтального расположения.
    """

    model = ImageURL
    extra = 1
    readonly_fields = (
        "id",
        "image_tag",
    )
    verbose_name = "Изображение для новости"
    verbose_name_plural = "Изображения для новостей"
    ImageURL.image_tag.short_description = "Миниатюра"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Обеспечивает отображение, фильтрацию и возможности поиска
    в панели администратора для модели Новости.
    """

    exclude = ("image",)
    inlines = (NewsImageURLInline,)
    list_display = (
        "name",
        "date",
        "short_text_preview",
    )
    list_filter = ("date",)
    search_fields = ("name",)

    def short_text_preview(self, obj: News) -> str:
        """
        Генерирует краткий текст новости.
        :param obj: Объект разработчика (экземпляр класса News).
        :type obj: News.

        :return: Краткий текст новости,
        сокращенной до 50 символов.
        :rtype: str.

        """
        return truncatechars(obj.text, 50)

    short_text_preview.short_description = "Краткий текст"
