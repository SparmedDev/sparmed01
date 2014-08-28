from django import forms
import datetime

class OrderForm(forms.Form):
    company_name = forms.CharField(max_length=255, label="Company Name")
    company_country = forms.CharField(max_length=255, label="Company Country")
    company_address = forms.TextField(label="Company Address")
    company_postal_code = forms.IntegerField(label="Company Postal Code (if applicable)", blank=True)
    
    contact_person = forms.CharField(max_length=255, label="Contact Person Name")
    telephone = forms.IntegerField(label="Contact Telephone Number (Please include country code)")
    email = forms.EmailField(max_length=254, label="Contact Email Address")
    date = forms.DateTimeField(default=datetime.datetime.now, label="Date and time ordered")
    
    arranged_freight = forms.BooleanField(label="SparMED Arranges Freight?", default=True)
    freight_forwarder = forms.CharField(max_length=255, label="Freight Forwarder (if not through SparMed)", blank=True)
    account_no = forms.CharField(max_length=255, label="Account Number (if not freight through SparMed)", blank=True)
    
    EURO_PALLET = 'EP'
    HALF_PALLET = 'HP'
    BOX = 'BX'    
    PACKING_CHOICES = (
      (EURO_PALLET, 'Euro Pallet'),
      (HALF_PALLET, 'Half Pallet'),
      (BOX, 'Box'),
    )    
    packing_instructions = forms.CharField(max_length=2, choices=PACKING_CHOICES, default=EURO_PALLET)
    packing_remarks = forms.TextField(label="Packaging Remarks/Comments", blank=True)
    
    CARDBOARD_BOX = 'CB'
    WOODEN_FRAMES = 'WF'
    AIRCLEANER_CHOICES = (
      (CARDBOARD_BOX, 'Cardboard Box'),
      (WOODEN_FRAMES, 'Wooden Frames'),
    )    
    aircleaner_instructions = forms.CharField(max_length=2, choices=AIRCLEANER_CHOICES, default=CARDBOARD_BOX)
    
    insurance_desired = forms.BooleanField(label="Insurance is Desired? (if freight is arranged by SparMed)", default=False)
    
    documents = forms.TextField(label="Please write down if you need any documents along with your shipment", blank=True)
  
    shipping_and_invoice_same = forms.BooleanField(label="Shipping and invoice addresses are the same?", default=True)
    invoice_company_name = forms.CharField(max_length=255, label="Invoice Company Name", blank=True)
    invoice_company_address = forms.CharField(max_length=255, label="Invoice Company Address", blank=True)
    invoice_company_country = forms.CharField(max_length=255, label="Invoice Company Country", blank=True)
    invoice_company_postal_code = forms.IntegerField(label="Invoice Company Postal Code (if applicable)", blank=True)
    
    other_remarks = forms.TextField(label="Any other remarks or comments regarding this order?")