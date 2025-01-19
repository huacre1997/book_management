from typing import Type

from mongoengine import Document
from rest_framework.exceptions import ValidationError


def validate_unique_field(
    value: str, model: Type[Document], filter_params: dict[str, str | bool]
) -> str:
    """
    Verifica si ya existe un registro con el mismo valor y parámetros de filtrado.
    Lanza un ValidationError si el registro existe.

    Args:
        value (str): El valor a validar (por ejemplo, el nombre).
        model (Type[Document]): El modelo en el que se valida.
        filter_params (dict): Los parámetros de filtrado para la consulta.

    Returns:
        str: El valor si no hay duplicados.

    Raises:
        ValidationError: Si ya existe un registro con los mismos parámetros.
    """
    existing_instance = model.objects(**filter_params).first()  # type: ignore

    if existing_instance:
        raise ValidationError(
            f"A {model.__name__} with the value '{value}' already exists."
        )

    return value
