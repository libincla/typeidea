from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category
from config.models import  Sidebar


# Create your views here.

def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)

    else:
        post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag':tag,
        'post_list' : post_list,
    }
    context.update(Category.get_nav())
    context.update({"sidebars" : Sidebar.get_cli()})
    return render(request, 'blog/list.html', context=context)
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


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    print(type(post))
    context = {'post':post}
    context.update(Category.get_nav())
    context.update({"sidebars": Sidebar.get_cli()})
    return render(request, 'blog/detail.html', context=context)

    # return HttpResponse('detail')
    # return render(request, 'blog/detail.html', context={'name': "post_detail"})

