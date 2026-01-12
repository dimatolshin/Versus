import urllib.parse
from django.http import JsonResponse
import os
import django
import json

from .models import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


file_path_upgrade = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DataJson', 'upgrade_car.json')


async def create_session(request):
    init_data = request.headers.get("Authorization")

    if not init_data:
        return JsonResponse({"detail": "Missing Telegram Init Data"}, status=400)

    try:
        init_data_dict = await transform_init_data(init_data)
    except ValueError as e:
        return JsonResponse({"detail": str(e)}, status=400)

    if len(init_data_dict.get("hash")) != 64:
        return JsonResponse({"detail": "Missing Telegram Init Data"}, status=400)

    # Сохраняем хэш и данные пользователя в сессии
    request.session["telegram_hash"] = init_data_dict.get("hash")
    request.session["telegram_user"] = init_data_dict.get("user", {})


async def transform_init_data(init_data: str) -> dict:
    try:
        decoded_data = urllib.parse.unquote(init_data)
        data = {k: v for k, v in (pair.split('=') for pair in decoded_data.split('&'))}
        data['user'] = json.loads(data['user'])
        return data
    except Exception as e:
        raise ValueError(f"Invalid Telegram Init Data format: {str(e)}")