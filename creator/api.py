from django.http import JsonResponse

from cryptomus import Client

from .models import Creator, Support

from environ import Env
env = Env()
Env.read_env()

MERCHANT_UUID = env('MERCHANT_UUID')