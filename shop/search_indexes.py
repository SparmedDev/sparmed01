from django.utils import timezone
from haystack import indexes
from shop.models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    
    name = indexes.CharField(model_attr='name')
    long_name = indexes.CharField(model_attr='long_name', null=True)
    product_id = indexes.CharField(model_attr='product_id', boost=1.25)    
    added = indexes.DateTimeField(model_attr='added')
    
    product_id_auto = indexes.EdgeNgramField(model_attr='product_id', boost=1.25)
    long_name_auto = indexes.EdgeNgramField(model_attr='long_name', null=True)
    
    def get_model(self): 
        return Product 
      
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Product.objects.filter(added__lte=timezone.now())      