#python manage.py import_network "C:\Users\ABC\Downloads\Network-2026-09-01.xlsx"
from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Network # ← عدّل اسم الـ app لو مختلف
from django.db import transaction



class Command(BaseCommand):
    help = "Import Excel file into Network model"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to Excel (.xlsx) file")

    @transaction.atomic
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        self.stdout.write(self.style.WARNING(f"Reading Excel file: {file_path} ..."))
        df = pd.read_excel(file_path).fillna('N/A')

        required_columns = [
            'governorate', 'governorate_ar',
            'area', 'area_ar',
            'type', 'type_ar',
            'speciality', 'speciality_ar',
            'provider', 'provider_ar',
            'address', 'address_ar',
            'phone', 'website', 'email', 'notes','discount'
        ]

        # Check missing columns
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            self.stdout.write(self.style.ERROR(f"Missing columns: {missing}"))
            return

        records = []
        for _, row in df.iterrows():
            records.append(Network(
                governorate=row['governorate'],
                governorate_ar=row['governorate_ar'],

                area=row['area'],
                area_ar=row['area_ar'],

                type=row['type'],
                type_ar=row['type_ar'],

                speciality=row['speciality'],
                speciality_ar=row['speciality_ar'],

                provider=row['provider'],
                provider_ar=row['provider_ar'],

                discount=row['discount'] if row['discount'] != 'N/A' else None,

                address=row['address'],
                address_ar=row['address_ar'],

                phone=row['phone'],
                website=row['website'] if row['website'] != 'N/A' else None,
                email=row['email'] if row['email'] != 'N/A' else None,
                notes=row['notes'] if row['notes'] != 'N/A' else None,
            ))

        # Bulk insert for speed
        Network.objects.bulk_create(records, batch_size=500)

        self.stdout.write(self.style.SUCCESS(f"Imported {len(records)} records successfully!"))
