from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

city = (
    (1, 'Ndjamena'),
    (2, 'Moundou'),
    (3,'abeche'),
)

class Data(models.Model):
    surface =  models.PositiveBigIntegerField(null=True)
    prix_mettre =  models.PositiveBigIntegerField(null=True)
    variation =  models.PositiveBigIntegerField(null=True)
    # prix_location =  models.PositiveBigIntegerField(null=True)
    ville = models.PositiveBigIntegerField(choices=city, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('perso2_model.joblib')
        self.predictions = ml_model.predict([[self.surface, self.ville, self.prix_mettre, self.variation]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name