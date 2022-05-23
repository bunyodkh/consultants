import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from organizations.models import Organization

class Consultant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    image = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Personal image of the consultant')
    fullname = models.CharField(_('Full name'), max_length=100, blank=False, null=False, unique=True, help_text='Full name of the consultant. If similar with other one add middle name')
    age = models.PositiveIntegerField(_('Age'), default=0, blank=False, null=False, help_text='Current age of the consultant')
    email = models.CharField(_('Email'), max_length=100, blank=True, null=True, unique=True, help_text='Active email of the consultant')
    phone = models.CharField(_('Phone'), max_length=100, blank=True, null=True, unique=True, help_text='Active phone number of the consultant')
    
    experience = models.TextField(_('Experience'), blank=True, null=True, help_text='Brief information on the previous and current positions of the consultant')
    education = models.TextField(_('Education'), blank=True, null=True, help_text='Brief information on the academic background of the consultant')
    
    sphere = models.ForeignKey('Sphere', on_delete=models.CASCADE, blank=True, null=True, help_text='Professional sphere')
    occupation = models.ForeignKey('Occupation', on_delete=models.CASCADE, blank=True, null=True, help_text='Current professional occupation')
    competences = models.ManyToManyField('Competence', verbose_name='Competences', blank=True)
    languages = models.ManyToManyField('Language', verbose_name='Languages', blank=True)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True, help_text='Current affiliated organization.')

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(_('Gender'), max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    TYPE_CHOICES = (
        ('international', 'International'),
        ('local', 'Local'),
    )
    type = models.CharField(_('Type'), max_length=20, choices=TYPE_CHOICES, help_text='International or local consultant?',  blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    verified = models.BooleanField(_('Verified'), default=False, help_text='Check if the given information is verified by the consultant.', null=True, blank=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self, *args, **kwargs):
        return reverse('consultants:consultant',  args=[self.id])
    
    def display_languages(self):
        return ', '.join(lang.title for lang in self.languages.all()[:3])


    class Meta:
        ordering = ['fullname']
        verbose_name = 'Consultant'
        verbose_name_plural = 'Consultants'


class Sphere(models.Model):
    title = models.CharField(_('Sphere'), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Sphere'
        verbose_name_plural = 'Spheres'


class Occupation(models.Model):
    title = models.CharField(_('Occupation'), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Occupation'
        verbose_name_plural = 'Occupations'


class LanguageLevel(models.Model):
    title = models.CharField(_('Level'), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'


class Language(models.Model):
    title = models.CharField(_('Language'), max_length=100, blank=False, null=False)
    level = models.ForeignKey('LanguageLevel', verbose_name='Level', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - ({self.level})' 

    class Meta:
        ordering = ['title']
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'



class Competence(models.Model):
    title = models.CharField(_('Competence'), max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'
