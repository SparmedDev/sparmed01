from django.utils import timezone
import models
from django.core.cache import cache

CART_ID = 'CART-ID'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart:
    def __init__(self, request):
        cart_id = cache.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
            
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item
            
    def get_item_list(self):  
        return self.cart.item_set.all()

    def new(self, request):
        cart = models.Cart(creation_date=timezone.now())
        cart.save()
        cache.set(CART_ID, cart.id)
        return cart

    def add(self, product, quantity=1):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.product = product
            item.quantity = quantity
            item.save()
        else: #ItemAlreadyExists
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()
    
    def set_product_quantity(self, product, quantity):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.set_quantity(quantity)

    def update(self, product, quantity):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
            
    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.quantity
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
            
    def delete(self):
      self.clear()

      cart_id = cache.get(CART_ID)
      if cart_id:
          try:
              models.Cart.objects.get(id=cart_id).delete()
          except models.Cart.DoesNotExist: 
              pass
            
          cache.delete(cart_id)