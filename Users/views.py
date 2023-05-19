from django.shortcuts import render,redirect

from Mentors.models import *
from GroupAdmin.models import *
from Users.models import *
from django.http import JsonResponse

import datetime
from django.views.decorators.cache import never_cache


# Create your views here.
def userregistration(request):
    return render(request,"userregistration.html")

def userregistrationaction(request):

    ob = userregistration_tb( fname=request.POST['fname'],lastname=request.POST['lname'],
                          location=request.POST['txtlocation'],
                          pincode=request.POST['txtpincode'],
                          mailid=request.POST['txtemail'],
                          phonenum=request.POST['txtphn'],
                          qualification=request.POST['qualification'],
                          experience=request.POST['experience'],
                          username=request.POST['txtuname'],
                          password=request.POST['pwd'])
    ob.save()
    return render(request,"userregistration.html",{"msg" : "Registration was successfull..."})

def checkUsernameUSER(request):
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
def changepwdUSER(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"users/changepasswordUSER.html")

@never_cache
def changepwd_USERaction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = userregistration_tb.objects.filter(password=request.POST["txtcurrentpwd"], id=request.session["id"])
    if (ob.count() > 0):
        if (request.POST['txtnewpwd'] == request.POST['txtretypepwd']):
            ob = userregistration_tb.objects.filter(id=request.session['id']).update(password=request.POST['txtnewpwd'])
            return render(request, "users/changepasswordUSER.html", {'msg': 'updated'})
        else:
            return render(request, "users/changepasswordUSER.html", {'msg': 'retype password again'})
    else:
        return render(request, "users/changepasswordUSER.html", {'msg': 'invalid'})

@never_cache
def addqueryUSER(request):
    if 'id' not in request.session:
        return redirect('index')
    grp = addgroup.objects.all()
    return render(request, "users/addqueryUSER.html", {'group': grp})


@never_cache
def addqueryactionUSER(request):
    if 'id' not in request.session:
        return redirect('index')

    Reply_Status_post="Valid"
    Reply_Status_file="Valid"
    observed=0
    observed_file=0
    
    example_sent=""
    pstatus="Good"
    category=""
    cnt_illegal=0
    cnt_res=0
    cnt_bad=0
    query_id=1
    uid=userregistration_tb.objects.get(id=request.session["id"])

    obQuery= ob = addqueryUSER_tb.objects.filter(user_id=uid).order_by('-id')
    if obQuery.count()>0:
        query_id=int(obQuery[0].id)
        query_id+=1
    print('query_id',query_id)
    
    post=request.POST['txtaddquery']
    postar=post.split(' ')
    print("count",len(postar))
    for p in postar:
        print(p)
        
    filtered_sentence = [] 
  
    
    for p in postar:    
        filtered_sentence.append(p)
    
    
    for filt in filtered_sentence:
        patterns_queryset=pattern.objects.filter(patternname=filt)
        if patterns_queryset.count()>0:
            
            #print(pn.patternname)
            observed=observed+1
            
    print("observed",observed)
    if(observed>0):
        Reply_Status_post="Suspicious"
        
    pic='nouploads'
    picname='No File'
    if len(request.FILES) != 0:
        pic = request.FILES['upload']
        print(pic)
    import os
    if pic!='nouploads':
        filtered_sentence_file = []
        filecontents=pic.read()
        print("content:",filecontents)
        print(pic.content_type)
        f, e = os.path.splitext(pic.name)
        if e==".txt" or e==".doc" or e==".docx":
            path="./query_uploads/"+str(query_id)+"_"+str(pic.name)
            filecontents=str(filecontents)
            filecontents=filecontents.replace("b'","")
            filecontents=filecontents.replace("'","")
            with open(path,"w") as f_create:
                f_create.write(str(filecontents))
                f_create.close()
            
        
            with open(path, "r") as f:
                for l in f:

                    example_sent_file = ""
                    # stemming and stop word removal
                    postar_file = l.split(' ')
                    print("count", len(postar_file))
                    for pfile in postar_file:
                        print(pfile)
                    
                    for pfile in postar_file:
                        print(pfile)    
                        filtered_sentence_file.append(pfile)
                  
        
        else:
            
            grp = addgroup.objects.all()
            
            return render(request, "users/addqueryUSER.html",{'group':grp, 'data':ob,'msg_invalid':'InvalidUploads'})

       
        for filt in filtered_sentence_file:
            patterns_queryset=pattern.objects.filter(patternname=filt)
            if patterns_queryset.count()>0:
            
                #print(pn.patternname)
                observed_file=observed_file+1
            
        print("observed",observed_file)
        if(observed_file>0):
            Reply_Status_file="Suspicious"
        picname=str(query_id)+"_"+str(pic.name)
    print('Reply_Status_post',Reply_Status_post)
    print('Reply_Status_file',Reply_Status_file)
    ob = addqueryUSER_tb(subject=request.POST['txtsubject'],
                      addquery=request.POST['txtaddquery'],
                      fileupload=picname,
                      group=request.POST['group'],
                      user_id=uid,
                      date=datetime.datetime.now(),
                      status_post=Reply_Status_post,
                      status_file=Reply_Status_file  )
    ob.save()








   
    grp = addgroup.objects.all()
    return render(request, "users/addqueryUSER.html",{'group':grp,'msg':'query added'})


