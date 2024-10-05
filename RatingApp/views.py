from django.shortcuts import render, redirect
from .models import SecondYear, ThirdYear,User
from .forms import SecondYearForm, ThirdYearForm, UserNameForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Start_view(request):
    if request.method == 'POST':
        user_form = UserNameForm(request.POST)
        if user_form.is_valid():
            user_instance = user_form.save(commit=True)
            request.session['user_email'] = user_instance.email  
            request.session['user_name'] = user_instance.name
            return redirect('/secondyear')  
    else:
        user_form = UserNameForm()

    return render(request, 'RatingApp/start.html', {'userform': user_form})


def SecondYearView(request):
    user_name = request.session.get('user_name', '')
    form = SecondYearForm()

    if request.method == 'POST':
        form = SecondYearForm(request.POST)
        
        if form.is_valid():
            rating_instance = form.save(commit=False)
            rating_instance.user = User.objects.get(email = request.session['user_email'])
            rating_instance.save()
            messages.success(request, "Your ratings have been submitted successfully!")
            return redirect('/thirdyear')

    return render(request, 'RatingApp/rating.html', {'data': form, "user_name":user_name})

def ThirdYearView(request):
    user_name = request.session.get('user_name', '')
    form = ThirdYearForm()

    if request.method == 'POST':
        form = ThirdYearForm(request.POST)
        
        if form.is_valid():
            rating_instance = form.save(commit=False)
            rating_instance.user = User.objects.get(email = request.session['user_email'])
            rating_instance.save()
            messages.success(request, "Your ratings have been submitted successfully!")
            return redirect('/result')

    return render(request, 'RatingApp/rating.html', {'data': form, "user_name":user_name})


def Success_view(request):
    return render(request, 'RatingApp/success.html')


# @login_required(login_url='/admin')
def Result_view(request):
    user_email = request.session.get('user_email', '')
    user_name = request.session.get('user_name', '')

    second_rating_details = SecondYear.objects.filter(user__email= user_email )
    third_rating_details = ThirdYear.objects.filter(user__email= user_email)

    second_year_rating = {key.replace('_', ' ') : val for key , val in second_rating_details.values()[0].items() if key != "id" and key != "user_id"} 
    third_year_rating = {key.replace('_', ' ') : val for key , val in third_rating_details.values()[0].items() if key != "id" and key != "user_id"} 
    
    if not second_rating_details.exists() and third_rating_details.exists():
        messages.warning(request, "No ratings found for your account.")

    return render(request, 'RatingApp/result.html', {'second_year_data': second_year_rating,'third_year_data': third_year_rating, "user_name":user_name})