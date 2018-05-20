from django.conf.urls import url
from webapp.views import PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patients', PatientViewSet, base_name='patient')
urlpatterns = router.urls

