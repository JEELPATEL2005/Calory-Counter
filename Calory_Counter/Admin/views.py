from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from requests import request
from Calory.models import Food
from .models import User
from Calory.views import user_login, user_logout

# ============= ADMIN DASHBOARD =============
@login_required
def admin_dashboard(request):
    """Main admin dashboard"""

    role = request.user.role 
    
    if role not in ['admin', 'superadmin']:
        return redirect('login')

    # Get statistics
    total_foods = Food.objects.count()
    total_users = User.objects.filter(role ='user').count()
    total_admins = User.objects.filter(role = 'admin').count()
    
    context = {
        'total_foods': total_foods,
        'total_users': total_users,
        'total_admins': total_admins,
    }
    
    return render(request, 'Admin/dashboard.html', context)

# ============= FOOD MANAGEMENT =============
@login_required
def manage_food(request):
    """Manage all food items"""
    
    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')

    foods = Food.objects.all().order_by('name')
    
    return render(request, 'Admin/manage_foods.html', {'foods': foods})

@login_required
def add_food(request):
    """Add a new food item"""
    
    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        meal_type = request.POST.get('meal_type')

        try:
            calories = float(request.POST.get('calories_100g') or 0)
        except ValueError:
            calories = 0
        try:
            protein = float(request.POST.get('protein') or 0)
        except ValueError:
            protein = 0
        try:
            carbs = float(request.POST.get('carbs') or 0)
        except ValueError:
            carbs = 0
        try:
            fat = float(request.POST.get('fat') or 0)
        except ValueError:
            fat = 0
        try:
            serving = float(request.POST.get('serving_grams') or 100)
        except ValueError:
            serving = 100
        verified = True if request.POST.get('verified') else False

        if name:
            Food.objects.create(
                meal_type=meal_type,
                name=name,
                calories_100g=calories,
                protein=protein,
                carbs=carbs,
                fat=fat,
                serving_grams=serving,
                verified=verified
            )

        return redirect('manage_foods')

    return render(request, 'Admin/edit_food.html', {'food': None})

@login_required
def edit_food(request, food_id):
    """Edit an existing food item"""
    
    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')

    food = get_object_or_404(Food, id=food_id)

    if request.method == 'POST':
        food.name = request.POST.get('name', food.name).strip()
        try:
            food.calories_100g = float(request.POST.get('calories_100g') or food.calories_100g)
        except ValueError:
            pass
        try:
            food.protein = float(request.POST.get('protein') or food.protein)
        except ValueError:
            pass
        try:
            food.carbs = float(request.POST.get('carbs') or food.carbs)
        except ValueError:
            pass
        try:
            food.fat = float(request.POST.get('fat') or food.fat)
        except ValueError:
            pass
        try:
            food.serving_grams = float(request.POST.get('serving_grams') or food.serving_grams)
        except ValueError:
            pass
        food.verified = True if request.POST.get('verified') else False
        food.save()

        return redirect('manage_foods')

    return render(request, 'Admin/edit_food.html', {'food': food})

@login_required
def delete_food(request, food_id):
    """Delete a food item"""

    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')
    
    food = get_object_or_404(Food, id=food_id)
    food.delete()

    return redirect('manage_foods')

# ============= USER MANAGEMENT =============
@login_required
def manage_users(request):
    """Manage all users"""
    
    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')

    users = User.objects.filter(role = 'user').order_by('username')
    
    return render(request, 'Admin/manage_users.html', {'users': users })

@login_required
def delete_user(request, user_id):
    """Delete a user account"""

    if request.user.role not in ['admin', 'superadmin']:
        return redirect('login')

    user = get_object_or_404(User, id=user_id)
    user.delete()

    return redirect('manage_users')

# ============= ADMIN MANAGEMENT =============
@login_required
def create_admin(username, email, password):

    if request.user.role != 'superadmin':
        return redirect('login')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='admin',
            is_staff=True
        )
        return redirect('admin_manage_admins')

    return render(request, 'create_admin.html')

@login_required
def manage_admins(request):
    """Manage admin users and their roles"""

    if request.user.role != 'superadmin':
        return redirect('login')

    admins = User.objects.filter(role='admin')

    return render(request, 'Admin/manage_admins.html', {'admins': admins})

@login_required
def create_admin(request):
    """Create a new admin user"""

    if request.user.role != 'superadmin':
        return redirect('login')

    if request.method == "POST":

        User.objects.create_user(
            username=request.POST.get('username', '').strip(),
            email=request.POST.get('email', '').strip(),
            password=request.POST.get('password'),
            role='admin',
            is_staff=True
        )
        return redirect('manage_admins')

    return render(request, 'Admin/edit_admin.html')

@login_required
def delete_admin(request, admin_id):
    """Edit admin role"""
    
    if request.user.role != 'superadmin':
        return redirect('login')

    admin = get_object_or_404(User, id=admin_id)
    admin.delete()
    
    return redirect('manage_admins')