from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    msg = fields.Raw()


class ResetPostsResponseSchema(Schema):
    msg = fields.String()
