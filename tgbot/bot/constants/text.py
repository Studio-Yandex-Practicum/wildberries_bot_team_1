START_MESSAGE = '''
Привет! Чтобы воспользоваться ботом, нужно подписаться на наш
<a href="https://t.me/mpexperts">telegram канал</a>.
'''
STOP_MESSAGE = 'Работа приложения остановлена.'
CANCEL_MESSAGE = 'Действие отменено'
HELP_MESSAGE = '''
Добро пожаловать!
Узнайте на каких позициях находится ваш товар в поиске Wildberries,
отправив запрос с указанием артикула и запросом.
'''
PARSING_START_MESSAGE = (
    'Для определения позиции артикула отправьте сообщение '
    'в формате "Артикул Поисковая фраза"\n\n'
    'Например:\n'
    '36704403 футболка женская'
)
PARSING_WAIT_MESSAGE = '''
Запрос создан! В ближайшие время вам будет отправлен результат.
'''
MEMBER_STATUSES = ('administrator', 'member', 'creator',)
PARSER_MESSAGE = '''
Артикул: {article}
Запрос: {query}
{result}
'''
ADVERT_PRODUCT_POSITION_MESSAGE = 'рекламное объявление\n'
PRODUCT_POSITION_MESSAGE = '{city} - Позиция: {position}\n'
PRODUCT_POSITION_SCHEDULE_MESSAGE = (
    '{city} - Позиция: {position}\n'
    'Рост/падение {position_difference}{position_arrow}\n'
)
PRODUCT_POSITION_NOT_FOUND_MESSAGE = '{city} - нет на первых 60 страниц\n'
POSITION_PARSER_PATTERN = r'^(\d+)\s+(.+)$'
RESIDUE_PARSER_START_MESSAGE = '''
Отправьте артикул для вывода остатков:

Например:
36704403
'''
RESIDUE_PARSER_MESSAGE = '''
Результат:
Остатки по складам
{residue_in_storehouses}

Остатки по размерам
{residual_sizes}
'''
RESIDUE_PARSER_COUNT = '{name}: {count} шт.'
RESIDUE_PARSER_PATTERN = r'^(\d+)$'
ACCEPTANCE_RATE_START_MESSAGE = '''
Выберите склад:
'''
SUBSCRIPTIONS_MESSAGE = '''
Ваши подписки:

{results}
'''
SUBSCRIBE_MESSAGE = 'Вы подписались'
UNSUBSCRIBE_MESSAGE = 'Вы отписались'
NO_SUBSCRIPTIONS_MESSAGE = 'У вас нет подписок'
ERROR_MESSAGE = 'Извините, у меня не получилось обработать запрос.'

LOG_MESSAGE_USER_SIGNED_UP = 'Пользователь {username}, чат ID {chat_id} подписался на канал и запустил бота'
LOG_MESSAGE_USER_START_PARSING = 'Пользователь {username}, чат ID {chat_id} ищет позицию товара {position}'
LOG_MESSAGE_WRONG_ARTICLE = 'Пользователь {username}, чат ID {chat_id} ввёл в парсере неверное название товара'
LOG_MESSAGE_USER_UPDATE_PARSING = 'Пользователь {username}, чат ID {chat_id} сделал запрос на обновление позиции товара {position}' # noqa
LOG_MESSAGE_USER_SUBSCRIPTION_CREATED = 'Пользователь {username}, чат ID {chat_id} создал подписку на  товар {position}'
LOG_MESSAGE_RESIDUE_REQUEST = 'Пользователь {username}, чат ID {chat_id} сделал запрос остатков товара {position}'
LOG_MESSAGE_DOWNLOAD = 'Пользователь {username}, чат ID {chat_id} сделал запрос на выгрузку результатов'
LOG_MESSAGE_UNSUBSCRIBE = 'Пользователь {username}, чат ID {chat_id} отписался от товара {position}'
