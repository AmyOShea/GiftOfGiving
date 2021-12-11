from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Clearable file input
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Gift Photo')
    input_text = _('')
    template_name = 'gifts/custom-widget-templates/custom-clearable-file-input.html'