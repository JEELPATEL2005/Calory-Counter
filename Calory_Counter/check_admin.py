import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Calory_Counter.settings')
django.setup()
from Admin.models import AdminUser
print('count', AdminUser.objects.count())
for a in AdminUser.objects.all():
    print('admin:', a.user.username, a.user.email, 'active:', a.is_active)
