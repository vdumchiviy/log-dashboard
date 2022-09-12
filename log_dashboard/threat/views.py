from django.http import JsonResponse
from .models import ThreatCategory, Threat


def show_threat_categories(request):
    categories = ThreatCategory.objects.all()
    data = dict()
    for cat in categories:
        data[cat.id] = cat.kind

    return JsonResponse(data)


def show_threats(request):
    threats = Threat.objects.all()
    data = dict()
    for threat in threats:
        data[threat.id] = f"{threat.category} at {threat.dt} on {threat.location}"

    return JsonResponse(data)
