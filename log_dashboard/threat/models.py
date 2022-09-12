from django.db import models

# Create your models here.


class ThreatCategory(models.Model):
    class ThreatCategoryKinds(models.TextChoices):
        ATTACK = "ATTACK"
        THREAT = "THREAT"
        FALSEALARM = "FALSEALARM"
        UNKNOWN = "UNKNOWN"

    kind = models.CharField(
        verbose_name="Category Kind",
        max_length=10,
        null=True,
        blank=True,
        choices=ThreatCategoryKinds.choices,
        default=ThreatCategoryKinds.UNKNOWN)

    class Meta:
        verbose_name = "Threat Category"
        verbose_name_plural = "Threat Categories"

    def __str__(self) -> str:
        return str(self.kind)


class Threat(models.Model):
    category = models.ForeignKey(
        verbose_name="Category of the Threat",
        to=ThreatCategory,
        on_delete=models.PROTECT
    )
    dt = models.DateTimeField(
        verbose_name="DateTime occured",
        auto_now_add=True,
        db_index=True
    )
    location = models.CharField(
        max_length=100,
        verbose_name="Location"
    )

    class Meta:
        verbose_name = "Threat"
        verbose_name_plural = "Threats"
        ordering = ["-dt", "location"]

    def __str__(self) -> str:
        return f"{self.pk}: {self.category} at {self.dt} on {self.location}"
