from django import forms
import datetime

class OrderForm(forms.Form):
    company_name = forms.CharField(max_length=255, label="Company Name")
    company_country = forms.CharField(max_length=255, label="Company Country")
    company_address = forms.CharField(widget=forms.Textarea, label="Company Address")
    company_postal_code = forms.IntegerField(label="Company Postal Code")
    
    contact_person = forms.CharField(max_length=255, label="Contact Person Name")
    telephone = forms.IntegerField(label="Contact Telephone Number (Please include country code)")
    email = forms.EmailField(max_length=254, label="Contact Email Address")
    date = forms.DateTimeField(initial=datetime.datetime.now, label="Date and time ordered")
    
    arranged_freight = forms.BooleanField(label="SparMED Arranges Freight?", initial=True)
    freight_forwarder = forms.CharField(max_length=255, label="Freight Forwarder (if not through SparMed)", required=False)
    account_no = forms.CharField(max_length=255, label="Account Number (if not freight through SparMed)", required=False)
    
    EURO_PALLET = 'EP'
    HALF_PALLET = 'HP'
    BOX = 'BX'    
    PACKING_CHOICES = (
      (EURO_PALLET, 'Euro Pallet'),
      (HALF_PALLET, 'Half Pallet'),
      (BOX, 'Box'),
    )    
    packing_instructions = forms.CharField(max_length=2, widget=forms.Select(choices=PACKING_CHOICES))
    packing_remarks = forms.CharField(widget=forms.Textarea, label="Packaging Remarks/Comments", required=False)
    
    CARDBOARD_BOX = 'CB'
    WOODEN_FRAMES = 'WF'
    AIRCLEANER_CHOICES = (
      (CARDBOARD_BOX, 'Cardboard Box'),
      (WOODEN_FRAMES, 'Wooden Frames'),
    )    
    aircleaner_instructions = forms.CharField(max_length=2, widget=forms.Select(choices=AIRCLEANER_CHOICES))
    
    insurance_desired = forms.BooleanField(label="Insurance is Desired? (if freight is arranged by SparMed)", initial=False)
    
    documents = forms.CharField(widget=forms.Textarea, label="Please write down if you need any documents along with your shipment", required=False)
  
    shipping_and_invoice_same = forms.BooleanField(label="Shipping and invoice addresses are the same?", initial=True)
    invoice_company_name = forms.CharField(max_length=255, label="Invoice Company Name", required=False)
    invoice_company_address = forms.CharField(max_length=255, label="Invoice Company Address", required=False)
    invoice_company_country = forms.CharField(max_length=255, label="Invoice Company Country", required=False)
    invoice_company_postal_code = forms.IntegerField(label="Invoice Company Postal Code", required=False)
    
    other_remarks = forms.CharField(widget=forms.Textarea, label="Any other remarks or comments regarding this order?")