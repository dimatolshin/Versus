from functools import wraps
from django.http import JsonResponse
from .models import User, UserBalance


def telegram_authenticated(view_func):
    @wraps(view_func)
    async def _wrapped_view(request, *args, **kwargs):
        telegram_hash = request.session.get("telegram_hash")
        telegram_user = request.session.get("telegram_user")

        if not telegram_hash or not telegram_user:
            return JsonResponse({"detail": "Unauthorized"}, status=401)

        if len(telegram_hash) != 64:
            return JsonResponse({"detail": "Unauthorized"}, status=401)

        # Добавляем данные Telegram в kwargs
        kwargs["telegram_user"] = telegram_user

        return await view_func(request, *args, **kwargs)

    return _wrapped_view


def check_user_exists(view_func):
    @wraps(view_func)
    async def _wrapped_view(request, *args, **kwargs):
        user = await User.objects.filter(tg_id=kwargs.get("telegram_user").get("id")).afirst()
        user_balance = await UserBalance.objects.filter(user=user).select_related('user', 'team',
                                                                                  'my_ofice__ofice').prefetch_related(
            'my_ofice__traders__trader__currency',
            'list_of_my_traders__trader__currency').afirst()
        if not user or user.is_baned == True:
            return JsonResponse({"Error": "User unexist"}, status=404)

        return await view_func(request, *args, **kwargs, user=user, user_balance=user_balance, )

    return _wrapped_view
