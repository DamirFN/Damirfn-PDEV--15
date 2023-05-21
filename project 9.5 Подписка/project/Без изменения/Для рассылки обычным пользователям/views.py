# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # импортируем для удаления новостей
from .models import Product, NewsPortal
from datetime import datetime
from .filters import ProductFilter, NewsFilter
from .forms import ProductForm, NewForm  # для создания продуктов через функцию forms.py
from django.contrib.auth.mixins import LoginRequiredMixin        # авторизация пользователя
from django.contrib.auth.mixins import PermissionRequiredMixin   # авторизация для автора
from django.contrib.auth.models import Group  # импорт созданных групп
from .models import Appointment    # рассылка сообщений
from django.core.mail import send_mail


class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'  # сортировка по расположению в порядке возрастания, или убывания '-name'

    # queryset = Product.objects.filter(
    #     price__lt=65990
    # ).order_by('name')  # отсортировать по цене ниже чем 50000 и с помощью .order_by добавить другую
    # # сортировку ordering = 'name'

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка товаров
    def __init__(self):
        self.filterset = None

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юнете ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.

        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Скоро ожидается снижение цен!'

        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# ProductDetail, которое будет выдавать информацию об одном товаре
class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'flatpages/product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Скоро ожидается снижение цен!'
        return context


# Create your views here.

# Добавляем новое представление для создания товаров.
class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/product_edit.html'


# ______________________________________________________________________________________________________________

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = NewsPortal
    # ___________________________________________________________
    ordering = '-sort_date_of_publication'
    # Здесь будит Фильтрация
    # по новизне новости
    # ___________________________________________________________
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    paginate_by = 10  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юнете ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.

        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.

        context['next_sale'] = 'Все самое свежее у нас!'

        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset

        return context


# NewsDetail, которое будет выдавать информацию об одной новости
class NewsDetail(LoginRequiredMixin, DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = NewsPortal
    ordering = '-sort_date_of_publication'
    # Используем другой шаблон — new.html
    template_name = 'flatpages/new.html'
    # Название объекта, в котором будет выбранный пользователем новость
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Следите за дальнейшим развитием события у нас на портале'
        return context


# Добавляем новое представление для создания новости.
class NewCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_newsportal')
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель товаров
    model = NewsPortal
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/post/new/create/':
            new.news_category_id = 1
        elif self.request.path == '/post/article/create/':
            new.news_category_id = 2
        new.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

# Авторизация пользователя для изменения данных и их обновление с помощью LoginRequiredMixin. Так же
# прописываем settings.py переменная LOGIN_URL с возвратом на страницу после успешной авторизации. Импортируем так
# же from django.contrib.auth.mixins import LoginRequiredMixin
# Добавляем обновление новости и статьи.
class NewUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_newsportal')
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель товаров
    model = NewsPortal
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/post/new/create/':
            new.news_category_id = 1
        elif self.request.path == '/post/article/create/':
            new.news_category_id = 2
        new.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

# Представление удаляющее товар.
class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_newsportal')

    model = NewsPortal
    template_name = 'flatpages/new_delete.html'
    success_url = reverse_lazy('new_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/profile/')

def profile(request):
    context = {'is_not_author': not request.user.groups.filter(name='authors').exists()}
    return render(request, 'flatpages/profile.html', context)

# подключаем отправку почтовых сообщений
class AppointmentView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'flatpages/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # отправляем письмо
        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='damirfn12345@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=['damirfn@mail.ru']  # Здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        return redirect('/appointment/')