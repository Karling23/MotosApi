from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from motostore.views.health import health_check
from motostore.views.usuario import UsuarioViewSet
from motostore.views.catalogos import MarcaViewSet, CategoriaViewSet
from motostore.views.productos import MotocicletaViewSet, CascoViewSet, AccesorioViewSet
from motostore.views.operaciones import PedidoViewSet, PagoViewSet, TestingViewSet
from motostore.views.auth import RegisterView, LogoutView, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'marcas', MarcaViewSet, basename='marca')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'motocicletas', MotocicletaViewSet, basename='motocicleta')
router.register(r'cascos', CascoViewSet, basename='casco')
router.register(r'accesorios', AccesorioViewSet, basename='accesorio')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'pagos', PagoViewSet, basename='pago')
router.register(r'testings', TestingViewSet, basename='testing')

urlpatterns = [
    path('health/', health_check),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('', include(router.urls)),
]