from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .src.validate_finite_set import Validate_Finite_Set
from .src.validate_numeric_value import Validate_Numeric_Value
"""
Both the POST API's given in the problem statements are implemented below
The required parameters are extracted from the input json accordingly and
the respective methods are called for processing.
"""

@api_view(['POST'])
def finite_set(request):
    """
    1. POST API to validate Finite Value Set
    """
    data             = json.loads(request.body.decode("utf-8"))
    values           = data.get("values")
    supported_values = data.get("supported_values")
    invalid_trigger  = data.get("invalid_trigger")
    key              = data.get("key")
    support_multiple = data.get("support_multiple")
    pick_first       = data.get("pick_first")
    validator        = Validate_Finite_Set()
    filled, partially_filled, trigger, parameters = validator.validate_finite_values_entity(values, supported_values, invalid_trigger, key, support_multiple, pick_first)
    resp	     = {
                           "filled" : filled,
                           "partially_filled" : partially_filled,
                           "trigger" : trigger,
                           "parameters" : parameters
                       }


    return Response(resp, status=status.HTTP_200_OK)

@api_view(['POST'])
def numeric_value(request):
    """
    2. POST API to validate Numerical Value
    """
    data             = json.loads(request.body.decode("utf-8"))
    values           = data.get("values")
    invalid_trigger  = data.get("invalid_trigger")
    key              = data.get("key")
    support_multiple = data.get("support_multiple")
    pick_first       = data.get("pick_first")
    constraint       = data.get("constraint")
    var_name         = data.get("var_name")
    validator        = Validate_Numeric_Value()
    filled, partially_filled, trigger, parameters = validator.validate_numeric_entity(values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name)
    resp	     = {
                           "filled" : filled,
                           "partially_filled" : partially_filled,
                           "trigger" : trigger,
                           "parameters" : parameters
                       }

    return Response(resp, status=status.HTTP_200_OK)
