from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib import messages
from .models import Issue, Comment, UserSeenIssue, UserVoted, UserVotedFeature
from .forms import AddEditIssueFrom, CommentForm
from django.core.paginator import Paginator

# Create your views here.


@login_required
def get_issues(request):
    """
    Create a view that will return a list
    of Issues that were published prior to 'now'
    and render them to the 'issues_list.html' template.
    """
    try:
        issue_list = Issue.objects.filter(published_date__lte=timezone.now()
                                          ).order_by('-published_date')
        paginator = Paginator(issue_list, 3)
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

    except:
        messages.info(request, "There are no issues logged yet")
        return redirect(reverse('get_issues'))


@login_required
def issue_detail(request, pk):
    """
    Create a view that returns a single
    Issue object based on the ID(pk) and
    render it to the 'issue_detail.html' template,
    or return an error if the issue is not found.
    """
    try:
        issue = get_object_or_404(Issue, pk=pk)
        total_cost = issue.hours_required * 55

        if not request.user.seen_issue.filter(post_id=pk).exists():
            issue.views += 1
            issue.save()
            UserSeenIssue.objects.create(user=request.user, post=issue)
        return render(request, "issue_detail.html", {'issue': issue,
                      'total_cost': total_cost})
    except:
        messages.info(request, "There are no bugs yet")
        return redirect(reverse('get_issues'))


@login_required
def new_issue(request, pk=None):
    """
    Create a view that allows us to create issue depending if the Issue ID
    is null or not.
    """
    genre = 'genre'
    hours_required = 'hours_required'

    if request.method == "POST":
        form = AddEditIssueFrom(request.POST, request.FILES)

        if request._post['genre'] == 'Navigation':
            hours_required = 3
            print(hours_required)
            messages.info(request, "Yay were inside the loop!")
        elif request._post['genre'] == 'Flight Controls':
            hours_required = 6
            print(hours_required)
            messages.info(request, "Yay were still inside the loop!")
        elif request._post['genre'] == 'Auto Pilot':
            hours_required = 9
            print(hours_required)
            messages.info(request, "Yay were still inside the loop!")

        else:
            messages.warning(request, "Sorry there has been an error")

        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user
            issue.hours_required = hours_required
            issue = form.save()
            return redirect(get_issues)

    else:
        form = AddEditIssueFrom()
    return render(request, 'new_issue_form.html',
                  {'form': form})

@login_required
def edit_issue(request, pk=None):
    """
    Create a view that allows us to edit an issue based on it product
    key in the issues table.
    """
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    hours_required = 0
    if issue.author == request.user:

        if request.method == "POST":
            form = AddEditIssueFrom(request.POST, request.FILES,
                                    instance=issue)           

            if issue.genre == 'Navigation':
                hours_required = 3
                print(hours_required)
                messages.info(request, "Yay were inside the loop!")
            elif issue.genre == 'Flight Controls':
                hours_required = 6
                print(hours_required)
                messages.info(request, "Yay were still inside the loop!")
            elif issue.genre == 'Auto Pilot':
                hours_required = 9
                print(hours_required)
                messages.info(request, "Yay were still inside the loop!")
            else:
                messages.warning(request, "Sorry there has been an error")

            if form.is_valid():
                issue = form.save(commit=False)
                issue.author = request.user
                issue.hours_required = hours_required
                issue.published_date = timezone.now()
                issue = form.save()
                return redirect(reverse('get_issues'))
        else:
            form = AddEditIssueFrom(instance=issue)
    else:
        messages.warning(request,
                         "WARNING! Only the author can edit their bug report")
        return redirect('get_issues')

    return render(request, 'new_issue_form.html',
                  {'form': form})


@login_required
def add_comment_to_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.issue = issue
            comment.save()
            issue.published_date = timezone.now()
            issue.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_issue.html', {'form': form})


@login_required
def comment_for_issue_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_superuser or request.user.is_staff:
        comment.approve()
        return redirect('issue_detail', pk=comment.issue.pk)
    else:
        messages.info(request, "A staff member will review your post")
        return redirect('issue_detail', pk=comment.issue.pk)


@login_required
def comment_for_issue_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_superuser or request.user.is_staff:
        comment.delete()
        return redirect('issue_detail', pk=comment.issue.pk)
    else:
        messages.info(request, "Only a staff member can remove a comment.")
        return redirect('issue_detail', pk=comment.issue.pk)


@login_required
def upvote(request, pk, category):

    issue = get_object_or_404(Issue, pk=pk)
    if category == 'BUG':
        if not request.user.has_voted.filter(post_id=pk).exists():
            issue.votes += 1
            bug_voter = request.user
            issue.voter.add(bug_voter)
            issue.save()
            UserVoted.objects.create(user=request.user, post=issue)
            messages.info(request, "Thank you for voting.")
            return redirect('issue_detail', pk=issue.pk)
        else:
            messages.warning(request, "You have already voted for this bug.")
            return redirect('issue_detail', pk=issue.pk)

    elif category == 'FEATURE':
        if not request.user.has_voted_feature.filter(post_id=pk).exists():
            issue.votes += 1
            feature_voter = request.user
            issue.voter.add(feature_voter)
            issue.save()
            UserVotedFeature.objects.create(user=request.user, post=issue)
            messages.info(request, "Thank you for voting.")
            return redirect('issue_detail', pk=issue.pk)
        else:
            messages.warning(request, "You have already voted for this feature.")
            return redirect('issue_detail', pk=issue.pk)
