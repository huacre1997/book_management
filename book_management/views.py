from django.http import JsonResponse
from loguru import logger

def main_view(_):
    logger.info("Book management on!")
    return JsonResponse(
        {
            'project': 'Book Management System',
            'message': 'server on',
        }
    )
