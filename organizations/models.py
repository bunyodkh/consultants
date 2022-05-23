import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Personal image of the consultant')
    title = models.CharField(_('Title'), max_length=300, blank=False, null=False, unique=True, help_text='Title of the organization.')
    type = models.ForeignKey('OrgType', on_delete=models.CASCADE, blank=True, null=True, help_text='Type of the organization')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'


class OrgType(models.Model):
    title = models.CharField(_('Organization type description'), max_length=300, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'OrgType'
        verbose_name_plural = 'OrgTypes'

    def __str__(self):
        return self.title

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('organizations:organization',  args=[self.id])