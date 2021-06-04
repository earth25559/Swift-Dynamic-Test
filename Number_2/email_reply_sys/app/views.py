from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def fill_info(request):
    form = CustomerForm()
    customer = Customer.objects.all()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view-user')
    context = {'form': form}
    print(form)

    return render(request, 'email_sys/user_email_form.html', context)


def view_user(request):
    customer = Customer.objects.all()
    print(customer)
    form = CustomerForm()
    context = {"customer": customer}
    return render(request, 'email_sys/view_user.html', context)


def delete_user(request, pk):
    customer = Customer.objects.get(id=pk)
    print(customer)
    print(customer.name)
    if request.method == 'POST':
        print(customer)
        print(customer.name)
        customer.delete()
        return redirect('/view-user')

    context = {'customer': customer}
    return render(request, 'email_sys/delete_user.html', context)


def index(request):
    customer = Customer.objects.all()
    form = CustomerForm()
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        name = request.POST.getlist('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        template = render_to_string(
            'email_sys/email_template.html', {'name': 'Earth'})
        list_of_cust = Customer.objects.filter(id__in=name)
        print(list_of_cust)
        for cus in list_of_cust:
            email = EmailMessage(
                subject,
                (f"Dear Khun {cus.name},\n{message}"),
                settings.EMAIL_HOST_USER,
                [cus.email],
            )
            print(cus.name)
            print(cus.email)
            email.fail_silently = False
            email.send()
    # if request.method == "POST":
        return redirect('/success', )
    context = {"form": form, "customer": customer}
    return render(request, 'email_sys/email.html', context)


def send_mail(request):
    customer = Customer.objects.all()
    form = CustomerForm()
    context = {"form": form}
    return render(request, 'email_sys/email_send.html', context)


def pre_fill(request):
    customer = Customer.objects.all()
    template = render_to_string(
        'email_sys/email_template.html', {'name': 'Earth'})
    context = {"template": template, "customer": customer}
    return render(request, 'email_sys/email.html', context)
