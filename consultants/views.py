from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Consultant


# Create your views here.
def consultant_list(request):
    consultants = get_list_or_404(Consultant)
    return render(request, 'consultants.html', {'cs': consultants })


def consultant_item(request, id):
    consultant = get_object_or_404(Consultant, id=id)
    return render(request, 'consultant.html', {'c': consultant })


def consultant_search(request):
    pass