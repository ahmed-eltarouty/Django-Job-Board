from django.shortcuts import redirect, render
from .forms import ContactUs_Form
# Create your views here.



def view_contact(request):
    
    if request.method == 'POST':
        form = ContactUs_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:sent')

    else:
        form = ContactUs_Form()

    return render(request,'contact_us.html',{'form':form})



def sent(request):
    
    return render(request , 'sucess.html',{})