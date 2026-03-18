from django.forms import ModelForm

from mi_aplicacion.models import Escuela, Maestro
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]

class MaestroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaestroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper = Layout(
            Row(
                Column(Field('nombre'), css_class='form-group col-md-6 mb-0'),
                Column(Field('escuela'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(Field('sexo'), css_class='form-group col-md-6 mb-0'),
                Column(Field('fecha_nacimiento'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit','guardar')
        )

    class Meta:
        model = Maestro
        fields = ["nombre", "escuela", "sexo", "fecha_nacimiento"]