# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .src.validate_finite_set import Validate_Finite_Set
from .src.validate_numeric_value import Validate_Numeric_Value
@api_view(['POST'])
def finite_set(request):
    data             = json.loads(request.body.decode("utf-8"))
    values           = data.get("values")
    supported_values = data.get("supported_values")
    invalid_trigger  = data.get("invalid_trigger")
    key              = data.get("key")
    support_multiple = data.get("support_multiple")
    pick_first       = data.get("pick_first")
    validator        = Validate_Finite_Set()
    resp             = validator.validate_finite_values_entity(values, supported_values, invalid_trigger, key, support_multiple, pick_first)

    return Response(resp, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def numeric_value(request):
    data             = json.loads(request.body.decode("utf-8"))
    values           = data.get("values")
    invalid_trigger  = data.get("invalid_trigger")
    key              = data.get("key")
    support_multiple = data.get("support_multiple")
    pick_first       = data.get("pick_first")
    constraint       = data.get("constraint")
    var_name         = data.get("var_name")
    validator        = Validate_Numeric_Value()
    resp             = validator.validate_numeric_entity(values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name)

    return Response(resp, status=status.HTTP_201_CREATED)
