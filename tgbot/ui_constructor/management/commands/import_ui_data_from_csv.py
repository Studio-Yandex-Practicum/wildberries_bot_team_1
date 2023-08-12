from csv import DictReader
from ui_constructor.models import ButtonConstructor
from sys import exit

from django.core.management import BaseCommand


CSV_TABLES = {
    'ButtonConstructor': DictReader(
        open('../data/buttons.csv', encoding='utf-8')
    ),
}


def delete_everything():
    ButtonConstructor.objects.all().delete()


def print_attention():
    print(
        'Внимание! Будут сброшены в значения по умолчанию '
        'тексты всех элементов управления бота. '
        'Хотите продолжить ? [Y / N]: '
    )
    answer = input()
    if answer.upper() != 'Y':
        exit()


print_attention()
delete_everything()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for value in CSV_TABLES['ButtonConstructor']:
            ButtonConstructor.objects.get_or_create(
                pk=value['id'],
                ui_control_id=value['ui_control_id'],
                button_description=value['button_description'],
                default_text=value['default_text'],
            )
        print('Данные по умолчанию добавлены в базу данных')
