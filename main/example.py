from drf_yasg import openapi
from rest_framework.serializers import Serializer


def get_response_examples(
    example: dict = {},
    description: str = '',
    schema: Serializer | Serializer | None = None,
):
    if schema is None:
        return openapi.Response(
            description=description,
            examples={"application/json": example},
        )

    return openapi.Response(
        description=description,
        schema=schema
    )