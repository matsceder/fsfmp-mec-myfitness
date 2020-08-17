from django.shortcuts import render
from .models import Programs


def programs(request):
    """ A view to display the different workout and diet-programs """
    template = 'programs/programs.html'
    context = {

    }

    return render(request, template, context)
