from rest_marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load

class AuthorSchema(Schema):
    class Meta(object):
        model = Author
    
    first_name = fields.String(validate=validate.Length(max=255))
    last_name = fields.String(validate=validate.Length(max=255))
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)