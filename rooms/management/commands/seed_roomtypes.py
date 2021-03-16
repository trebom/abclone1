from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates house rules"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        roomtypes = [
            "Hotel Room",
            "Shared Room",
            "Entire Room",
            "Private Room",
        ]
        for rt in roomtypes:
            RoomType.objects.create(name=rt)
        self.stdout.write(self.style.SUCCESS("RoomTypes created!"))
