from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from . models import Pension
from . models import Pen
from django.contrib import messages
# Create your views here.

# index crud 

def index(request):

   

    if request.method == "POST":
       
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        rsa = request.POST.get('rsa')
        pfa = request.POST.get('pfa')
        balance = request.POST.get('balance')


        # try:
        #     existed = Pen.objects.get(email=email)

        #     messages.error(request,"Email Address Already Exists")
        #     return redirect(request.META['HTTP_REFERER'])

        # except existed.DoesNotExist:

        if Pen.objects.filter(email=email).exists():
            messages.error(request,"Email Address Already Exists")
            return redirect(request.META['HTTP_REFERER'])

        pension = Pen(
            fullname = fullname,
            email = email,
            phone = phone,
            rsa = rsa,
            pfa = pfa,
            balance = balance,
            isActive = True

        )

        pension.save()

        messages.success(request,'New Pencom was added successfully')
    

        return redirect(request.META['HTTP_REFERER'])

    pfacompany = [
    "AIICO Pension Managers Limited",
    "APT Pension Fund Managers Limited",
    "ARM Pension Managers (PFA) Limited",
    "AXA Mansard Pension Limited",
    "CrusaderSterling Pensions Limited",
    "Fidelity Pension Managers Limited",
    "First Guarantee Pension Limited",
    "Future Unity Glanvills Pensions Limited",
    "IEI-Anchor Pension Managers Limited",
    "Investment One Pension Managers Limited",
    "Leadway Pensure PFA Limited",
    "Nigerian University Pension Management Company Limited (NUPEMCO)",
    "NPF Pensions Limited",
    "PAL Pensions Limited",
    "Pension Alliance Limited",
    "Premium Pension Limited",
    "Radix Pension Managers Limited",
    "Sigma Pensions Limited",
    "Stanbic IBTC Pension Managers Limited",
    "Trustfund Pensions Limited",
    "Veritas Glanvills Pensions Limited",
    "CrusaderSterling Pensions Limited (formerly UBA Pension Custodian Limited)",
    "Legacy Pension Managers Limited"
        ]

  
    accounts = Pen.objects.all()
    context = {
        'pfa':pfacompany,
        'accounts':accounts
    }


    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("Hello, this is about")


def details(request,id):

    account = Pen.objects.get(id=id)

    if request.method == "POST":
    #    status = request.POST.get("status")
    #    pension = get_list_or_404(Pen, id=id)
    #    pension.status = not pension.status  
    #    pension.save()


        status = request.POST.get("status")
       

      
        pension = Pen.objects.get(id=id)
        pension.isActive = not pension.isActive
        pension.save()
        


        return redirect(request.META['HTTP_REFERER'])


    context = {
        'account':account
    }


    return render(request, 'details.html', context)


def deletePension(request,id):

    if request.method == 'POST':
        pension = Pen.objects.get(id=id)
        pension.delete()
        

        messages.success(request,"Account deleted successfully")

        return redirect('index')


# Update pension account

def updatePension(request,id):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        rsa = request.POST.get('rsa')
        pfa = request.POST.get('pfa')
        balance = request.POST.get('balance')
 

        pension = Pen.objects.get(id=id)
        pension.fullname = fullname
        pension.email = email
        pension.phone = phone
        pension.rsa = rsa
        pension.pfa = pfa
        pension.balance = balance
        pension.save()

        messages.success(request,"Account updated successfully")
        return redirect('index')