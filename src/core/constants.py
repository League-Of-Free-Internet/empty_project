MAX_LIST_LENGTH = 15
MAX_LENGTH_DEFAULT = 255
MAX_LENGTH = 5000


class NewsCfg:
    """
    Настройки для модели News.
    """

    HELP_MSG_NAME = "Введите название новости"
    HELP_MSG_TXT = f"Напишите текст новости до {MAX_LENGTH} символов"
    HELP_MSG_IMG = "Добавьте ссылки на изображения"


class EventsCfg:
    """
    Настройки для модели Events.
    """
    EVENTS = "Events"
    EVENTS_NAME_VERBOSE_NAME = "Название события"
    EVENTS_NAME_HELP_MSG = "Введите название события"
    EVENTS_DESCRIPTION_VERBOSE_NAME = "Описание события"
    EVENTS_DESCRIPTION_HELP_MSG = (
        f"Напишите текст о событии до {MAX_LENGTH} символов"
    )
    EVENTS_IMG_RELATED_NAME = "events_images"
    EVENTS_IMG_URLS_VERBOSE_NAME = "Изображения для события"
    EVENTS_IMG_URLS_HELP_MSG = "Добавьте ссылки на изображения с событиями"
    EVENTS_PUB_DATE_VERBOSE_NAME = "Дата события"
    EVENTS_PUB_DATE_HELP_MSG = "Выберите дату события"
    EVENTS_PLACE_VERBOSE_NAME = "Место события"
    EVENTS_PLACE_HELP_MSG = "Введите название места события"
    EVENTS_DISCIPLINE_VERBOSE_NAME = "Дисциплина для события"
    EVENTS_DISCIPLINE_HELP_MSG = "Выберите дисциплину для события"
    EVENTS_META_VERBOSE_NAME = "Событие"
    EVENTS_META_VERBOSE_NAME_PLURAL = "События"


class EventsImageURLCfg:
    EVENTS_IMAGE_URL = "EventsImageURL"
    EVENTS_IMG_URL_FOREIGN_RELATED_NAME = "events"
    EVENTS_IMG_URL_FOREIGN_VERBOSE_NAME = "События"
    EVENTS_IMG_URL_VERBOSE_NAME = "Ссылка на изображение события"
    EVENTS_IMG_URL_HELP_MSG = "Укажите URL-адрес изображения о событии"


class DisciplinesCfg:
    """
    Настройки для модели Disciplines.
    """

    DISCIPLINES = "Disciplines"
    DISCIPLINES_NAME_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_NAME_HELP_MSG = "Напишите название дисциплины"
    DISCIPLINES_DESCRIPTION_VERBOSE_NAME = "Описание дисциплины"
    DISCIPLINES_DESCRIPTION_HELP_MSG = (
        f"Напишите описание дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINES_IMG_URLS_RELATED_NAME = "disciplines_images"
    DISCIPLINES_IMG_URLS_VERBOSE_NAME = "Изображения для дисциплин"
    DISCIPLINES_IMG_URLS_HELP_MSG = (
        "Добавьте ссылки на изображения с дисциплиной"
    )
    DISCIPLINES_RULES_VERBOSE_NAME = "Правила спортивных дисциплин"
    DISCIPLINES_RULES_HELP_MSG = (
        f"Напишите правила дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINES_META_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_META_VERBOSE_NAME_PLURAL = "Спортивные дисциплины"


class DisciplinesImageURLCfg:
    """
    Настройки для модели DisciplinesImageURL.
    """

    DISCIPLINES_IMG_URL = "DisciplinesImageURL"
    DISCIPLINES_IMG_URL_FOREIGN_RELATED_NAME = "discipline"
    DISCIPLINES_IMG_URL_FOREIGN_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_IMG_URL_VERBOSE_NAME = "Ссылка на изображение с дисциплиной"
    DISCIPLINES_IMG_URL_HELP_MSG = (
        "Укажите URL-адрес изображения со спортивной дисциплиной"
    )


class AboutCfg:
    HELP_MSG_VIDEO = "Укажите URL-адрес видео"
    HELP_MSG_IMG = "Укажите URL-адрес изображения"
    HELP_MSG_NAME = "Введите имя участника"
    HELP_MSG_TXT = f"Укажите текст истории до {MAX_LENGTH} символов"
    HELP_MSG_PARTNER = "Введите название партнера"
    HELP_MSG_ROLE = "Название роли, к которой относится участник"
    HELP_MSG_BRAND = "Укажите название"
    MAX_LENGTH_NAME = 50


class CustomUserCfg:
    HELP_MSG_FIRST = "Введите имя"
    HELP_MSG_LAST = "Введите фамилию"
    HELP_MSG_PHONE = "Введите номер телефона в формате +7999 999 99 99"
    HELP_MSG_ROLE = "Название роли, к которой относится пользователь"
    MAX_LENGTH_NAME = 50
