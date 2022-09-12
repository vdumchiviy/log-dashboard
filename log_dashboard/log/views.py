from .models import Log
from django.http import JsonResponse


def show_all_logs(request):
    logs = Log.objects.all()
    data = dict()
    for log in logs:
        data[log.id] = {
            "server": log.server_name,
            "dt": log.dt,
            "threat": log.threat.category.kind,
            "comment": log.comment
        }

    return JsonResponse(data)
