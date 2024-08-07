from . models import Car, Review
from django import forms

class inventoryForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    make = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    carModel = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'content']
    
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )