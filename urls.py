from django.conf.urls.defaults import *
from hdb.databank.models import Patient
from django.contrib.auth import views as auth_views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {
     'queryset': Patient.objects.all(),#change to admin
}
patient_info = {'model' : Patient}

urlpatterns = patterns('',
     (r'^login/$', auth_views.login,
          dict(template_name='login/login_user.html')),
     (r'^search/$', 'django.views.generic.list_detail.object_list',
          dict(info_dict, paginate_by=25, template_name='patients/patient_search_results.html', )),
     (r'^patients/$', 'django.views.generic.list_detail.object_list',
          dict(info_dict, paginate_by=25, template_name='patients/patient_list.html')),
     (r'^patients/create/$', 'django.views.generic.create_update.create_object', dict(patient_info,
          template_name='patients/patient_form.html', post_save_redirect='/patients/')),
     (r'^patients/update/(?P<object_id>\d+)/$', 'django.views.generic.create_update.update_object',
          dict(patient_info, template_name='patients/patient_form.html', post_save_redirect='/patients/')),
     (r'^patients/delete/(?P<object_id>\d+)/$', 'django.views.generic.create_update.delete_object',
     dict(patient_info, template_name='patients/patient_confirm_delete.html',
          post_delete_redirect='/patients/')),

     (r'^admin/', include(admin.site.urls)),

     #(r'^site_media/(?P.*)$', 'django.views.static.serve',
     #     {'document_root': '/home/brianna/hdb/databank/static'}),
)
