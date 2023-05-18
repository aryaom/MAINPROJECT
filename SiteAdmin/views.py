from django.conf import settings
from django.http.response import Http404
from django.shortcuts import render,redirect
from GroupAdmin.models import *
from Users.models import *
from SiteAdmin.models import *
from Mentors.models import *
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
import os
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"login.html")

def loginaction(request):
    ob = login.objects.filter(username=request.POST['txtuname'],
                                 password=request.POST['txtpswd'])
    if(ob.count()>0):
        request.session['id'] = ob[0].id
        return redirect('adminHome')
    else:
        ob = groupadmins.objects.filter(username=request.POST['txtuname'],
                                        password=request.POST['txtpswd'])
        if (ob.count() > 0):
            request.session['id']=ob[0].id
            return redirect('gHome')
        else:

            ob = mentorsregistration.objects.filter(username=request.POST['txtuname'],
                                            password=request.POST['txtpswd'],status='verified')
            if (ob.count() > 0):
                request.session['id'] = ob[0].id
                return redirect('mentorHome')
            else:
                ob = userregistration_tb.objects.filter(username=request.POST['txtpswd'],
                                                        password=request.POST['txtpswd'])
                if (ob.count() > 0):
                    request.session['id'] = ob[0].id
                    return redirect('uHome')
                else:
                    return render(request, "login.html", {'msg': 'Invalid Username or Password'})


@never_cache
def addgroups(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"admin/addgroups.html")

@never_cache
def addgroupaction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=addgroup.objects.filter(groups=request.POST["txtgroup"])
    if (ob.count()>0):
        return render(request,"admin/addgroups.html",{'msg2':'group already exist'})
    else :
        grup=addgroup(groups=request.POST['txtgroup'])
        grup.save()
        return render(request,"admin/addgroups.html",{'msg':'group added'})

@never_cache
def groupadminregistration (request):
    if 'id' not in request.session:
        return redirect('index')
    ob = addgroup.objects.all()
    return render(request,"admin/groupadminregistration.html",{'group':ob})

@never_cache
def grpadminRegisterAction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = groupadmins(name=request.POST['txtname'],
                     gender=request.POST['radgender'],
                     location=request.POST['txtlocation'],
                     mailid=request.POST['txtemail'],
                     phonenum=request.POST['txtphn'],
                     qualification=request.POST['qualification'],
                     experience=request.POST['experience'],
                     username=request.POST['txtuname'],
                     password=request.POST['txtpswd'],
                     group=request.POST['group'])
    ob.save()

    return render(request,"admin/groupadminregistration.html",{'msg':'registration successful'})

