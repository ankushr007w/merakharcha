from django.shortcuts import render,redirect
from .models import Expense

def home(request):
    expense = Expense.objects.all()[::-1]

    data ={ 
        'expense' : expense,
    }
    return render(request,"index.html", data)


def add(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        kname = request.POST.get('kname')
        pname = request.POST.get('pname')
        mode = request.POST.get('mode')

        exp = Expense(
            date=date,
            amount=amount,
            kname=kname,
            pname=pname,
            mode=mode,
        )

        exp.save()
        return redirect('home')
    return render(request,"index.html")


def edit(request):
    expense = Expense.objects.all()[::-1]

    data ={ 
        'expense' : expense,
    }
    return render(request,"index.html", data)


def update(request,id):
    if request.method == 'POST':
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        kname = request.POST.get('kname')
        pname = request.POST.get('pname')
        mode = request.POST.get('mode')

        exp = Expense(
            id=id,
            date=date,
            amount=amount,
            kname=kname,
            pname=pname,
            mode=mode,
        )
        exp.save()
        return redirect('home')
    return render(request,"index.html")

def delete(request,id):
    expense = Expense.objects.filter(id = id)
    expense.delete()
    data = {
        'expense':expense
    }
    return redirect('home')
    return render(request,"index.html",data)








