from django.db import models
from threat.models import Threat


class Log(models.Model):
    server_name = models.CharField(max_length=100, verbose_name="Server")
    dt = models.DateTimeField(auto_now=True, verbose_name="DT log record")
    threat = models.ForeignKey(
        to=Threat,
        related_name="logs",
        verbose_name="Threat",
        db_index=True,
        on_delete=models.PROTECT
    )
    comment = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
        ordering = ["-dt", "server_name"]

    def __str__(self) -> str:
        return f"{self.pk}: {self.server_name} at {self.dt} for {self.threat}"
