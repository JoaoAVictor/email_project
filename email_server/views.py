from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
import os


class SendEmailView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, format=None):
        recipient_email = request.data.get('recipient_email')
        subject = request.data.get('subject')
        message = request.data.get('message')
        attachments = request.FILES.getlist('attachments')

        if not recipient_email or not subject or not message:
            return Response({'message': 'Recipient email, subject, and message are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email='jvictor@magnasistemas.com',  # Update with your email
                to=[recipient_email],
            )

            for attachment in attachments:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            email.send()

            return Response({'message': 'Email enviado com sucesso.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
