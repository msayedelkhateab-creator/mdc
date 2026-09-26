# python manage.py import_emfa "C:\Users\ABC\Downloads\Networkemfa-2026-09-26.xlsx"

from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from app.models import Networkemfa  # ← عدّل اسم الـ app لو مختلف
from django.db import transaction


class Command(BaseCommand):
    help = "Import Excel file into Networkemfa model"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to Excel (.xlsx) file")

    @transaction.atomic
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        self.stdout.write(self.style.WARNING(f"Reading Excel file: {file_path} ..."))

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            raise CommandError(f"Could not read Excel file: {e}")

        df.columns = [str(c).strip() for c in df.columns]
        df = df.fillna('')

        # أعمدة الإكسل الجديد = نفس أسماء حقول المودل بالظبط
        required_columns = [
            'country', 'country_ar',
            'city', 'city_ar',
            'type', 'type_ar',
            'speciality', 'speciality_ar',
            'provider', 'provider_ar',
            'address', 'address_ar',
            'phone', 'mobile', 'email', 'website', 'notes',
        ]

        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            self.stdout.write(self.style.ERROR(f"Missing columns: {missing}"))
            self.stdout.write(self.style.ERROR(f"Found columns: {list(df.columns)}"))
            return

        def clean(value):
            value = str(value).strip()
            return value if value else None

        records = []
        skipped = 0

        for idx, row in df.iterrows():
            provider = clean(row['provider'])

            if not provider:
                skipped += 1
                continue

            records.append(Networkemfa(
                country=clean(row['country']) or 'Egypt',
                country_ar=clean(row['country_ar']),

                city=clean(row['city']),
                city_ar=clean(row['city_ar']),

                type=clean(row['type']),
                type_ar=clean(row['type_ar']),

                speciality=clean(row['speciality']),
                speciality_ar=clean(row['speciality_ar']),

                provider=provider,
                provider_ar=clean(row['provider_ar']),

                address=clean(row['address']),
                address_ar=clean(row['address_ar']),

                phone=clean(row['phone']),
                mobile=clean(row['mobile']),
                email=clean(row['email']),
                website=clean(row['website']),
                notes=clean(row['notes']),
            ))

        Networkemfa.objects.bulk_create(records, batch_size=500)

        self.stdout.write(self.style.SUCCESS(
            f"Imported {len(records)} records successfully! (skipped {skipped} empty rows)"
        ))