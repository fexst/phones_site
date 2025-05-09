import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone(id_phone=phone.get('id'), name=phone.get('name'), image=phone.get('image'),
                  price=int(phone.get('price')), release_date=phone.get('release_date'),
                  lte_exists=phone.get('lte_exists'), slug=slugify(phone.get('name'))).save()
