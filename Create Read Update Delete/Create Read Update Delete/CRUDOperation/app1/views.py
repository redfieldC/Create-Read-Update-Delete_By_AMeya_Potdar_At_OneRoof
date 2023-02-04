from  django.shortcuts import render,redirect
from app1.models import EmpModel
from django.contrib import messages
from app1.serializers import CRUDSerializer, CrudSerializer

def showemp(request):
    showall = EmpModel.objects.filter(isactive=True)
    serializer = CRUDSerializer(showall,many=True)
    return render(request,'Index.html',{"data":serializer.data})

def Insertemp(request):
    if request.method == "POST":
       
        Updateemp = {}
        Updateemp['firstname']=request.POST.get('firstname')
        Updateemp['middlename']=request.POST.get('middlename')
        Updateemp['lastname']=request.POST.get('lastname')
        Updateemp['department']=request.POST.get('department')
        Updateemp['designation']=request.POST.get('designation')
        Updateemp['status']=request.POST.get('status')
        Updateemp['salary']=request.POST.get('salary')
        Updateemp['gender']=request.POST.get('gender')
        Updateemp['location']=request.POST.get('location')
        form = CRUDSerializer(data=Updateemp)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('app1:showemp')
        else:
            print(form.errors)
    else:
            return render(request,'Insert.html')


def Editemp(request,id):
    if request.method == 'GET':
        editempobj = EmpModel.objects.filter(id=id).first()
        s= CRUDSerializer(editempobj)
        return render(request,'Edit.html',{"EmpModel":s.data})
    else:
        Updateemp = {}
        
        d = EmpModel.objects.filter(id=id).first()
        if d:
            Updateemp['firstname']=request.POST.get('firstname')
            Updateemp['middlename']=request.POST.get('middlename')
            Updateemp['lastname']=request.POST.get('lastname')
            Updateemp['department']=request.POST.get('department')
            Updateemp['designation']=request.POST.get('designation')
            Updateemp['status']=request.POST.get('status')
            Updateemp['salary']=request.POST.get('salary')
            Updateemp['gender']=request.POST.get('gender')
            Updateemp['location']=request.POST.get('location')
        
       
            form = CRUDSerializer(d,data=Updateemp)
            if form.is_valid():
                form.save()
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('app1:showemp')
            else:
                print(form.errors)
    






def Delemp(request,id):
    delemployee = EmpModel.objects.get(id=id)
    Delemp={}
    Delemp['isactive']=False
    form = CrudSerializer(delemployee,data=Delemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Deleted Successfully...!:)')
        return redirect('app1:showemp')
    else:
        return redirect('app1:showemp')
    
