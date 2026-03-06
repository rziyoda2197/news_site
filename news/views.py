from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Q, F
from .models import Post, Category, Comment, PostView
from .forms import CommentForm, EmailShareForm, ContactForm, SearchForm


def home(request):
    latest_posts = Post.objects.filter(status='published')[:6]
    most_read = Post.objects.filter(status='published').order_by('-views_count')[:5]
    return render(request, 'news/home.html', {
        'latest_posts': latest_posts,
        'most_read': most_read,
    })


def post_list(request):
    posts_qs = Post.objects.filter(status='published')
    paginator = Paginator(posts_qs, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/post_list.html', {
        'posts': posts,
        'page_title': 'Barcha yangiliklar',
    })


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')

    # Faqat yangi IP manzildan ko'rilganda views_count oshadi
    ip = get_client_ip(request)
    _, created = PostView.objects.get_or_create(post=post, ip_address=ip)
    if created:
        Post.objects.filter(pk=post.pk).update(views_count=F('views_count') + 1)
    post.refresh_from_db(fields=['views_count'])

    comments = post.comments.filter(active=True)
    commented = request.GET.get('commented') == '1'

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url() + '?commented=1#comments')
    else:
        comment_form = CommentForm()

    # Similar posts by category
    similar_posts = Post.objects.filter(
        status='published', category=post.category
    ).exclude(id=post.id)[:4] if post.category else Post.objects.none()

    return render(request, 'news/post_detail.html', {
        'post': post,
        'comments': comments,
        'commented': commented,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_qs = Post.objects.filter(status='published', category=category)
    paginator = Paginator(posts_qs, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/category.html', {
        'category': category,
        'posts': posts,
    })


def tag_posts(request, tag):
    posts_qs = Post.objects.filter(status='published', tags__icontains=tag)
    paginator = Paginator(posts_qs, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/tag_posts.html', {
        'tag': tag,
        'posts': posts,
    })


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(
                status='published'
            ).filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
    return render(request, 'news/search.html', {
        'form': form,
        'query': query,
        'results': results,
    })


def post_share(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} sizga yangilik yubordi: {post.title}"
            message = f"'{post.title}' yangiligini o'qing: {post_url}\n\n" \
                      f"{cd['name']} izohi: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailShareForm()
    return render(request, 'news/post_share.html', {
        'post': post,
        'form': form,
        'sent': sent,
    })


def about(request):
    return render(request, 'news/about.html')


def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                f"Kimdan: {cd['name']} ({cd['email']})\n\n{cd['message']}",
                cd['email'],
                ['admin@newsportal.uz'],
            )
            sent = True
    else:
        form = ContactForm()
    return render(request, 'news/contact.html', {
        'form': form,
        'sent': sent,
    })
