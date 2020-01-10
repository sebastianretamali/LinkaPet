from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

#import tabla mascota
from mascota.views import list_mascota, create_mascota, delete_mascota, update_mascota, aleatorio, descripcion_mascota, match_mascota, successView
#import tabla Cuestiorario
from cuestionario.views import list_cuestionario, create_cuestionario
#import tabla auth_user
from accounts.views import edit_profile

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static


urlpatterns = [
    #Login, logout, sigup.
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    
    #Editar perfil
    url(r'^accounts/edit/$', accounts_views.edit_profile, name='edit_profile'),
    url(r'^edit/accept/$', TemplateView.as_view(template_name='accept_profile.html'), name='accept_profile'),

    #Recuperar contraseña
    url(r'^reset/$',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
    ),
         name='password_reset'),
    url(r'^reset/done/$',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    url(r'^reset/complete/$',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

    #url mascotas
    path('list/', list_mascota, name='list_mascota'),
    path('crea/', create_mascota, name='create_mascota'),
    path('update/<int:id>/', update_mascota, name='update_mascota'),
    path('delete/<int:id>/', delete_mascota, name='delete_mascota'),

    path('descripcion/<int:id>/', descripcion_mascota, name='descripcion_mascota'),
    
    path('match/<int:id>/', match_mascota, name='match_mascota'),
    path('success/', successView, name='success'),

    #Cuestionario
    path('list/cuestionario/', list_cuestionario, name='list_cuestionario'),
    path('crea/cuestionario/', create_cuestionario, name='create_cuestionario'),
    path('aleatorio/<int:id>/', aleatorio, name='aleatorio'),

    #Inicio de seción fundaciones
    url(r'^register/$', accounts_views.register, name='register'),

]

if settings.DEBUG: 
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
         
         