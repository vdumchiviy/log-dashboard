from http.client import HTTPResponse
from .models import Log
from threat.models import Threat, ThreatCategory
from django.http import JsonResponse, HttpResponse
from django.db.models import Count, F, Value, Window
from django.db.models.functions import FirstValue, TruncDate


def show_all_logs(request):
    logs = Log.objects.all()
    data = ""
    data += f"total log records: {len(logs)}<br>"

    threats = Threat.objects.all()
    data += f"<br>total threats: {len(threats)}<br>"

    data += f"<br>total threat categories: {len(threats)}<br>"
    cat_count = Threat.objects.values('category__kind').annotate(
        category_count=Count('category')).order_by()
    for cat_cnt in cat_count:
        data += f"Threat type: {cat_cnt['category__kind']} - {cat_cnt['category_count']} times<BR>"

    data += "<br><br>Threats by servers:"
    by_servers = Log.objects.values_list(
        "server_name", "threat__category__kind"
    ).order_by("server_name").all().distinct()
    for by_s in by_servers:
        data += f"<br>{by_s[0]} - {by_s[1]}"

    data += "<br><br>Logs:"
    for log in logs:
        data += "<br>" + str(log)

    return HttpResponse(data)
