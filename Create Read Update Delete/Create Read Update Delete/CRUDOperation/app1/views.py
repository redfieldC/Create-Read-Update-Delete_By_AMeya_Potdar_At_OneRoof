from  django.shortcuts import render,redirect
from app1.models import EmpModel
from django.contrib import messages
from app1.serializers import CRUDSerializer, CrudSerializer

def showemp(request):
    showall = EmpModel.objects.filter(isactive=True)
    print(showall)
    serializer = CRUDSerializer(showall,many=True)
    print(serializer.data)
    return render(request,'Index.html',{"data":serializer.data})

def Insertemp(request):
    if request.method == "POST":
        # if request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('department') and request.POST.get('designation') and request.POST.get('location') and request.POST.get('status') and request.POST.get('salary') and request.POST.get('gender'):
        #     saverecord = EmpModel()
        #     saverecord.firstname = request.POST.get('firstname')
        #     saverecord.middlename = request.POST.get('middlename')
        #     saverecord.lastname = request.POST.get('lastname')
        #     saverecord.location = request.POST.get('location')
        #     saverecord.designation = request.POST.get('designation')
        #     saverecord.department = request.POST.get('department')
        #     saverecord.status = request.POST.get('status')
        #     saverecord.salary = request.POST.get('salary')
        #     saverecord.gender = request.POST.get('gender')
        #     saverecord.save()
        #     messages.success(request,'Employee ' + saverecord.firstname + ' is saved successfully :)!')
        #     return render(request,'Insert.html')
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
            print("hkjk",form.data)
            messages.success(request,'Record Updated Successfully...!:)')
            return redirect('app1:showemp')
        else:
            print(form.errors)
    else:
            return render(request,'Insert.html')


def Editemp(request,id):
    if request.method == 'GET':
        print('GET',id)
        editempobj = EmpModel.objects.filter(id=id).first()
        s= CRUDSerializer(editempobj)
        return render(request,'Edit.html',{"EmpModel":s.data})
    else:
        print('POST',id)
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
            print(Updateemp)
        # Updateemp = EmpModel.objects.get(id=id)
            #print(Updateemp)
            form = CRUDSerializer(d,data=Updateemp)
            if form.is_valid():
                form.save()
                print("hkjk",form.data)
                messages.success(request,'Record Updated Successfully...!:)')
                return redirect('app1:showemp')
            else:
                print(form.errors)
    



# def updateemp(request,id):
#     # Updateemp = {}
#     # if request.method=='POST':
#     #     data = EmpModel.objects.get(id=id)
#     #     if data:
#     #         Updateemp['firstname']=request.POST.get('firstname')
#     #         Updateemp['middlename']=request.POST.get('middlename')
#     #         Updateemp['lastname']=request.POST.get('lastname')
#     #         Updateemp['department']=request.POST.get('department')
#     #         Updateemp['designation']=request.POST.get('designation')
#     #         Updateemp['status']=request.POST.get('status')
#     #         Updateemp['salary']=request.POST.get('salary')
#     #         Updateemp['gender']=request.POST.get('gender')
#     #     # Updateemp = EmpModel.objects.get(id=id)
#     #         #print(Updateemp)
#     #         form = CRUDSerializer(data,data=Updateemp)
#     #         if form.is_valid():
#     #             form.save()
#     #             messages.success(request,'Record Updated Successfully...!:)')
#     #             return render(request,'Edit.html',{"EmpModel":Updateemp})
#     # return render(request,'Edit.html',Updateemp)


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
        print("sfsdrf",form.errors)
        return redirect('app1:showemp')
    
