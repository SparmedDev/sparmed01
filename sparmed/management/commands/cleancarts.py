from cart.models import Cart
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):  
    help = 'Cleans old cart instances from the database'
    
    def handle(self, *args, **options):
        Cart.objects.filter(creation_date__gte=datetime.now()-timedelta(days=7)).delete()
        self.stdout.write("--> Cleared all carts older than 7 days from database!")