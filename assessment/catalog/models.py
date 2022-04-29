from django.db import models

# Create your models here.
class Catalog(models.Model):
    object_id = models.CharField(max_length=255, null=False, unique=True)
    data = models.JsonField()

    class Meta:
        db_table = 'catalog'
        app_label = 'catalog'
