#threading example

from rest_framework import decorators, permissions

import threading
from django.contrib.auth.models import User
from rest_framework.response import Response
from .mailer import send_email_by_threading

@decorators.api_view(["POST"])
@decorators.permissions_classes([permissions.IsAdminUser])
def SendMailView (request,user_id) : 
  try : 
    
    msg_content = request.data.get("message_content",None)
    
    # check the message is inserted by the client
    if msg_content is None :
      return Response({"message":"please insert the message"},status=400)
    
    
    try : 
      to_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
      return Respose({"message":"user with this id not found"},stauts=404)
      
    # send the email by threading 
    to_user_email = to_user.email
    thread = threading.Thread(target=send_email_by_threading,args=(to_user_email,msg_content,))
    thread.start()
    
    return Respose({"message":"email sent successfully"},status=200)

  except Exception as error : 
    return Response({
  "message" : f"an error accoured : {error}"
},status=500)