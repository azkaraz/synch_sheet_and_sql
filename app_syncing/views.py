import logging

from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseServerError

from app_syncing.synchronize_data import synchronize_data


@require_http_methods(['GET'])
def webhook_receiver_view(request):
    logging.warning('Webhook request processed successfully')
    if synchronize_data() is None:
        return HttpResponse('success')
    else:
        logging.error('Error processing webhook request')
        return HttpResponseServerError()


