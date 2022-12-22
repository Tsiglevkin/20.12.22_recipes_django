from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def get_omlet(reqeust):
    """"""
    how_many = int(reqeust.GET.get('servings', 1))
    context = {'recipe': DATA['omlet']}
    for ingr, quan in context['recipe'].items():
        context['recipe'][ingr] = quan * how_many

    return render(reqeust, 'calculator/index.html', context=context)


def get_pasta(reqeust):
    """"""
    how_many = int(reqeust.GET.get('servings', 1))
    context = {'recipe': DATA['pasta']}
    for ingr, quan in context['recipe'].items():
        context['recipe'][ingr] = quan * how_many

    return render(reqeust, 'calculator/index.html', context=context)


def get_buter(reqeust):
    """"""
    how_many = int(reqeust.GET.get('servings', 1))
    context = {'recipe': DATA['buter']}
    for ingr, quan in context['recipe'].items():
        context['recipe'][ingr] = quan * how_many

    return render(reqeust, 'calculator/index.html', context=context)



