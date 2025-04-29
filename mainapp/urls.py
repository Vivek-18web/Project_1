from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, URLPattern
from. import views
urlpatterns = [
    path('',views.main),
    path('login',views.login),
    path('home',views.home),
    path('register',views.register),
    path('registercheck',views.registercheck),
    path('logincheck',views.logincheck),
    path('out',views.out),
    path('profile',views.profile),
    path('update',views.update),
    path('apply',views.apply),
    path('success',views.success),

    path('hrlogin',views.hrlogin),
    path('hrregister',views.hrregister),
    path('hrregistercheck',views.hrregistercheck),
    path('hrlogincheck',views.hrlogincheck),
    path('hrprofile',views.hrprofile),
    path('hrupdate',views.hrupdate),

    path('hrdash',views.hrdash),
    path('job',views.job),
    path('addjob',views.addjob),
    path('list',views.list),
    path('applylist',views.applylist),
    path('hrlogout',views.hrlogout),
    path('delete',views.delete),
    path('user_applied',views.user_applied),
    path('reject',views.reject),
    path('reject_process',views.reject_process),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
