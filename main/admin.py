from django.contrib import admin

from .models import *


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(Ofice)
class OficeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserOfice)
class UserOficeAdmin(admin.ModelAdmin):
    pass


@admin.register(Traders)
class TradersAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTraders)
class UserTradersAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(UserTask)
# class UserTaskAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(SocialTask)
# class SocialTaskAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(UserSocialTask)
# class UserSocialTaskAdmin(admin.ModelAdmin):
#     pass

@admin.register(ClaimUserHistory)
class ClaimUserHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
