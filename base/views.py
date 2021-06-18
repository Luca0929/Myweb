from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post, Category
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
	template_name = 'base/login.html'
	fields = '__all__'


	def get_success_url(self):
		return reverse_lazy('post_list')


class PostList(ListView):
	model = Post
	template_name='base/post_list.html'
	context_object_name = 'posts'


	def get_context_data(self, **kwagrs):
		cat_list = Category.objects.all()
		context= super().get_context_data(**kwagrs)
		search_input= self.request.GET.get('search-area') or ''
		category= self.request.GET.get('category') or ''
		if search_input:
			if context['posts'].filter(title__icontains=search_input):
				context['posts'] = context['posts'].filter(title__icontains=search_input)
			else: 
				if context['posts'].filter(body__icontains=search_input):
					context['posts'] = context['posts'].filter(body__icontains=search_input)
				
		if category:
			context['posts'] = context['posts'].filter(category__name=category.title())

		context['cat_list'] = cat_list
		context['search_input'] = search_input	
		return context




class PostDetail(DetailView):
	model = Post
	template_name='base/post_detail.html'
	

class CreatePost(LoginRequiredMixin, CreateView):
	model = Post
	template_name='base/post_create.html'
	fields = '__all__'

	success_url = reverse_lazy('post_list')

class EditPost(LoginRequiredMixin, UpdateView):
	model = Post
	template_name='base/post_edit.html'
	fields = '__all__'
	success_url = reverse_lazy('post_list')

class DeletePost(LoginRequiredMixin, DeleteView):
	model = Post
	template_name='base/post_delete.html'
	success_url = reverse_lazy('post_list')