@never_cache
def viewgroups(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=addgroup.objects.all()
    return render(request,"admin/viewgroups.html",{'data':ob})

@never_cache
def deletegroup(request,gid):
    if 'id' not in request.session:
        return redirect('index')
    ob = addgroup.objects.filter(id=gid).delete()
    ob = addgroup.objects.all()
    return render(request,"admin/viewgroups.html",{'data':ob})

@never_cache
def deleteuser(request,uid):
    if 'id' not in request.session:
        return redirect('index')
    ob = userregistration_tb.objects.filter(id=uid).delete()
    ob = userregistration_tb.objects.all()
    return render(request,"admin/viewusers.html",{'data':ob})

@never_cache
def viewgroupadmin(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=groupadmins.objects.all()
    return render(request,"admin/viewgroupadmin.html",{'data':ob})

@never_cache
def deletegroupadmins(request,gid):
    if 'id' not in request.session:
        return redirect('index')
    ob = groupadmins.objects.filter(id=gid).delete()
    ob = groupadmins.objects.all()
    return render(request,"admin/viewgroupadmin.html",{'data':ob})

def checkUsernameGA(request):
    data={}
    obadmin=login.objects.filter(username=request.GET.get('username')).exists()
    obgrpadmin = groupadmins.objects.filter(username=request.GET.get('username')).exists()
    obmentor = mentorsregistration.objects.filter(username=request.GET.get('username')).exists()
    obuser = userregistration_tb.objects.filter(username=request.GET.get('username')).exists()
    if(obadmin or obgrpadmin or obmentor or obuser):
        data['k1']="exists"
    else:
        data['k1']="valid"
    return JsonResponse(data)

@never_cache
def changepasswordSA(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"admin/changepasswordSADMIN.html")

@never_cache
def changepwdSAaction(request):
     if 'id' not in request.session:
         return redirect('index')
     ob=login.objects.filter(password=request.POST["txtcurrentpwd"],id=request.session["id"])
     if(ob.count()>0):
         if(request.POST['txtnewpwd']==request.POST['txtretypepwd']):
             ob=login.objects.filter(id=request.session['id']).update(password=request.POST['txtnewpwd'])
             return render(request, "admin/changepasswordSADMIN.html",{'msg':'updated'})
         else:
             return render(request,"admin/changepasswordSADMIN.html",{'msg': 'retype password again'})
     else:
         return render(request,"admin/changepasswordSADMIN.html",{'msg':'invalid'})

@never_cache
def viewusers(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=userregistration_tb.objects.all()
    return render(request,"admin/viewusers.html",{'data':ob})

@never_cache
def viewmentorsADMIN(request,gid):
    if 'id' not in request.session:
        return redirect('index')
    ob = mentorsregistration.objects.filter(grpadmin_id=gid,status='verified')
    return render(request,"admin/viewmentors.html",{'data':ob})
@never_cache
def movetohomeA(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"admin/Register_base.html")

def ADMIN_logout(request):
    request.session.flush()
    return redirect('index')


#jquery ------------
@never_cache
def ViewMentorsQueryAndReply(request):
    if 'id' not in request.session:
        return redirect('index')
    obgroup=addgroup.objects.all()
    return render(request,"admin/ViewMentorsQueryAndReply_admin.html",{'group':obgroup})

@never_cache
def getMentors(request):
    if 'id' not in request.session:
        return redirect('index')
    group=request.GET.get('groups')
    print(group)
    obGroupAdmin=groupadmins.objects.filter(group=group)
    print("Gpid",obGroupAdmin[0].id)
    obMentors=mentorsregistration.objects.filter(grpadmin_id=obGroupAdmin[0].id)

    return render(request, "admin/ViewMentorsAjax.html", {'mentors': obMentors})

@never_cache
def getQueriesAndReply(request):
    if 'id' not in request.session:
        return redirect('index')
    mentor= request.GET.get('mentor_id')
    mentor_id=mentorsregistration.objects.get(id=mentor)
    obmentorquery=reply_mentor.objects.filter(mentor_id=mentor_id)
    return render(request, "admin/viewQueryAndReplyAjax.html",{'data':obmentorquery})


@never_cache
def blockmentorsSA(request):
    if 'id' not in request.session:
        return redirect('index')
    mentor = request.POST['ddlMentors']
    obbtn=mentorsregistration.objects.filter(id=mentor).update(status='blocked')
    return render(request,"admin/ViewMentorsQueryAndReply_admin.html",{'mentors':obbtn})

@never_cache
def viewblockedmentors(request):
    if 'id' not in request.session:
        return redirect('index')
    obmentor=mentorsregistration.objects.filter(status='blocked')
    return render(request, "admin/viewblockedmentors.html",{'data':obmentor})

@never_cache
def unblockmentors(request,gid):
    if 'id' not in request.session:
        return redirect('index')
    obstatus = mentorsregistration.objects.filter(id=gid).update(status='verified')
    return redirect('viewblockedmentors')

@never_cache
def viewcomplaintsSA(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = usercomplaints_tb.objects.all()
    return render(request,"admin/viewcomplaintsSA.html",{'data':ob})

@never_cache
def viewmentordetailsfromcomplaintSA(request,mid):
    if 'id' not in request.session:
        return redirect('index')
    ob=mentorsregistration.objects.filter(id=mid)
    return render(request,"admin/viewmentordetailsfromcomplaint.html",{'data':ob})

@never_cache
def viewuserdetailsfromcomplaintSA(request,uid):
    if 'id' not in request.session:
        return redirect('index')
    ob=userregistration_tb.objects.filter(id=uid)
    return render(request,"admin/viewuserdetailsfromcomplaint.html",{'data':ob})

def forgot_password(request):
    return render(request,"forgetpassword_verify.html")

def forgetpassword_verifyaction(request):
    ob=mentorsregistration.objects.filter(emailid=request.POST['txtmailid'],
                                          phoneno=request.POST['txtphn'],
                                          username=request.POST['txtuname'])
    if(ob.count()>0):
        return render(request,"forgetpassword_changingpwd.html",{"type":"mentor","username":ob[0].username})
    else:
        ob = userregistration_tb.objects.filter(mailid=request.POST['txtmailid'],
                                                phonenum=request.POST['txtphn'],
                                                username=request.POST['txtuname'])
        if (ob.count() > 0):
            return render(request, "forgetpassword_changingpwd.html", {"type": "user", "username": ob[0].username})
        else:
            ob = groupadmins.objects.filter(mailid=request.POST['txtmailid'],
                                                    phonenum=request.POST['txtphn'],
                                                    username=request.POST['txtuname'])
            if (ob.count() > 0):
                return render(request, "forgetpassword_changingpwd.html",{"type": "groupadmin", "username": ob[0].username})
            else:
                return render(request, "forgetpassword_verify.html",{'msg':'invalid user'})

def forgetpassword_updateAction(request):
    print("helooooo")
    if(request.POST['txtnewpwd']==request.POST['txtretypepwd']):
        if(request.POST['hdn_type']=="mentor"):
            print("mentorrr")
            ob=mentorsregistration.objects.filter(username=request.POST['hdn_uname']).update(password=request.POST['txtnewpwd'])
            return render(request, "forgetpassword_changingpwd.html",{'msg':'password updated successfully'})
        else:
            if(request.POST['hdn_type']=="user"):
                print("userrrrrrr")
                ob = userregistration_tb.objects.filter(username=request.POST['hdn_uname']).update(password=request.POST['txtnewpwd'])
                return render(request, "forgetpassword_changingpwd.html",{'msg':'password updated successfully'})
            else:
                if(request.POST['hdn_type']=="groupadmin"):
                    print("gruuppp")
                    ob = groupadmins.objects.filter(username=request.POST['hdn_uname']).update(password=request.POST['txtnewpwd'])
                    return render(request, "forgetpassword_changingpwd.html",{'msg':'password updated successfully'})
                else:
                    return render(request, "forgetpassword_changingpwd.html",{'msg':'Try again'})
    else:
        return render(request, "forgetpassword_changingpwd.html",{'msg':'Try again'})

@never_cache
def addpattern(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"admin/addpatterns.html")

@never_cache
def addpatternaction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=pattern.objects.filter(patternname=request.POST['txtpattern'])
    if(ob.count()>0):
        return render(request,"admin/addpatterns.html",{'msggg':'asderr'})
    else:
        ob=pattern(patternname=request.POST['txtpattern'])
        ob.save()
        return render(request,"admin/addpatterns.html",{'msg':'asd'})

@never_cache
def viewpattern(request):
    if 'id' not in request.session:
        return redirect('index')
    ob=pattern.objects.all()
    return render(request,"admin/viewpatterns.html",{'data':ob})
@never_cache
def deletepattern(request,pid):
    if 'id' not in request.session:
        return redirect('index')
    ob=pattern.objects.filter(id=pid).delete()
    ob=pattern.objects.all()
    return render(request, "admin/viewpatterns.html",{'data':ob})

@never_cache
def adminHome(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,'admin/Register_base.html')

# def download(request,path):
#     filepath=os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(filepath):
#         with open(filepath,'rb') as f:
#             response=HttpResponse(f.read(),content_type="application/fileupload")
#             response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
#             return response
#     return Http404


