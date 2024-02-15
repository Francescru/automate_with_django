from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
  help = "Greets the user"

  def add_arguments(self, parser):
    parser.add_argument("name", type=str, help="specifies username")

  def handle(self, *args, **kwargs):
    name = kwargs["name"]
    greeting = f"Hi {name} you sanavabitch"
    self.stdout.write(self.style.SUCCESS(greeting))
    # print(kwargs)