import requests
import json
import logging
from django.http import HttpResponse
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

logger = logging.getLogger(__name__)

class ChallengeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/todos/', stream=True)

            raw = response.json()
            data = list(map(lambda x: {'id': x['id'], 'title': x['title']}, raw[:5]))
            status_code = response.status_code
            dt_now = datetime.now().strftime('%H:%M:%S %d/%m/%Y')

            logger.info('Timestamp: {}'.format(dt_now))
            logger.info('Status code: {}'.format(status_code))
            logger.info(raw)
            return HttpResponse(json.dumps(data), content_type="application/json")
        except Exception as e:
            return HttpResponse(json.dumps({'error': {'reason': str(e)}}), status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")
