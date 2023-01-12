import magic

ALLOWED_MIME_TYPES = [
    "audio/mpeg",
    "audio/ogg",
    "audio/vnd.wav",
    "audio/wav",
    "audio/x-wav",
    "application/x-msdos-program",
]

ALLOWED_FILE_EXTENTIONS = ["mp3", "ogg", "wav"]


def is_allowed_audio(file):
    # When the file is empty it returns is_allowed and a None file_type
    if not file:
        return True, None
    # First it checks if it can find the mime type of the uploaded file
    is_allowed, content_type = check_mime_type(file)

    # If the mime type is not allowed it returns False and the mime/content type
    if not is_allowed:
        return is_allowed, content_type

    # To make validation more complete, the file extension is also checked.
    is_allowed, content_type = check_file_extension(file)

    return is_allowed, content_type


def check_mime_type(file):
    import pdb

    pdb.set_trace()
    mime = file.content_type

    is_allowed = mime in ALLOWED_MIME_TYPES

    if is_allowed:
        file.seek(0)
        mime = magic.from_buffer(file.read(), mime=True)
        is_allowed = mime in ALLOWED_MIME_TYPES

    return is_allowed, mime


def check_file_extension(file):
    file_extension = file.name.split(".")[-1]

    is_allowed = file_extension.lower() in ALLOWED_FILE_EXTENTIONS
    return is_allowed, file_extension.lower()
