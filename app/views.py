from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import auth
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Session
from .forms import SessionForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/conference/')


def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = ''
                if 'next' in request.GET:
                    next = request.GET['next']
                if next == None or next == '':
                    next = '/'
                return redirect(next, {'message': 'Logged in!!'})
            else:
                return render(request, 'auth/login.html', {
                    'warning': 'Your account has been disabled'
                })
        else:
            return render(request, 'auth/login.html', {
                'warning': 'Invalid username or password'
            })


# @login_required
# def submit_session(request):
#     return render(request, 'submit_session.html')


class SessionList(ListView):
    model = Session
    template_name = 'app/sessions.html'
    context_object_name = 'sessions'


class SessionDetail(DetailView):
    model = Session
    context_object_name = 'session'
    template_name = 'app/session.html'


class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm


class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm


class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('app:session_list')
