from django.http import HttpResponseNotFound
from django.template import loader


def custom_404(request, exception):
    template = loader.get_template('404.html')
    context = {
        'path': request.path,
    }
    return HttpResponseNotFound(template.render(context, request))
