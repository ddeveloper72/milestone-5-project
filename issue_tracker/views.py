from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse, \
    HttpResponse
from django.utils import timezone
from django.contrib import messages
from .models import Issue
from .forms import AddEditIssueFrom

# Create your views here.


@login_required
def get_issues(request):
    """
    Create a view that will return a list
    of Issues that were published prior to 'now'
    and render them to the 'issues_list.html' template.    
    """
    try:
        issues = Issue.objects.filter(published_date__lte=timezone.now()
                                      ).order_by('-published_date')
        return render(request, "issues_list.html", {'issues': issues})

    except:
        messages.info(request, "There are no issues logged yet")
        return redirect(reverse('get_issues'))
  

