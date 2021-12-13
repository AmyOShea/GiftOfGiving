from django import forms
from .widgets import CustomClearableFileInput
from .models import Gift

class GiftForm (forms.ModelForm):

    class Meta:
        model = Gift
        fields = ['description', 'estimated_price', 'age_range', 'needed', 'received', 'image']
        # specify fields
    
    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'description': 'Description',
            'estimated_price': 'Estimated price',
            'age_range': 'Age range',
            'received': 'Mark Received',
            'needed': 'Mark no longer needed',
            'image': 'Upload gift photo',
        }

        for field in self.fields:
            self.fields['description'].widget.attrs['class'] = 'field-styling'
            self.fields['estimated_price'].widget.attrs['class'] = 'field-styling'
            self.fields['age_range'].widget.attrs['class'] = 'field-styling'
            self.fields['received'].widget.attrs['class'] = 'field-styling'
            self.fields['needed'].widget.attrs['class'] = 'field-styling'
            self.fields['image'].widget.attrs['class'] = 'field-styling'
