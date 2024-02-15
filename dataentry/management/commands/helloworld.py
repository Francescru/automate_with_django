from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = "Prints Hello World"

  def handle(self, *args, **kwargs):
    self.stdout.write('Hello World')


#source env/scripts/activate
#python manage.py runserver
#python manage.py migrate
    #user absota
    #pwd from