from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


def success(code=status.HTTP_200_OK, msg="", data=None, extra_info=None):
    json_result = {
        'code': code,
        'msg': msg,
        'data': data
    }
    if extra_info:
        json_result.update(extra_info)
    return JsonResponse(json_result)


def error(code=status.HTTP_400_BAD_REQUEST, msg="", data=None):
    return JsonResponse({
        'code': code,
        'msg': msg,
        'data': data
    })

def api_success(code=status.HTTP_200_OK, msg="", data=None):
    return JsonResponse({
        'code': code,
        'msg': msg,
        'data': data
    })

def api_error(code=status.HTTP_400_BAD_REQUEST, user_id=-1, user_locale='en', **kwargs):
    message = get_api_message(code, user_id, user_locale, **kwargs)
    return JsonResponse({
        'code': code,
        'msg': message["title"],
        'data': None
    })

def api_http_error(error_code="", user_id=-1, user_locale='en', **kwargs):
    message = get_api_message(error_code, user_id, user_locale, **kwargs)
    print(message)
    return Response(
        {
            'error': message["title"],
            'code': error_code,
        },
        status=int(message["status"]),
    )
