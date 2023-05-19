from django.shortcuts import render,redirect
from SiteAdmin.models import *
from GroupAdmin.models import *
from Users.models import *
from django.http import JsonResponse
import datetime
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def viewprofile(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = groupadmins.objects.filter(id=request.session['id'])
    return render(request, "groupadmin/viewprofile.html", {'data': ob})

@never_cache
def updategrupadminprofile(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = groupadmins.objects.filter(id=request.session['id']).update(name=request.POST['txtname'],
                                                                           gender=request.POST['radgender'],
                                                                           location=request.POST['txtlocation'],
                                                                           mailid=request.POST['txtemail'],
                                                                           phonenum=request.POST['txtphn'],
                                                                           qualification=request.POST['qualification'],
                                                                           experience=request.POST['experience'])
    ob = groupadmins.objects.filter(id=request.session['id'])
    return render(request, "groupadmin/viewprofile.html", {'data': ob})

@never_cache
def addmentors(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request, "groupadmin/addmentors.html")

@never_cache
def addmentoraction(request):
    if 'id' not in request.session:
        return redirect('index')
    obgrp = groupadmins.objects.get(id=request.session['id'])
    ob = mentorsregistration(mentorname=request.POST['mname'],
                              gender=request.POST['radgender'],
                              location=request.POST['txtlocation'],
                              emailid=request.POST['txtemail'],
                              phoneno=request.POST['txtphn'],
                              qualification=request.POST['qualification'],
                              experience=request.POST['experience'],
                              username=request.POST['txtuname'],
                              password=request.POST['pwd'],
                              status="verified",
                              grpadmin_id=obgrp)
    ob.save()
    return render(request, "groupadmin/addmentors.html", {'msg': 'Added Successfully'})

@never_cache
def viewmentors(request):
    if 'id' not in request.session:
        return redirect('index')
    obgrp = groupadmins.objects.get(id=request.session['id'])
    ob = mentorsregistration.objects.filter(grpadmin_id=obgrp,status='verified')
    return render(request,"groupadmin/viewmentors.html",{'data':ob})

@never_cache
def deletementors(request,mid):
    if 'id' not in request.session:
        return redirect('index')
    obgrp = groupadmins.objects.get(id=request.session['id'])
    ob = mentorsregistration.objects.filter(id=mid).delete()
    ob = mentorsregistration.objects.filter(grpadmin_id=obgrp)
    return render(request,"groupadmin/viewmentors.html",{'data':ob})

def checkUsernameMENTOR(request):
    data={}
    obadmin=login.objects.filter(username=request.GET.get('username')).exists()
    obgrpadmin = groupadmins.objects.filter(username=request.GET.get('username')).exists()
    obmentor = mentorsregistration.objects.filter(username=request.GET.get('username')).exists()
    obuser = userregistration_tb.objects.filter(username=request.GET.get('username')).exists()
    if(obadmin or obgrpadmin or obmentor ):
        data['k1']="exists"
    else:
        data['k1']="valid"
    return JsonResponse(data)

@never_cache
def changepwdGA(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"groupadmin/changepasswordGADMIN.html")


@never_cache
def changepwdGAaction(request):
    if 'id' not in request.session:
        return redirect('index')
    print('checking')
    ob = groupadmins.objects.filter(password=request.POST["txtcurrentpwd"], id=request.session["id"])
    if (ob.count() > 0):
        print('chec')
        if (request.POST['txtnewpwd'] == request.POST['txtretypepwd']):
            print('checkingnn')
            ob = groupadmins.objects.filter(id=request.session['id']).update(password=request.POST['txtnewpwd'])
            return render(request, "groupadmin/changepasswordGADMIN.html", {'msg': 'updated'})
        else:
            return render(request, "groupadmin/changepasswordGADMIN.html", {'msg': 'retype password again'})
    else:
        print('che')
        return render(request, "groupadmin/changepasswordGADMIN.html", {'msg': 'invalid'})

@never_cache
def viewqueryGA(request):
    if 'id' not in request.session:
        return redirect('index')
    obgrp = groupadmins.objects.get(id=request.session['id'])
    obMentor = mentorsregistration.objects.filter(grpadmin_id=obgrp)
    ob=groupadmins.objects.filter(id=request.session["id"])
    obgrp=ob[0].group
    obquery=addqueryUSER_tb.objects.filter(group=obgrp,status='pending')
    return render(request, "groupadmin/viewquery.html", {'data': obquery,'mentor':obMentor})

@never_cache
def DeleteQuery(request,qid):
    if 'id' not in request.session:
        return redirect('index')
    print("helooo")
    obgrp = groupadmins.objects.get(id=request.session['id'])
    ob = mentorsregistration.objects.filter(grpadmin_id=obgrp)
    obquery=addqueryUSER_tb.objects.filter(id=qid).update(status='delete')
    obgrp = groupadmins.objects.get(id=request.session['id'])
    obMentor = mentorsregistration.objects.filter(grpadmin_id=obgrp)
    ob = groupadmins.objects.filter(id=request.session["id"])
    obgrp = ob[0].group
    obquery = addqueryUSER_tb.objects.filter(group=obgrp,status='pending')
    return render(request, "groupadmin/viewquery.html", {'data': obquery, 'mentor': obMentor})

@never_cache
def scheduleQueryAction(request):
    if 'id' not in request.session:
        return redirect('index')
    qids=request.POST.getlist('chk[]')
    for qid in qids:
        obMentor=mentorsregistration.objects.get(id=request.POST['ddlmentor'])
        obquery = addqueryUSER_tb.objects.get(id=qid)
        obAllocate=QueryAllocation(mentorid=obMentor,queryid=obquery,status='Allocated',date=datetime.datetime.now())

        obAllocate.save()
        obquery = addqueryUSER_tb.objects.filter(id=qid).update(status='Allocated')

    obgrp = groupadmins.objects.get(id=request.session['id'])
    obMentor = mentorsregistration.objects.filter(grpadmin_id=obgrp)
    ob = groupadmins.objects.filter(id=request.session["id"])
    obgrp = ob[0].group
    print('group',obgrp)
    obquery = addqueryUSER_tb.objects.filter(group=obgrp,status='pending')
    return render(request, "groupadmin/viewquery.html", {'data': obquery, 'mentor': obMentor})


def groupadmin_logout(request):
    request.session.flush()
    return redirect('index')

@never_cache
def backtohomeGA(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"groupadmin/Register_base.html")

@never_cache  
def viewusercomplaintsGA(request):
    if 'id' not in request.session:
        return redirect('index')
    obgaid=groupadmins.objects.get(id=request.session['id'])
    obmentor = mentorsregistration.objects.filter(grpadmin_id=obgaid)
    ob = usercomplaints_tb.objects.filter(mentor_id__in= mentorsregistration.objects.filter(grpadmin_id=obgaid))
    return render(request,"groupadmin/viewusercomplaintsGA.html",{'data':ob})

@never_cache
def viewmentordetailsfromcomplaintsGA(request,mid):
    if 'id' not in request.session:
        return redirect('index')
    complaint_count=0
    ob=mentorsregistration.objects.filter(id=mid,status='verified')
    obmentor=mentorsregistration.objects.get(id=mid)
    obcomplaints=usercomplaints_tb.objects.filter(mentor_id=obmentor)
    if(obcomplaints.count()>0):
        complaint_count=obcomplaints.count()

    return render(request,"groupadmin/viewmentordetailsfromcomplaintsGA.html",{'data':ob,'count':complaint_count})

@never_cache
def viewuserdetailsfromcomplaintsGA(request,uid):
    if 'id' not in request.session:
        return redirect('index')
    ob=userregistration_tb.objects.filter(id=uid)
    return render(request,"groupadmin/viewuserdetailsfromcomplaintsGA.html",{'data':ob})

@never_cache
def deactivateMentorfromcomplaint(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = mentorsregistration.objects.filter(id=request.POST['hdnid']).update(status='deactivated')
    ob = mentorsregistration.objects.filter(id=request.POST['hdnid'])
    return render(request,"groupadmin/viewmentordetailsfromcomplaintsGA.html",{'data':ob,'msg':' Your mentor is deactivated'})

@never_cache
def gHome(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,'groupadmin/Register_base.html')



