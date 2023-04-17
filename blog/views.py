from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import NewForm
from .models import Post


def post_home(request):
    return render(request, 'blog/post_home.html')


# def post_list(request):
#     post = Post.objects.filter(status='PUB').order_by('-deta_edited')
#     return render(request, 'blog/post_list.html', {'post': post})

class PostList(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(status='PUB').order_by('-deta_edited')


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetail(generic.DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    model = Post


# def post_create(request):
#     form = NewForm()
#     if request.method == 'POST':
#         form = NewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     return render(request, 'blog/post_create.html', {'form': form})

class PostCreate(generic.CreateView):
    form_class = NewForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


#
# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('post_detail', args=[pk]))
#     return render(request, 'blog/post_update.html', {'form': form})

class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'form'
    form_class = NewForm


# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_delete.html', {'post': post})

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
