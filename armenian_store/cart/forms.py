from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

def quantity_validation(value):
    return value > 0

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="",
                                widget=forms.NumberInput(attrs={"id": 'cart-amount', "value": 1}),
                                max_value=99,
                                min_value=1,
                                validators=[quantity_validation])
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)