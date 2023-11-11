from .forms import AddBoulderFormU18UE50, AddBoulderFormBJM, AddBoulderFormBJW
from .boulders_controller import get_sorted_boulder_data_based_on, get_existing_boulder_data, \
    retrieve_boulders_based_on_, get_addboulderform_based_on_category, category2boulder_model__mapping
from django.contrib.auth.decorators import login_required
import logging
from .models import UserProfile, U18W, U18M, UE50W, UE50M
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
logger = logging.getLogger(__name__)


def home(request):
    return render(request, "home.html")


def ranking_view(request):
    modes = ["u18", "bj", "ue50"]
    genders = ["man", "woman"]

    rankings = {}

    for mode in modes:
        for gender in genders:
            category = f"{mode}_{gender}"
            data = get_sorted_boulder_data_based_on(category)
            rankings[category] = data

    context = {
        'rankings': rankings,
    }

    return render(request, "ranking.html", context)

@login_required
def view_boulder(request):
    user_boulders = retrieve_boulders_based_on_(request.user)
    return render(request, 'view_boulder.html', {'boulders': user_boulders, 'username': request.user.username})




@login_required
def add_boulders_view(request):

    cur_user_profile = UserProfile.objects.get(user=request.user)
    user_gender = cur_user_profile.gender
    user_mode = cur_user_profile.mode
    user_category = f"{user_mode}_{user_gender}"
    form_class_name = get_addboulderform_based_on_category(user_category)

    existing_boulder = get_existing_boulder_data(request.user, user_category)
    if request.method == 'POST':
        if user_category.startswith("ue50") or user_category.startswith("u18"):
            model = category2boulder_model__mapping(user_category)
            form = form_class_name(request.POST, instance=existing_boulder, model=model)
        else:
            form = form_class_name(request.POST, instance=existing_boulder)
        if form.is_valid():
            boulder_entry = form.save(commit=False)
            boulder_entry.user = request.user
            boulder_entry.save()
            logger.info("Boulders added successfully")
            return redirect('jagd:view_boulder')
        else:
            if user_category.startswith("ue50") or user_category.startswith("u18"):
                model = category2boulder_model__mapping(user_category)
                form = form_class_name(request.POST, instance=existing_boulder, model=model)
            else:
                form = form_class_name(request.POST, instance=existing_boulder)
            logger.error("Boulders addition failed. Unsuccessful form submission")
        return render(request, "add_boulders.html", {'form': form, 'username': request.user.username})

    else:

        if user_category.startswith("ue50") or user_category.startswith("u18"):
            model = category2boulder_model__mapping(user_category)
            form = form_class_name(request.POST, instance=existing_boulder, model=model)
        else:
            form = form_class_name(request.POST, instance=existing_boulder)
        return render(request, "add_boulders.html", {'form': form, "username": request.user.username})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('jagd:home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('jagd:home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('jagd:home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('jagd:home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('jagd:home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        # Create the UserProfile and associate it with the User
        gender = request.POST.get('gender')
        mode = request.POST.get('mode')
        UserProfile.objects.create(user=myuser, gender=gender, mode=mode)

        messages.success(request,
                         "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")


        return redirect('jagd:signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'home.html', {"username": username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('jagd:home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    return redirect('jagd:home')