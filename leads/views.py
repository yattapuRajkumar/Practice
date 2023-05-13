
from django.shortcuts import render,redirect
from django.http import HttpResponse
from leads.forms import LeadForm,LeadModelForm
from leads.models import *

# Create your views here.

def lead_list(request):
    leads=Lead.objects.all()
    context={
        'leads':leads
        
    }
    return render(request,'lead_list.html',context)

#this is rajkumar.
print("this is venkat")
def lead_detail(request,pk):
    lead=Lead.objects.get(id=pk)
    context={
        'lead':lead
    }
    
    return render(request,'lead_detail.html',context)


# def lead_update(request,pk):
    
#     form=LeadForm()
#     lead=Lead.objects.get(id=pk)
#     print(request.POST)
#     if request.method=='POST':
#         print('receiving post request')
#         form=LeadForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             print(form.cleaned_data)

#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
           
            
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()
                
            
#             print('The lead has been created')
#             return redirect('/')
#     context={
#         'form':form,
#         'lead':lead
#     }

    
#     return render(request,'lead_update.html',context)

def lead_update(request,pk):
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)
    if request.method=='POST':
        form=LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
        'lead':lead
    }
    return render(request,'lead_update.html',context)


def lead_delete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')











# def lead_create(request):
#     form=LeadForm()
#     # print(request.POST)
#     if request.method=='POST':
#         print('receiving post request')
#         form=LeadForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             print(form.cleaned_data)

#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             agent=Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print('The lead has been created')
#             return redirect('/')


#     context={
#         'form':form
#     }
#     return render(request, 'lead_create.html',context)

def lead_create(request):
    form=LeadModelForm()
    # print(request.POST)
    if request.method=='POST':
        print('receiving post request')
        form=LeadModelForm(request.POST)
        if form.is_valid():
            # print('form is valid')
            # print(form.cleaned_data)

            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # age=form.cleaned_data['age']
            # agent=form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )
            # the above commented code is equal to
            form.save()


            print('The lead has been created')
            return redirect('/')


    context={
        'form':form
    }
    return render(request, 'lead_create.html',context)




    