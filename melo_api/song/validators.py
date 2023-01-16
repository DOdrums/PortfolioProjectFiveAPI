from django.core.exceptions import ValidationError
import magic

ALLOWED_MIME_TYPES = [
    "audio/mpeg",
    "audio/m4a",
]

ALLOWED_FILE_EXTENTIONS = ["mp3", "m4a"]


def validate_audio(audio):
    file = audio
    # When the file is empty it returns is_allowed and a None file_type
    if not file:
        raise ValidationError("File is empty")

    # To make validation more complete, the file extension is also checked.
    is_allowed, content_type = check_file_extension(file)
    if not is_allowed:
        raise ValidationError(
            f".{content_type} files are not supported, please upload an audio file of type: .mp3 or .m4a."
        )

    # First it checks if it can find the mime type of the uploaded file
    is_allowed, content_type = check_mime_type(file)

    # If the mime type is not allowed it returns False and the mime/content type
    if not is_allowed:
        raise ValidationError(
            f"Filetype {content_type} is not supported, please upload an audio file of type: .mp3 or .m4a"
        )

    return is_allowed, content_type


def check_mime_type(file):
    mime = file.content_type

    is_allowed = mime in ALLOWED_MIME_TYPES

    if is_allowed:
        file.seek(0)
        mime = magic.from_buffer(file.read(1024), mime=True)
        is_allowed = mime in ALLOWED_MIME_TYPES

    return is_allowed, mime


def check_file_extension(file):
    file_extension = file.name.split(".")[-1]

    is_allowed = file_extension.lower() in ALLOWED_FILE_EXTENTIONS
    return is_allowed, file_extension.lower()
