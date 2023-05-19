"""suspiciousdiscussion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path
from django.urls import include,re_path as url
from SiteAdmin import views as siteadmin_view
from GroupAdmin import views as groupadmin_view
from Mentors import views as mentors_view
from Users import views as users_view
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',siteadmin_view.index,name='index'),
    url(r'^loginaction/',siteadmin_view.loginaction,name='loginaction'),
    url(r'^addgroups/',siteadmin_view.addgroups,name='addgroups'),
    url(r'^addgroupaction/',siteadmin_view.addgroupaction,name='addgroupaction'),
    url(r'^groupadminregistration/',siteadmin_view.groupadminregistration,name='groupadminregistration'),
    url(r'^grpadminRegisterAction/',siteadmin_view.grpadminRegisterAction,name='grpadminRegisterAction'),
    url(r'^viewgroups/',siteadmin_view.viewgroups,name='viewgroups'),
    url(r'^deletegroup/(?P<gid>\d+)/$',siteadmin_view.deletegroup,name='deletegroup'),
    url(r'^deleteuser/(?P<uid>\d+)/$',siteadmin_view.deleteuser,name='deleteuser'),
    url(r'^viewgroupadmin/', siteadmin_view.viewgroupadmin, name='viewgroupadmin'),
    url(r'^deletegroupadmins/(?P<gid>\d+)/$', siteadmin_view.deletegroupadmins, name='deletegroupadmins'),
    url(r'^viewprofile/', groupadmin_view.viewprofile, name='viewprofile'),
    url(r'^updategrupadminprofile/', groupadmin_view.updategrupadminprofile, name='updategrupadminprofile'),
    url(r'^addmentors/',groupadmin_view.addmentors,name='addmentors'),
    url(r'^addmentoraction/',groupadmin_view.addmentoraction,name='addmentoraction'),
    url(r'^viewmentors/',groupadmin_view.viewmentors,name='viewmentors'),
    url(r'^deletementors/(?P<mid>\d+)/$', groupadmin_view.deletementors, name='deletementors'),
    url(r'^userregistration/', users_view.userregistration, name='userregistration'),
    url(r'^userregistrationaction/',users_view.userregistrationaction,name='userregistrationaction'),
    url(r'^checkUsernameGA/', siteadmin_view.checkUsernameGA, name='checkUsernameGA'),
    url(r'^checkUsernameMENTOR/',groupadmin_view.checkUsernameMENTOR, name='checkUsernameMENTOR'),
    url(r'^checkUsernameUSER/',users_view.checkUsernameUSER, name='checkUsernameUSER'),
    url(r'^changepasswordSA/',siteadmin_view.changepasswordSA, name='changepasswordSA'),
    url(r'^changepwdSAaction/',siteadmin_view.changepwdSAaction, name='changepwdSAaction'),
    url(r'^changepwdGA/',groupadmin_view.changepwdGA, name='changepwdGA'),
    url(r'^changepwdGAaction/', groupadmin_view.changepwdGAaction, name='changepwdGAaction'),
    url(r'^changepwdUSER/',users_view.changepwdUSER, name='changepwdUSER'),
    url(r'^changepwd_USERaction/',users_view.changepwd_USERaction, name='changepwd_USERaction'),
    url(r'^changepwdMENTOR/',mentors_view.changepwdMENTOR, name='changepwdMENTOR'),
    url(r'^changepwd_MENTORaction/',mentors_view.changepwd_MENTORaction, name='changepwd_MENTORaction'),
    url(r'^addqueryUSER/', users_view.addqueryUSER, name='addqueryUSER'),
    url(r'^addqueryactionUSER/', users_view.addqueryactionUSER, name='addqueryactionUSER'),
    url(r'^viewqueryUSER/', users_view.viewqueryUSER, name='viewqueryUSER'),
    url(r'^viewprofileUSER/', users_view.viewprofileUSER, name='viewprofileUSER'),
    url(r'^viewprofileUSERaction/', users_view.viewprofileUSERaction, name='viewprofileUSERaction'),
    url(r'^viewusers/', siteadmin_view.viewusers, name='viewusers'),
    url(r'^viewmentorsADMIN/(?P<gid>\d+)/$', siteadmin_view.viewmentorsADMIN, name='viewmentorsADMIN'),
    url(r'^viewqueryGA/', groupadmin_view.viewqueryGA, name='viewqueryGA'),
    url(r'^viewprofileMENTOR/', mentors_view.viewprofileMENTOR, name='viewprofileMENTOR'),
    url(r'^updateMENTORprofile/', mentors_view.updateMENTORprofile, name='updateMENTORprofile'),
    url(r'^DeleteQuery/(?P<qid>\d+)/$', groupadmin_view.DeleteQuery, name='DeleteQuery'),
    url(r'^viewqueryandreplyMENTOR/', mentors_view.viewqueryandreplyMENTOR, name='viewqueryandreplyMENTOR'),
    url(r'^scheduleQuery/', groupadmin_view.scheduleQueryAction, name='scheduleQuery'),
    url(r'^viewallocatedqueryM/', mentors_view.viewallocatedqueryM, name='viewallocatedqueryM'),
    url(r'^replyMENTOR/(?P<mid>\d+)/$', mentors_view.replyMENTOR, name='replyMENTOR'),
    url(r'^replyactionMENTOR/', mentors_view.replyactionMENTOR, name='replyactionMENTOR'),
    url(r'^view_pendingqueryUSER/', users_view.view_pendingqueryUSER, name='view_pendingqueryUSER'),
    url(r'^movetohome/', users_view.movetohome, name='movetohome'),
    url(r'^movetohomeA/', siteadmin_view.movetohomeA, name='movetohomeA'),
    url(r'^user_logout/', users_view.user_logout, name='user_logout'),
    url(r'^MENTOR_logout/', mentors_view.MENTOR_logout, name='MENTOR_logout'),
    url(r'^groupadmin_logout/', groupadmin_view.groupadmin_logout, name='groupadmin_logout'),
    url(r'^backtohomeGA/', groupadmin_view.backtohomeGA, name='backtohomeGA'),
    url(r'^ADMIN_logout/', siteadmin_view.ADMIN_logout, name='ADMIN_logout'),
    url(r'^ViewMentorsQueryAndReply/', siteadmin_view.ViewMentorsQueryAndReply, name='ViewMentorsQueryAndReply'),
    url(r'^getMentors/', siteadmin_view.getMentors, name='getMentors'),
    url(r'^getQueriesAndReply/', siteadmin_view.getQueriesAndReply, name='getQueriesAndReply'),
    url(r'^blockmentorsSA/', siteadmin_view.blockmentorsSA, name='blockmentorsSA'),
    url(r'^viewblockedmentors/', siteadmin_view.viewblockedmentors, name='viewblockedmentors'),
    url(r'^unblockmentors/(?P<gid>\d+)/$', siteadmin_view.unblockmentors, name='unblockmentors'),
    url(r'^viewrepliedmentors_details/(?P<mid>\d+)/$', users_view.viewrepliedmentors_details, name='viewrepliedmentors_details'),
    url(r'^complaint/', users_view.complaint, name='complaint'),
    url(r'^complaintaction/', users_view.complaintaction, name='complaintaction'),
    url(r'^viewcomplaintsMentor/', mentors_view.viewcomplaintsMentor, name='viewcomplaintsMentor'),
    url(r'^viewusercomplaintsGA/', groupadmin_view.viewusercomplaintsGA, name='viewusercomplaintsGA'),
    url(r'^viewcomplaintsSA/$', siteadmin_view.viewcomplaintsSA, name='viewcomplaintsSA'),
    url(r'^viewmentordetailsfromcomplaintSA/(?P<mid>\d+)/$', siteadmin_view.viewmentordetailsfromcomplaintSA, name='viewmentordetailsfromcomplaintSA'),
    url(r'^viewuserdetailsfromcomplaintSA/(?P<uid>\d+)/$', siteadmin_view.viewuserdetailsfromcomplaintSA, name='viewuserdetailsfromcomplaintSA'),
    url(r'^viewmentordetailsfromcomplaintsGA/(?P<mid>\d+)/$', groupadmin_view.viewmentordetailsfromcomplaintsGA, name='viewmentordetailsfromcomplaintsGA'),
    url(r'^viewuserdetailsfromcomplaintsGA/(?P<uid>\d+)/$', groupadmin_view.viewuserdetailsfromcomplaintsGA, name='viewuserdetailsfromcomplaintsGA'),
    url(r'^deactivateMentorfromcomplaint/', groupadmin_view.deactivateMentorfromcomplaint, name='deactivateMentorfromcomplaint'),
    url(r'^forgot_password/', siteadmin_view.forgot_password, name='forgot_password'),
    url(r'^forgetpassword_verifyaction/', siteadmin_view.forgetpassword_verifyaction, name='forgetpassword_verifyaction'),
    url(r'^forgetpassword_updateAction/', siteadmin_view.forgetpassword_updateAction, name='forgetpassword_updateAction'),
    url(r'^addpattern/', siteadmin_view.addpattern, name='addpattern'),
    url(r'^addpatternaction/', siteadmin_view.addpatternaction, name='addpatternaction'),
    url(r'^viewpattern/', siteadmin_view.viewpattern, name='viewpattern'),
    url(r'^deletepattern/(?P<pid>\d+)/$', siteadmin_view.deletepattern, name='deletepattern'),
    url(r'^adminHome/$',siteadmin_view.adminHome,name='adminHome'),
    url(r'^mentorHome/$',mentors_view.mentorHome,name='mentorHome'),
    url(r'^gHome/$',groupadmin_view.gHome,name='gHome'),
    url(r'^uHome/$',users_view.uHome,name='uHome'),
    #url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
