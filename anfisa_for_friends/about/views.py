from django.shortcuts import render


def about(request):
    template = 'about/description.html'
    return render(request, template)
