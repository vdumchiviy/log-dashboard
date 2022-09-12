from django.forms import ModelForm
from threat.models import Threat, ThreatCategory
from log.models import Log


class LogSearchForm(ModelForm):
    class Meta:
        model = Log
        fields = ('id', 'server_name', 'comment', 'category')
