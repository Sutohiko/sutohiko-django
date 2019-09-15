from django.shortcuts import render, render_to_response


def startup(request):
    menu = ['Главная', 'Заметки', 'Портфолио', 'Контакты']

    return render(request, 'base/index.html', context={
        'menu': menu,
    })


def robots(request):
    return render_to_response('robots.txt', content_type='text/plain')
