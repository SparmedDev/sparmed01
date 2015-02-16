import datetime
from haystack import indexes
from shop.models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    
    name = indexes.CharField(model_attr='name')
    long_name = indexes.CharField(model_attr='long_name')
    product_id = indexes.CharField(model_attr='product_id', boost=1.25)    

    product_id_auto = indexes.EdgeNgramField(model_attr='product_id', boost=1.25)
    long_name_auto = indexes.EdgeNgramField(model_attr='long_name')
    description_auto = indexes.EdgeNgramField(model_attr='description')
    
    def get_model(self): 
        return Product 