
from django.views import generic

from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DateDetailView):
    model = Post
    slug_field = 'slug'
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        # Aqui, 'slug' é extraído dos argumentos de palavra-chave da URL
        return Post.objects.get(slug=self.kwargs['slug'])