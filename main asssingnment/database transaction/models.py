from django.db import models



from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp2.models import MyModel

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    with transaction.atomic():
        pass

#or this method same database transaction

from django.shortcuts import render
from django.contrib import messages
from .models import Transaction
from django.db import transaction
 
def home(request):
    if request.method == 'POST':
        try:
            one = request.POST.get('one')
            two = request.POST.get('two')
            amount = int(request.POST.get('amount'))
             
            # Start a database transaction block
            with transaction.atomic():
                user_one_Transaction_obj = Transaction.objects.get(user=user_one)
                user_two_Transaction_obj = Transaction.objects.get(user=user_two)
                     
                user_one_Transaction_obj.amount -= amount
                user_one_Transaction_obj.save()
                     
                user_two_Transaction_obj.amount += amount
                user_two_Transaction_obj.save()
             
            messages.success(request, "Amount transferred successfully")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
     
    return render(request, 'home.html')
