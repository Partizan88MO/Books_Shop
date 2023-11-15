from django import forms
from catalog.models import Book
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'user',
            'summ',
            'order_book',
            'currency'
        ]
    def update_obj(self, pk):
        user = self.cleaned_data.get("user")
        summ = self.cleaned_data.get("summ")
        order_book = self.cleaned_data.get("order_book")
        currency = self.cleaned_data.get("currency")
        models.Order.objects.filter(pk=pk).update(
        user = user,
        summ = summ,
        order_book = order_book,
        currency = currency
        )
    def save_obj(self):
        user = self.cleaned_data.get("user")
        summ = self.cleaned_data.get("summ")
        order_book = self.cleaned_data.get("order_book")
        currency = self.cleaned_data.get("currency")
        obj = models.Order.objects.create(
            user = user,
            summ = summ,
            order_book = order_book,
            currency = currency
        )
        return obj