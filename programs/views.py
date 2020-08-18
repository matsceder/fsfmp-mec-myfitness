from django.shortcuts import render, get_object_or_404
from .models import Programs, Category


def programs(request):
    """ A view to display the different workout and diet-programs """
    categories = Category.objects.all()
    programs = Programs.objects.all()

    template = 'programs/programs.html'
    context = {
        'categories': categories,
        'programs': programs,
    }

    return render(request, template, context)


def program(request, program_id):
    """ A view to display the different workout and diet-programs """
    program = get_object_or_404(Programs, pk=program_id)

    template = 'programs/program_detail.html'
    context = {
        'program': program,
    }

    return render(request, template, context)
