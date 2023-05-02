#
# register = template.Library()
#
# # добавляем возможность выбирать
# CENSOR_WORDS = ['редиска', 'обезьяна', 'обезьяны']


#
#
# # Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# # что это именно фильтр для шаблонов, а не простая функция.
# @register.filter()
# def censor(value):
#     value = list(value)
#     for i in value:
#         if i in CENSOR_WORDS:
#             i = i.replace('*****')
#             i += i
#
#     return i.join(',', '')
#
# #     # Возвращаемое функцией значение подставится в шаблон.
# censor('fghhhd ddfd обезьяна jkjkjkj')

