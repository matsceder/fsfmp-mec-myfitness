from django.shortcuts import render
from .models import Programs


def programs(request):
    """ A view to display the different workout and diet-programs """
    programs = Programs.objects.all()

    template = 'programs/programs.html'
    context = {
        'programs': programs,
    }

    return render(request, template, context)
