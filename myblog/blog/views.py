from django.shortcuts import render

# Create your views here.
#首页
from blog.models import Category, Article, Tag


def index(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    allarticle = Article.objects.all().order_by('-id')[0:6]
    tui = Article.objects.filter(tui__id=1)[:3]  # 查询推荐位ID为1的文章
    # hot = Article.objects.all().order_by('?')[:10]#随机推荐
    # hot = Article.objects.filter(tui__id=3)[:10]   #通过推荐进行查询，以推荐ID是3为例
    hot = Article.objects.all().order_by('-views')[:6]  # 通过浏览数进行排序
    remen = Article.objects.filter(tui__id=2)[:6]
    # 把查询出来的分类封装到上下文里
    context = {
        'allcategory': allcategory,
        'allarticle': allarticle,
        'tui': tui,
        'hot': hot,
        'remen': remen,
    }
    return render(request, 'index.html', context)  # 把上下文传到index.html页面

#列表页
def list(request,lid):
    pass

#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass