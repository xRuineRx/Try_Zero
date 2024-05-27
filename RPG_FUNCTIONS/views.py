from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GamePostForm
from .models import GamePost, GameUser

from django.shortcuts import get_object_or_404

# Create your views here.


class GamePostList(ListView):
    model = GamePost
    template_name ='Gameposts.html'
    context_object_name = 'GamePosts'


class GamePostDetail(DetailView):
    model = GamePost
    template_name = 'Post_Detail.html'
    context_object_name = "post"


class GamePostUpdate(LoginRequiredMixin, UpdateView):
    form_class = GamePostForm
    model = GamePost
    template_name = 'GamePost_Create.html'
    success_url = reverse_lazy('All_Posts')

class GamePostCreate(LoginRequiredMixin, CreateView):
    model = GamePost
    form_class = GamePostForm
    template_name = 'GamePost_Create.html'
    success_url = reverse_lazy('All_Posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        GameUser.objects.get_or_create(user_link=self.request.user)
        post.link_GameUser = self.request.user.gameuser
        post.save()
        return super().form_valid(form)




#Приватная страница пользователя с его объявлениями и  откликами на его объявления
class PrivateGameCabinateList(ListView):
    model = GamePost
    template_name ='PrivateGameCabinate.html'
    context_object_name = 'GamePosts_Private'

    def get_queryset(self):
        # self.link_GameUser = get_object_or_404(GameUser, id=self.kwargs['pk'])
        # ask = GameUser.objects.get_or_create(user_link=self.request.user)
        # queryset = GamePost.objects.filter(link_GameUser=ask)
        # return queryset

        # ask_1 = GameUser.objects.get_or_create(user_link=self.request.user)

        # ask_2 = list(GameUser.objects.values_list('user_link', flat=True))[1]
        ask_2= list(GameUser.objects.filter(user_link=self.request.user).values_list('user_link', flat=True))[0]

        queryset = GamePost.objects.filter(link_GameUser=ask_2)
        return queryset


#Для отправки отклика
# @login_required
# def subscribe(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscribers.add(user)
#
#     message = 'Вы успешно подписались на рассылку новостей категорий'
#     return render(request, 'flatpages/subscribe.html', {'category': category, 'message' : message})



