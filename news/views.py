from django.shortcuts import render


def news_list(request):
    meta_title = 'News - davarch.ru'
    meta_description = 'News Meta Description'
    heading_title = 'H1 - News'
    content = 'News description'
    menu = ['Главная', 'Заметки', 'Портфолио', 'Контакты']

    return render(request, 'news/index.html', context={
        'meta_title': meta_title,
        'meta_description': meta_description,
        'heading_title': heading_title,
        'content': content,
        'menu': menu
    })
