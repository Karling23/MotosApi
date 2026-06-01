from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def saludo(request):
    """
    Endpoint más simple posible.
    GET /api/saludo/ → devuelve un JSON fijo.
    """
    datos = {
        "mensaje":  "¡Hola desde Django REST Framework!",
        "version":  "1.0",
        "estado":   "ok",
    }
    return Response(datos)
