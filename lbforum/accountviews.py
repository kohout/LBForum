from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from forms import SignatureForm


def profile(request, username=None, template_name="lbforum/account/profile.html"):
    view_user = request.user
    if username:
        view_user = get_object_or_404(get_user_model(), username=username)
    view_only = view_user != request.user
    ext_ctx = {'view_user': view_user, 'view_only': view_only}
    return render(request, template_name, ext_ctx)


@login_required
def signature(request, form_class=SignatureForm, template_name="lbforum/account/signature.html"):
    profile = request.user.lbforum_profile
    if request.method == "POST":
        form = form_class(instance=profile, data=request.POST)
        form.save()
    else:
        form = form_class(instance=profile)
    ext_ctx = {'form': form}
    return render(request, template_name, ext_ctx)
