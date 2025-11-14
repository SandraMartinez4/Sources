from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import json

#IMPORTAMOSS NUESTRO METODO
from.utils import run_code

@api_view(['POST'])
def main(request):
#definimos el metodo de la peticion
    if request.method!='POST':
        return JsonResponse(
            {'code':''},
            status=405
        )



    try:
        #PARSEAMOS EL CUERPO DE LA PETICION EN UN JSON
        body=request.body.decode('utf-8')if request.body else''
        data = json.loads(body)if body else {}
    except Exception:
        return JsonResponse({'code':'Json'},
                            status=405
                            )
#del Json obtenemos qel que tenga 'text'
    code=data.get('text','')
    #EJECUTAMOSS LAS INTRUCCIONES CON EL METODO QUE DEFINIMOS
    output=run_code(code)
    #DA UNA RESPUESTA DE TIPO JSON
    return Response(
        {"output":output},
        status=status.HTTP_200_OK
    )

    
