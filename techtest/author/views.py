import json
from marshmallow import ValidationError
from django.shortcuts import render
from django.views.generic import View
from techtest.utils import json_response
from author.models import Author


# Create your views here.
class AuthorView(View):
    def get(self, request, *args, **kwargs):
        return json_response(ArticleSchema().dump(Author.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        try:
            Author = AuthorSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(article), 201)
