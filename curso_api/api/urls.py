from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
from .views import PersonaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)
router.register(r'personas', PersonaViewSet)

urlpatterns = router.urls
