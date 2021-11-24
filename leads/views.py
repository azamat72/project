from django.shortcuts import render, redirect
from . models import Lead, Agent, User
from django.shortcuts import get_object_or_404
from leads import models
from .forms import LeadForm

def index(request):
    leads = models.Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "index.html", context)

def about(request):
    data = Lead.objects.all()
    return render(request, "about.html", {'leads': data})

def news(request):
    data = Lead.objects.all()
    return render(request, "news.html", {'leads': data})

def contacts(request):
    data = Lead.objects.all()
    return render(request, "contacts.html", {'leads': data})

def leads_abc(request, pk):
    lead = get_object_or_404(models.Lead, id=pk) 
    context = {
        "lead": lead
    }
    return render(request, 'details.html', context)

def create(request):
    error = ''
    form = LeadForm
    if request.method == "POST":
        print("keldi")
        form = LeadForm(request.POST)
        if form.is_valid():
            # print("OK")
            # print(form.cleaned_data)
            # familiyasi = form.cleaned_data['familiyasi']
            # ismi = form.cleaned_data['ismi']
            # yoshi = form.cleaned_data['yoshi']
            # full = form.cleaned_data['full']
            # agent = Agent.objects.first()
            # Lead.objects.create(
            #     familiyasi = familiyasi,
            #     ismi = ismi,
            #     yoshi = yoshi,
            #     full = full,
            #     agent = agent
            # )
            form.save()
            return redirect('/about')
        else:
            error = "Shakllar noto'g'ri to'ldirilgan"


    form = LeadForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

