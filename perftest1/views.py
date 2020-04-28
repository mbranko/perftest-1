from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from http import HTTPStatus
from perftest1.models import Test
from django.forms.models import model_to_dict
from django.views.decorators.cache import cache_page
from base64 import b64decode
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class HttpResponseUnauthorized(HttpResponse):
    status_code = HTTPStatus.UNAUTHORIZED


@cache_page(60*60)
def test_1(request, pk):
    """
    - ucita objekat iz baze
    - konvertuje u dict
    - posalje kao JSON
    """
    try:
        test_ = Test.objects.get(pk=pk)
        return JsonResponse(model_to_dict(test_))
    except Test.DoesNotExist:
        return HttpResponseNotFound()


@cache_page(60*60)
def test_2(request, pk):
    """
    - autentifikuje korisnika u bazi prema basic http auth
    - ucita objekat iz baze
    - konvertuje u dict
    - posalje kao JSON
    """
    try:
        basic_auth = request.META['HTTP_AUTHORIZATION'].strip()
        if basic_auth.startswith('Basic'):
            part_2 = basic_auth.split(' ')[1]
            us_pw = b64decode(part_2).decode('ascii')
            username, password = us_pw.split(':')
            user = authenticate(username=username, password=password)
            if not user:
                return HttpResponseUnauthorized()        
            test_ = Test.objects.get(pk=pk)
            return JsonResponse(model_to_dict(test_))
        else:
            return HttpResponseUnauthorized()
    except Test.DoesNotExist:
        return HttpResponseNotFound()
    except User.DoesNotExist:
        return HttpResponseUnauthorized()
    except KeyError:
        return HttpResponseUnauthorized()
