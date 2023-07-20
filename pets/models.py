from django.db import models

# Create your models here.
class PetSex(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"


class Pet(models.Model):
  
    name = models.CharField(max_length=50,null=False)
    age = models.IntegerField()
    weight= models.FloatField()
    sex= models.CharField(max_length=20,choices=PetSex.choices,default=PetSex.DEFAULT)
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.PROTECT,
        related_name="pets",
    )
    traits = models.ManyToManyField(
       "traits.Trait",
        related_name="pets",
    )

    

# string, tamanho máximo 20, somente dentre as opções Male, Female e Not Informed. 
# Valor padrão sendo Not Informed.

