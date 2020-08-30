from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Programs, Category
from .forms import ProgramsForm


def programs(request):
    """ A view to display the different workout and diet-programs """
    categories = Category.objects.all()
    programs = Programs.objects.all()
    current_category = None

    if request.GET:
        if 'category' in request.GET:
            current_category = request.GET['category'].split(',')
            programs = programs.filter(category__name__in=current_category)
            current_category = Category.objects.filter(
                name__in=current_category)

    template = 'programs/programs.html'
    context = {
        'categories': categories,
        'programs': programs,
        'current_category': current_category,
        'on_programs_page': True,
    }

    return render(request, template, context)


def program(request, program_id):
    """ A view to display the different workout and diet-programs """
    program = get_object_or_404(Programs, pk=program_id)

    template = 'programs/program_detail.html'
    context = {
        'program': program,
        'on_programs_page': True,
    }

    return render(request, template, context)


@login_required
def add_program(request):
    """ Adding new Program post """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    if request.method == 'POST':
        programs_form = ProgramsForm(request.POST, request.FILES)
        if programs_form.is_valid():
            programs_form.save()
            messages.success(request, "Program post was saved successfully")
            return redirect(reverse('programs'))
        else:
            messages.error(
                request, "Failed to save post. Make sure it it's valid"
            )
    else:
        programs_form = ProgramsForm()

    template = 'programs/add_program.html'
    context = {
        'programs_form': programs_form,
    }

    return render(request, template, context)


@login_required
def edit_program(request, program_id):
    """ Adding new Program post """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    program = get_object_or_404(Programs, pk=program_id)
    if request.method == 'POST':
        programs_form = ProgramsForm(
            request.POST, request.FILES, instance=program
        )
        if programs_form.is_valid():
            programs_form.save()
            messages.success(request, "Post successfully updated")
            return redirect(reverse('program', args=[program.id]))
        else:
            messages.error(
                request, "Failed to save post. Make sure form is valid"
            )
    else:
        programs_form = ProgramsForm(instance=program)
        messages.info(
            request,
            f"You're now making changes to {program.title} by {program.author}"
        )

    template = 'programs/edit_program.html'
    context = {
        'program': program,
        'programs_form': programs_form,
    }

    return render(request, template, context)


@login_required
def delete_program(request, program_id):
    """ Deletes a program post """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    program = get_object_or_404(Programs, pk=program_id)
    program.delete()
    messages.success(request, 'Program post deleted!')
    return redirect(reverse('programs'))
