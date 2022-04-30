from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import views

from . import negotiators, parsers

# Create your views here.
class CatalogView(views.APIView):

    parser_classes = (parsers.JSONSchemaParser,)
    content_negotiation_class = negotiators.IgnoreClientContentNegotiation

    def post(self, request, *args, **kwargs):
        print(request.DATA)
        try:
            # implicitly calls parser_classes
            request.DATA
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.message),
                status=status.HTTP_400_BAD_REQUEST
            )
        utils.store_the_json(request.DATA)
        return Response()
