from django.shortcuts import render,redirect

from Users.models import *
from SiteAdmin.models import *
from Users.models import *
from Mentors.models import *
from django.http import JsonResponse
from GroupAdmin.models import *
import datetime
from django.views.decorators.cache import never_cache


# Create your views here.
def checkUsername(request):
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
def changepwdMENTOR(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"mentors/changepasswordMENTOR.html")

@never_cache
def changepwd_MENTORaction(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = mentorsregistration.objects.filter(password=request.POST["txtcurrentpwd"], id=request.session["id"])
    if (ob.count() > 0):
        if (request.POST['txtnewpwd'] == request.POST['txtretypepwd']):
            ob = mentorsregistration.objects.filter(id=request.session['id']).update(password=request.POST['txtnewpwd'])
            return render(request, "mentors/changepasswordMENTOR.html", {'msg': 'Updated Successfully...'})
        else:
            return render(request, "mentors/changepasswordMENTOR.html", {'msg': 'Retype Password Again'})
    else:
        return render(request, "mentors/changepasswordMENTOR.html", {'msg': 'Invalid'})

@never_cache
def viewprofileMENTOR(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = mentorsregistration.objects.filter(id=request.session['id'])
    return render(request, "mentors/viewprofileMENTOR.html",{'data':ob})

@never_cache
def updateMENTORprofile(request):
    if 'id' not in request.session:
        return redirect('index')
    ob = mentorsregistration.objects.filter(id=request.session['id']).update(mentorname=request.POST['txtfname'],
                                                                             gender=request.POST['radgender'],
                                                                             location=request.POST['txtlocation'],
                                                                             emailid=request.POST['txtemail'],
                                                                             phoneno=request.POST['txtphn'],
                                                                             qualification=request.POST[
                                                                                 'qualification'],
                                                                             experience=request.POST['experience'])
    ob = mentorsregistration.objects.filter(id=request.session['id'])
    return render(request, "mentors/viewprofileMENTOR.html", {'data': ob})

@never_cache
def viewallocatedqueryM(request):
    if 'id' not in request.session:
        print('hh')
        return redirect('index')
    obmentor=mentorsregistration.objects.get(id=request.session['id'])
    ob=QueryAllocation.objects.filter(mentorid_id=obmentor,status='Allocated')
    
    return render(request,"mentors/viewallocatedqueryM.html",{'data':ob})

@never_cache
def replyMENTOR(request,mid):
    if 'id' not in request.session:
        return redirect('index')

    print("helloooo",mid)
    ob = QueryAllocation.objects.filter(id=mid)
    #qid=ob[0].queryid_id
    #ob=addqueryUSER_tb.objects.filter(id=qid)
    return render(request,"mentors/reply.html",{'data':ob})

@never_cache
def replyactionMENTOR(request):
    if 'id' not in request.session:
        return redirect('index')
    chi=0
    chi_square=0
    tot=0
    max_chi_sq_Tot=0
    min_chi_sq_Tot=0

    max_chi_sq_Tot_file=0
    min_chi_sq_Tot_file=0
    
    chi_status=0
    chi_status_file=0
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
    mid=mentorsregistration.objects.get(id=request.session["id"])
    post=request.POST['txtreply']
    postar=post.split(' ')
    print("count",len(postar))
    for p in postar:
        print(p)
        
  
    filtered_sentence = [] 
  
    
    for p in postar:    
        filtered_sentence.append(p)
    #--------------

    
    for filt in filtered_sentence:
        patterns_queryset=pattern.objects.filter(patternname=filt)
        if patterns_queryset.count()>0:
            
            #print(pn.patternname)
            observed=observed+1
            
    print("observed",observed)
    if(observed>0):
        obmentor= mentorsregistration.objects.filter(id=request.session["id"])
        grp_admin_id=obmentor[0].grpadmin_id_id
        ob_groupadmins=groupadmins.objects.filter(id=grp_admin_id)
        group_name=ob_groupadmins[0].group

        print('group',group_name)
        objexpected=expectedchisquare_tb.objects.filter(groupname=group_name)
        if objexpected.count()>0:
             expected_value=int(objexpected[0].expected_chi_value)
             chi=int(observed-expected_value)
             print('chi',chi)
             chi_square=int(chi*chi)
             tot=int(chi_square/expected_value)
             print(observed)
             #print(expected_chi_value)
             print(chi_square)
             print("chisq",tot)
             max_chi_sq_Tot=tot+2
             min_chi_sq_Tot=tot-2
             objValue=p1_tb.objects.filter(v1__gte=min_chi_sq_Tot, v1__lte=max_chi_sq_Tot)
             if objValue.count()>0:
                 p1_value=objValue[0].v1
                 chi_status=1
             else:
                 print("no expected value")
             print("chi_status",chi_status)
             if(chi_status==1):
                 Reply_Status_post="Suspicious"  
    
    
                
        
        

    pic='nouploads'
    picname='No File'
    if len(request.FILES) != 0:
        pic = request.FILES['upload']
        print(pic)
    
    obmentor=  mentorsregistration.objects.get(id=request.session["id"])  
    ob = QueryAllocation.objects.filter(id=request.POST['hdn'])
    query_id=ob[0].queryid_id
    obQuery = addqueryUSER_tb.objects.get(id=query_id)
    print("Reply_Status_post",Reply_Status_post)
    reply_id=1
    obreply=reply_mentor.objects.filter( mentor_id=obmentor).order_by('-id')
    if obreply.count()>0:
        reply_id=int(obreply[0].id)
        reply_id+=1

    import os
    if pic!='nouploads':
        filtered_sentence_file = []
        filecontents=pic.read()
        print("content:",filecontents)
        print(pic.content_type)
        f, e = os.path.splitext(pic.name)
        if e==".txt" or e==".doc" or e==".docx":
            path="./reply_uploads/"+str(reply_id)+"_"+str(pic.name)
            filecontents=str(filecontents)
            filecontents=filecontents.replace("b'","")
            filecontents=filecontents.replace("'","")
            with open(path,"w") as f_create:
                f_create.write(str(filecontents))
                f_create.close()
            
        
            with open(path, "r") as f:
                for l in f:

                    example_sent_file = ""
                   
                    postar_file = l.split(' ')
                    print("count", len(postar_file))
                    for pfile in postar_file:
                        print(pfile)
                   
                    for pfile in postar_file:
                        print(pfile)    
                        filtered_sentence_file.append(pfile)
                  
        
        else:
             return render(request, "mentors/reply.html",{'data':ob,'msg_invalid':'InvalidUploads'})

       
        for filt in filtered_sentence_file:
            patterns_queryset=pattern.objects.filter(patternname=filt)
            if patterns_queryset.count()>0:
            
                #print(pn.patternname)
                observed_file=observed_file+1
            
        print("observed",observed_file)
        if(observed_file>0):
            obmentor= mentorsregistration.objects.filter(id=request.session["id"])
            grp_admin_id=obmentor[0].grpadmin_id_id
            ob_groupadmins=groupadmins.objects.filter(id=grp_admin_id)
            group_name=ob_groupadmins[0].group

            print('group',group_name)
            objexpected=expectedchisquare_tb.objects.filter(groupname=group_name)
            if objexpected.count()>0:
                expected_value_file=int(objexpected[0].expected_chi_value)
                chi_file=int(observed_file-expected_value_file)
                print('chi',chi_file)
                chi_square_file=int(chi_file*chi_file)
                tot_file=int(chi_square_file/expected_value_file)
                print(observed)
                #print(expected_chi_value)
                print(chi_square)
                print("chisq",tot)
                max_chi_sq_Tot_file=tot_file+2
                min_chi_sq_Tot_file=tot_file-2
                objValue=p1_tb.objects.filter(v1__gte=min_chi_sq_Tot, v1__lte=max_chi_sq_Tot)
                if objValue.count()>0:
                     p1_value=objValue[0].v1
                     chi_status_file=1
                else:
                     print("no expected value")
                print("chi_status",chi_status)
                if(chi_status_file==1):
                     Reply_Status_file="Suspicious"
        picname=str(obQuery.id)+'R_'+str(pic.name)

   
        
    #obquery = addqueryUSER_tb.objects.get(id=request.POST['hdn'])
    obmentor = mentorsregistration.objects.get(id=request.session['id'])
    #ob = reply_mentor(query_id=obquery,mentor_id=obmentor,reply=request.POST['txtreply'], fileupload=pic,  date=datetime.datetime.now(), status='pending')
    #ob.save()
    print("Reply_Status_file",Reply_Status_file)
    
    ob = reply_mentor(query_id=obQuery,mentor_id=obmentor,reply=request.POST['txtreply'], fileupload=picname,  date=datetime.datetime.now(), status_post=Reply_Status_post,status_file=Reply_Status_file)
    ob.save()
    
    if(Reply_Status_post=="Valid" and Reply_Status_file=="Valid" ):
        ob = QueryAllocation.objects.filter(id=request.POST['hdn']).update(status='Replied')
        ob = QueryAllocation.objects.filter(id=request.POST['hdn'])
        query_id=ob[0].queryid_id
        obQuery = addqueryUSER_tb.objects.filter(id=query_id).update(status='Replied')
                    
    ob = QueryAllocation.objects.filter(id=request.POST['hdn'])
    return render(request, "mentors/reply.html",{'data':ob,'msg':'aa'})

@never_cache
def viewqueryandreplyMENTOR(request):
    if 'id' not in request.session:
        return redirect('index')
    mentorid = mentorsregistration.objects.get(id=request.session['id'])
    ob = reply_mentor.objects.filter(mentor_id=request.session['id'])
    return render(request,"mentors/viewqueryandreplyMENTOR.html", {'data': ob})

def MENTOR_logout(request):
    request.session.flush()
    return redirect('index')

@never_cache
def viewcomplaintsMentor(request):
    if 'id' not in request.session:
        return redirect('index')
    obmentorid=mentorsregistration.objects.get(id=request.session['id'])
    ob=usercomplaints_tb.objects.filter(mentor_id=obmentorid)
    return render(request,"mentors/viewcomplaintsMentor.html",{'data':ob})

@never_cache
def mentorHome(request):
    if 'id' not in request.session:
        return redirect('index')
    return render(request,"mentors/Register_base.html")
