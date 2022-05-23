from django import template

from consultants.models import Consultant

register = template.Library()

@register.inclusion_tag('includes/controls.html')
def filterbar_data ():
  spheres = Consultant.objects.all()
  
  count_all = Consultant.objects.count()
  count_male = Consultant.objects.filter(gender='male').count()
  count_female = Consultant.objects.filter(gender='female').count()
  count_international = Consultant.objects.filter(type='international').count()
  count_local = Consultant.objects.filter(type='local').count()



  return {
    'all': count_all,
    'male' : count_male,
    'female' : count_female,
    'international': count_international,
    'local': count_local
  }