from django.views import View

from creditapp.models import *
from django.http import *
from django.shortcuts import *

from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import *
from creditapp.forms import *
from django.urls import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import *
from django.contrib import messages
from django.contrib.auth.models import *
from django.contrib.auth import *
app_name="creditapp"

class CreditList(LoginRequiredMixin, ListView):
    login_url = 'creditapp:login'
    model = Card
    context_object_name = 'jails'
    template_name = 'creditapp/credit_list.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(CreditList, self).get_context_data(**kwargs)
        context.update(
            {
                'jails': Card.objects.filter(user__username = self.request.user.username)
            }
        )
        return context


class AddCard(LoginRequiredMixin, CreateView):
    login_url = 'creditapp:login'
    model = Card
    form_class = Addcard
    success_url = reverse_lazy('creditapp:credit_list')

    def get_context_data(self, **kwargs):
        context = super(AddCard, self).get_context_data(**kwargs)
        context.update({
            'form': context.get('form'),
        })
        return context
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user.username)
        user = get_object_or_404(User, pk=user.id)
        form = Addcard(request.POST)

        if form.is_valid():
            card = form.save(commit=False)
            card.user = user
            card.save()

            return redirect('creditapp:credit_list')


class DeleteCard(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'creditapp:login'
    model = Card
    template_name = 'creditapp/delete.html'
    success_url = reverse_lazy('creditapp:credit_list')

    def has_permission(self):
        res = Card.objects.filter(user__username = self.request.user.username, id = self.kwargs['pk'])
        if len(res)!=0:
            return True
        else:
            self.raise_exception=True
            return False


class EditCard(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'creditapp:login'
    model = Card
    form_class = Addcard
    success_url = reverse_lazy('creditapp:credit_list')

    def has_permission(self):
        res = Card.objects.filter(user__username = self.request.user.username, id = self.kwargs['pk'])
        if len(res)!=0:
            return True
        else:
            self.raise_exception=True
            return False


    def get_object(self, queryset=None):
        return get_object_or_404(Card, **{'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super(EditCard, self).get_context_data(**kwargs)
        return context


class LoginController(View):
    def get(self,request,*args,**kargs):
        login =  Loginform()
        return render(
            request,
            template_name="creditapp/login.html",
            context={'form':login,'title':'Login Form'}
        )

    def post(self, request, *args, **kwargs):
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('creditapp:credit_list')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('creditapp:login')

def logout_user(request):
    logout(request)
    return redirect('creditapp:login')