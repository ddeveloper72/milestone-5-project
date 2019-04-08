from django.shortcuts import render
from issue_tracker.models import Issue
from django.core.paginator import Paginator

# Create your views here.


def do_search(request):
    issue_list = Issue.objects.filter(genre__icontains=request.GET['q'])
    paginator = Paginator(issue_list, 3)
    page = request.GET.get('page')
    issues = paginator.get_page(page)
    return render(request, "issues_list.html", {'issues': issues})
