def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_page.html', {'role': 'Member'})
