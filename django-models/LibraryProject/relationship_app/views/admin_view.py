from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# from django.http import HttpResponseForbidden

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_page.html', {'role': 'Admin'})


# # Helper function to check for 'Admin' role
# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')
