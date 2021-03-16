from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates many house rules"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        house_rules = [
            "No smoking.",
            "No parties or events.",
            "No pets/Pets allowed.",
            "No unregistered guests.",
            "No food or drink in bedrooms.",
            "No loud noise after 11 PM.",
        ]
        for a in house_rules:
            HouseRule.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("House Rules created!"))
