from django.core.exceptions import ValidationError


def validate_music_length(value):
    if value not in range(1, 3601):
        raise ValidationError(
            f"A duração da música deve ser um número"
            f" inteiro entre 1 e 3600 segundos. O valor"
            f"{value} não é válido.")


def validate_singers_name(value):
    if not value.isnumeric():
        raise ValidationError(
            f"{value} must be a number"
        )