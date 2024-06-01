from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import index, tc_view, matier_detailtc , gem_view, matier_detailgem ,  ppv_view, matier_detailppv
from core.views import sta_view ,matier_detailsta, psa_view, matier_detailpsa , gab_view, matier_detailgab


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tc/', tc_view, name='tc_view'),
    path('tc/<int:matier_id>/', matier_detailtc, name='matier_detailtc'),
    path('gem/', gem_view, name='gem_view'),
    path('gem/<int:matier_id>/', matier_detailgem, name='matier_detailgem'),
    path('gab/', gab_view, name='gab_view'),
    path('gab/<int:matier_id>/', matier_detailgab, name='matier_detailgab'),
    path('ppv/', ppv_view, name='ppv_view'),
    path('ppv/<int:matier_id>/', matier_detailppv, name='matier_detailppv'),
    path('sta/', sta_view, name='sta_view'),
    path('sta/<int:matier_id>/', matier_detailsta, name='matier_detailsta'),
    path('psa/', psa_view, name='psa_view'),
    path('psa/<int:matier_id>/', matier_detailpsa, name='matier_detailpsa'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




  