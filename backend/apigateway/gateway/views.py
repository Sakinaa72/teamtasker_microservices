import jwt
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView



class GatewayView(APIView):
    def dispatch(self, request, *args, **kwargs):
        #Extract JWT from authentication header
        auth_header=request.headers.get('Authorization','')
        if not auth_header.startswith('Bearer '):
            return JsonResponse({'error':"Authorization header must start with Bearer"})
        
        token=auth_header.split(' ')[1]
        try:
            #validate jwt(replace 'your_secret_key', with the actual secret or public key)
            payload=jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            request.user_info=payload  #attach user info to request
        except jwt.InvalidTokenError:
            return JsonResponse({'error':'Invalid token'}, status=401)
        
        #Determine the target microservices based on the path
        path = request.path
        if path.startswith('/auth/'):
            target_url=f"{settings.MICROSERVICES['auth']}{path}"    
        elif path.startswith('/user/'):
            target_url=f"{settings.MICROSERVICES['user']}{path}"
        elif path.startswith('/task/'):
            target_url=f"{settings.MICROSERVICES['task']}{path}"
        elif path.startswith('/notification/'):
            target_url=f"{settings.MICROSERVICES['notification']}{path}"    
        else :
            return JsonResponse({'error':"Invalid endpoint"}, status=404)
        
        #forward request
        
        try:
            response = requests.request(
                method=request.method,
                url=target_url,
                headers={k: v for k, v in request.headers.items() if k != 'Host'},
                data=request.body,
                params=request.GET   
            )
            return JsonResponse(response.json(), status=response.status_code, safe=False)
        except request.RequestException as e:
            return JsonResponse({'error':str(e)}, status=500)