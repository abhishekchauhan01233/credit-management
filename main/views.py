from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import user_model, transaction_model, feedback_model
from django.contrib import messages
from datetime import datetime, date

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def view(request):
    data = user_model.objects.all()
    if request.POST.get('add'):
        user_id = request.POST.get('userid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        credit = request.POST.get('credit')

        if user_model.objects.filter(user_id=user_id).exists():
            messages.error(request, "User with this UserID already exists")
            return redirect('/view/')

        elif user_model.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists")
            return redirect('/view/')

        else:
            user_model.objects.create(user_id=user_id, name=name, email=email, credit=credit)
            print("User Added Successfuly")
            messages.success(request, "User Added Successfuly")
            return redirect('/view/')
    
    elif request.POST.get('delete'):
        email = request.POST.get('email')
        user_model.objects.get(email=email).delete()
        messages.error(request, "User Deleted Successfully")
        print("User Deleted Successfuly")
        return  redirect('/view/')
        
    return render(request, 'main/view_credits.html', {'data':data})

def transfer(request):
    data = user_model.objects.all()
    today = date.today()
    current_time = datetime.strftime(datetime.now(),"%H:%M:%S")

    if request.POST.get('save'):
        from_email = request.POST.get('from')
        to_email = request.POST.get('to')
        amount = request.POST.get('amount')

        for d in data:
            if from_email == to_email:
                messages.error(request, "You cannot transfer your credits to yourself")

            elif d.email == from_email:
                if int(amount) == 0:
                    messages.error(request, "You cannot transfer 0 credits")
                    return redirect('/transfer/')

                elif int(amount) > int(d.credit):
                    messages.error(request, "You don't have sufficient credits")
                    return redirect('/transfer/')
                else:
                    from_data = user_model.objects.get(email=from_email)
                    new_credit = int(from_data.credit) - int(amount)
                    from_data.credit = new_credit
                    from_data.save()

                    to_data = user_model.objects.get(email=to_email)
                    new_credit2 = int(to_data.credit) + int(amount)
                    to_data.credit = new_credit2
                    to_data.save()
                    transaction_model.objects.create(from_email=from_email, to_email=to_email, credit=int(amount), date=today, current_time=current_time)
                    messages.success(request, "Transaction Successful")
                    return redirect('/transfer/')
    
    return render(request, 'main/transfer.html', {'data':data})

def history(request):
    data = transaction_model.objects.all()
    return render(request, 'main/history.html', {'data':data})

def feedback(request):
    if request.POST.get('save'):
        name = request.POST.get('name')
        role = request.POST.get('role')
        feedback = request.POST.get('feedback')

        feedback_model.objects.create(name=name, role=role, feedback=feedback)

    return render(request, 'main/feedback.html')