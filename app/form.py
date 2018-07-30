from django import forms as frm

class ProductForm(frm.Form):
	name=frm.CharField(required=True,widget=frm.TextInput())
	barcode=frm.CharField(required=True,widget=frm.TextInput())
