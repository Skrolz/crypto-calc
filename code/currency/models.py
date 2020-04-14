from django.db import models

class CurrencyManager(models.Manager):
    def get_by_natural_key(self, abbreviation):
        return self.get(abbreviation=abbreviation)

class Currency(models.Model):

    # abbreviation
    abbreviation = models.CharField(
        blank=False,
        max_length=10,
        null=False,
        unique=True,
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

    objects = CurrencyManager()

    def natural_key(self):
        return [self.abbreviation]

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.abbreviation