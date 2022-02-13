
from django.shortcuts import redirect, render
from django.contrib import messages
from hiretubers.models import HireTubers

# Create your views here.

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # tuber_id = models.IntegerField()
    # tuber_name = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # message = models.TextField()
    # user_id = models.IntegerField(blank=True)

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hiretubers = HireTubers(
            first_name=first_name,
            last_name=last_name,
            tuber_id=tuber_id,
            tuber_name=tuber_name,
            city=city,
            phone=phone,
            email=email,
            state=state,
            message=message,
            user_id=user_id
        )

        hiretubers.save()
        messages.success(request,"Thank you for reaching out !")
        return redirect('youtubers')