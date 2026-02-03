from django.core.management.base import BaseCommand
from front_office.models import State, City

KERALA_CITIES = [
    "Thiruvananthapuram",
    "Kollam",
    "Pathanamthitta",
    "Alappuzha",
    "Kottayam",
    "Idukki",
    "Ernakulam",
    "Thrissur",
    "Palakkad",
    "Malappuram",
    "Kozhikode",
    "Wayanad",
    "Kannur",
    "Kasaragod",
]

class Command(BaseCommand):
    help = "Insert Kerala cities into City model"

    def handle(self, *args, **kwargs):
        try:
            state = State.objects.get(name="Kerala", country__name="India")
        except State.DoesNotExist:
            self.stdout.write(self.style.ERROR("Kerala state not found. Run state import first."))
            return

        for city_name in KERALA_CITIES:
            city, created = City.objects.get_or_create(state=state, name=city_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added city: {city_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {city_name}"))
