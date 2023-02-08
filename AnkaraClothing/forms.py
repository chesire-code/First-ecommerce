from django import forms
from .models import Subscribers, Message

class SearchForm(forms.Form):
  query = forms.CharField(label='Search', max_length=100, required=False)
  maxprice = forms.IntegerField(label='max price', required=False)


class SubscribeForm(forms.Form):
  mail = forms.CharField(label='Subscribe', max_length=100)
