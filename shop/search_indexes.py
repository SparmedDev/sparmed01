import datetime
from haystack import indexes
from shop.models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    
    name = indexes.CharField(model_attr='name')
    product_id = indexes.CharField(model_attr='product_id', boost=1.25)    
    #description = indexes.CharField(model_attr='description') 
    
    #name_auto = indexes.EdgeNgramField(model_attr='name')
    product_id_auto = indexes.EdgeNgramField(model_attr='product_id', boost=1.25)
    description_auto = indexes.EdgeNgramField(model_attr='description')
    
    def get_model(self): 
        return Product 