from django.contrib.auth.models import User

def all_users_context(request):
    users = User.objects.all()
    return {'all_users': users}

def user_groups_context(request):
    if request.user.is_authenticated:
        groups = request.user.groups.all()
        return {'user_groups': groups}
    return {'user_groups': None}