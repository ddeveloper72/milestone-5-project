from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from issue_tracker.models import Issue, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def do_search(request):
    """Create a search that picks up keywords from the
        Issue model
    """
    queryset_list = Issue.objects
    query = request.GET.get('q')

    if query:
        queryset_list = queryset_list.filter(
            Q(genre__icontains=query) |
            Q(category__icontains=query) |
            Q(tag__icontains=query) |
            Q(genre__icontains=query) |
            Q(completed__icontains=query) |
            Q(status__icontains=query)
        ).distinct()  # Do not add duplicate items

    paginator = Paginator(queryset_list, 1)
    page_request_var = "page"
    page = request.GET.get('page', 1)
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an ineger, deliver first page
        issues = paginator.page(1)
    except EmptyPage:
        # if page is out of range (eg 9999), deliver last page in range
        issues = paginator.page(paginator.num_pages)
    return render(request, "issues_list.html", {'issues': issues})

    