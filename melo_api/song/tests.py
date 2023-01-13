from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from song.validators import validate_audio
from django.core.exceptions import ValidationError


class IsAllowedAttachmentTests(APITestCase):
    """
    Test if the mime types of the possibly uploaded attachment are allowed.
    """

    def test_file_is_allowed(self):
        mock_mp3 = b"\xff\xfb\xff\xf3\xff\xf2"
        # Dont upload files that have a other extension type than content type
        wav_file = SimpleUploadedFile(
            "file_name.wav.mp3", mock_mp3, content_type="audio/x-wav"
        )
        self.assertRaises(ValidationError, validate_audio, wav_file)
        # self.assertFalse(wav_file)
        # self.assertEqual(file_type, "wav")

        # exe_file_2 = SimpleUploadedFile(
        #     "file_name.exe.mp3",
        #     b"file_content",
        #     content_type="application/x-msdos-program",
        # )
        # exe_file_2, file_type = is_allowed_audio(exe_file_2)
        # self.assertFalse(exe_file_2)
        # self.assertEqual(file_type, "application/x-msdos-program")

        # # Mime type is allowed but extension is not allowed resulting in a not allowed file.
        # ps2_file = SimpleUploadedFile(
        #     "file_name.ps2", b"file_content", content_type="text/plain"
        # )
        # ps2_file, file_type = is_allowed_audio(ps2_file)
        # self.assertFalse(ps2_file)
        # # self.assertEqual(file_type, "ps2")

        # Allowed file
        mp3_file = SimpleUploadedFile(
            "file_name.mp3", mock_mp3, content_type="audio/mpeg"
        )
        mp3_file, file_type = validate_audio(mp3_file)
        self.assertTrue(mp3_file)
        self.assertEqual(file_type, "mp3")
