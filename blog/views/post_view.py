from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


#class PostDetail(generic.DateDetailView):
 #   model = Post
 #   slug_field = 'slug'
 #   template_name = 'post_detail.html'
 #   context_object_name = 'post'
 #   
 #   def get_object(self, queryset=None):
 #       # Aqui, 'slug' é extraído dos argumentos de palavra-chave da URL
 #       return Post.objects.get(slug=self.kwargs['slug'])

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by('-created_on')
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()
        print()
    return render(
        request,
        template_name,
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        },
    )