@never_cache
def viewprofileUSER(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = userregistration_tb.objects.filter(id=request.session['id'])
    return render(request,"users/viewprofileUSER.html",{'data': ob})

@never_cache
def viewprofileUSERaction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = userregistration_tb.objects.filter(id=request.session['id']).update(fname=request.POST['txtfname'],
                                                                             lastname=request.POST['lname'],
                                                                            gender=request.POST['radgender'],
                                                                           location=request.POST['txtlocation'],
                                                                            pincode=request.POST['txtpincode'],
                                                                     mailid=request.POST['txtemail'],
                                                                     phonenum=request.POST['txtphn'],
                                                                     qualification=request.POST['qualification'],
                                                                     experience=request.POST['experience'],
                                                                     designation=request.POST['designation'],
                                                                     companyname=request.POST['cname'],)
    ob = userregistration_tb.objects.filter(id=request.session['id'])
    return render(request, "users/viewprofileUSER.html", {'data': ob, 'msg':'profile edited'})

@never_cache
def viewqueryUSER(request):
    if 'id' not in request.session:
        return redirect('index')
    obuserid=userregistration_tb.objects.get(id=request.session['id'])
    ob=reply_mentor.objects.filter(query_id__in=addqueryUSER_tb.objects.filter(user_id=obuserid.id,status='Replied').values('id'))
    return render(request, "users/viewRepliedqueryUSER.html", {'data': ob})

@never_cache
def view_pendingqueryUSER(request):
    if 'id' not in request.session:
        return redirect('index')
    obuserid = userregistration_tb.objects.get(id=request.session['id'])
    ob=addqueryUSER_tb.objects.filter(user_id=obuserid.id).exclude(status='Allocated')
    return render(request, "users/view_pendingqueryUSER.html", {'data': ob})
@never_cache
def movetohome(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"login.html")

def user_logout(request):
    request.session.flush()
    return redirect('index')

@never_cache
def viewrepliedmentors_details(request,mid):
    if 'id' not in request.session:
        return redirect('index')
    obmentor = mentorsregistration.objects.filter(id=mid)
    return render(request,"users/viewrepliedmentordetails.html",{'data':obmentor})

@never_cache
def complaint(request):
    if 'id' not in request.session:
        return redirect('index')
    obmentor=mentorsregistration.objects.all()
    return render(request,"users/addcomplaint.html",{'mentor':obmentor})

@never_cache
def complaintaction(request):
    if 'id' not in request.session:
        return redirect('index')
    obuid=userregistration_tb.objects.get(id=request.session['id'])
    obmid=mentorsregistration.objects.get(id=request.POST['Mentorddl'])
    ob = usercomplaints_tb(about=request.POST['txtsubject'],
                           details=request.POST['txtdetails'],
                           date=datetime.datetime.now(),
                           mentor_id=obmid,
                           user_id=obuid)
    ob.save()
    obmentor = mentorsregistration.objects.all()
    return render(request,"users/addcomplaint.html",{'mentor':obmentor,'msg':'msgg'})

@never_cache
def uHome(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,'users/Register_base.html')
