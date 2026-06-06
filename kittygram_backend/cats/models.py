from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
User = get_user_model()
def validate_birth_year(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError(
            f'Год рождения не может быть больше текущего ({current_year}).'
        )
class Achievement(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField(validators=[validate_birth_year])
    owner = models.ForeignKey(
        User,
        related_name='cats',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat',
        blank=True
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None,
        blank=True
    )
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.achievement} {self.cat}'