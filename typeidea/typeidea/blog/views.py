from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category
from config.models import  Sidebar
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

class CommonViewMixin:
    # def get_category_context(self):
    #     categories = Category.objects.filter(status=1)  # TODO: fix magic number

    #     nav_cates = []
    #     cates = []
    #     for cate in categories:
    #         if cate.is_nav:
    #             nav_cates.append(cate)
    #         else:
    #             cates.append(cate)
    #     return {
    #         'nav_cates': nav_cates,
    #         'cates': cates,
    #     }

    #获取content内容
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': Sidebar.get_all(),
        })
        context.update(Category.get_nav())
        return context

class IndexView(CommonViewMixin,ListView):
    # queryset = Post.latest_posts()
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'
# Create your views here.

class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        # get_object_or_404是一个快捷方式，用来获取一个对象的实例，如果获取到，返回实例对象。如果不存在，返回404错误
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        # 重写queryset，根据分类过滤
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)

class  TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)

class PostDetailView(CommonViewMixin,DetailView):
    # queryset = Post.latest_posts()  这种方法会报错
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'




# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None

#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)

#     else:
#         post_list = Post.latest_posts()

#     context = {
#         'category': category,
#         'tag':tag,
#         'post_list' : post_list,
#     }
#     context.update(Category.get_nav())
#     context.update({"sidebars" : Sidebar.get_cli()})
#     return render(request, 'blog/list.html', context=context)
    # if  tag_id:
    #     try:
    #         tag = Tag.objects.get(id=tag_id)
    #     except Tag.DoesNotExist:
    #         post_list = []
    #     else:
    #         post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    # else:
    #     post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
    #     if category_id:
    #         post_list = post_list.filter(category_id=category_id)
    # return render(request, 'blog/list.html', context={'post_list': post_list})
    # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id)
    # return HttpResponse(content)
    # return render(request, 'blog/list.html', context={'name': 'post_list'})

# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None

#     print(type(post))
#     context = {'post':post}
#     context.update(Category.get_nav())
#     context.update({"sidebars": Sidebar.get_cli()})
#     return render(request, 'blog/detail.html', context=context)

    # return HttpResponse('detail')
    # return render(request, 'blog/detail.html', context={'name': "post_detail"})

