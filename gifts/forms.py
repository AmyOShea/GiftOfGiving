from django import forms
from .widgets import CustomClearableFileInput
from .models import Gift

class GiftForm (forms.ModelForm):

    class Meta:
        model = Gift
        fields = '__all__'
    
    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'estimated_price': 'Estimated price',
            'age_range': 'Age range',
            'image': 'Upload gift photo',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
            self.fields['estimated_price'].widget.attrs['class'] = 'field-styling'
            self.fields['age_range'].widget.attrs['class'] = 'field-styling'
            self.fields['image'].widget.attrs['class'] = 'field-styling'
