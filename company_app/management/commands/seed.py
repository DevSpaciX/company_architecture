import random

from faker import Faker
from django.core.management.base import BaseCommand
from company_app.models import Employee

fake = Faker()

from django.db import transaction


class Command(BaseCommand):
    help = "Seed database with initial data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, help="Indicates the number of employees to be seeded"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        number = options["number"] or 20

        for _ in range(number):
            employee = Employee(
                name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_this_century(),
                email=fake.email(),
            )
            employee.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} employees")
        )
