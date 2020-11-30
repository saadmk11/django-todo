from todos.views import TodoViewSet
from rest_framework.routers import DefaultRouter


app_name = 'todos'


router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
urlpatterns = router.urls
