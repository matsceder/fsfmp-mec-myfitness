from django.shortcuts import render


def about(request):
    """ A view to return about page and scroll to wanted section """
    context = {}
    if 'scroll' in request.GET:
        scroll = request.GET['scroll']
        context = {
            'scroll': scroll,
        }

    return render(request, 'about/about.html', context)
