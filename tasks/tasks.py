from cart.models import Cart
from time import datetime, deltatime
  
@app.task
def clean_carts():
    Cart.objects.filter(creation_date__gte=datetime.now()-timedelta(days=7)).delete()
    return True
