from cart.models import Cart
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('sparmed.cleancarts')

class Command(BaseCommand):  
    help = 'Cleans old cart (older than 7 days) instances from the database'
    
    def handle(self, *args, **options):
        Cart.objects.filter(creation_date__gte=datetime.now()-timedelta(days=7)).delete()
        logger.info("--> Cleared all carts older than 7 days from database!")
        self.stdout.write("--> Cleared all carts older than 7 days from database!")