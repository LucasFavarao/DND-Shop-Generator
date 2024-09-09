import csv
from django.core.management.base import BaseCommand
from shopApp.models import Dnditem
from preplanned import convertMoneyType

class Command(BaseCommand):
    help= 'Import csv data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self,*args,**kwargs):
        csv_file_path=kwargs['csv_file']

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            model_instances = [
                Dnditem(
                    item_name=row["item_name"],
                    price=convertMoneyType(row["price"]),
                    item_weight=row["item_weight"],
                    shop_vendor=row["shop_vendor"],
                    rarity=row["rarity"],
                )
                for row in reader
            ]
            Dnditem.objects.bulk_create(model_instances)
            self.stdout.write(('Succesfully import the CSV file'))