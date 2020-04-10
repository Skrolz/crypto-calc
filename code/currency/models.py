from django.db import models


class Currency(models.Model):

    # abbreviation
    abbreviation = models.CharField(
        blank=False,
        max_length=10,
        null=False,
    )

    # comments
    comments = models.TextField(
        blank=True,
        null=True,
    )

    # name
    name = models.CharField(
        blank=False,
        max_length=100,
        null=False,
    )

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.abbreviation