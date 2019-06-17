from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


    
# Create your models here.
class Post(models.Model):
    SOORT_REPTIEL = (
        ('X', 'Kies soort reptiel'),
	    ('H', 'Hagedis'),
        ('S', 'Slang'),
        ('D', 'Schildpad'),
        ('K', 'Krokodil'),
    )
    
    
    image = models.ImageField(upload_to="images", null=True, blank=True)
    title = models.CharField(max_length=200)
    naamdier = models.TextField()
    latijnsenaam = models.TextField()
    uiterlijk = models.TextField()
    kortebeschrijving = models.TextField()
    verspreidingwild = models.TextField()
    geslachtsonderscheid = models.TextField()
    huisvesting = models.TextField()
    inrichting = models.TextField()
    voeding = models.TextField()
    voortplanting = models.TextField()
    draagtijdincubatiegrootbrengen = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    soort=models.CharField(max_length=1, default= 'X', choices=SOORT_REPTIEL)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT) 

    def __str__(self):
        return self.title

