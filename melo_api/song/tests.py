from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from song.validators import is_allowed_audio


class IsAllowedAttachmentTests(APITestCase):
    """
    Test if the mime types of the possibly uploaded attachment are allowed.
    """

    def test_file_is_allowed(self):
        mock_wav = b"RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00"
        # Dont upload files that have a other extension type than content type
        wav_file = SimpleUploadedFile(
            "file_name.exe.wav", mock_wav, content_type="audio/x-wav"
        )
        wav_file, file_type = is_allowed_audio(wav_file)
        self.assertFalse(wav_file)
        self.assertEqual(file_type, "wav")

        exe_file_2 = SimpleUploadedFile(
            "file_name.exe.mp3",
            b"file_content",
            content_type="application/x-msdos-program",
        )
        exe_file_2, file_type = is_allowed_audio(exe_file_2)
        self.assertFalse(exe_file_2)
        self.assertEqual(file_type, "application/x-msdos-program")

        # Mime type is allowed but extension is not allowed resulting in a not allowed file.
        ps2_file = SimpleUploadedFile(
            "file_name.ps2", b"file_content", content_type="text/plain"
        )
        ps2_file, file_type = is_allowed_audio(ps2_file)
        self.assertFalse(ps2_file)
        # self.assertEqual(file_type, "ps2")

        # Allowed file
        wav_file = SimpleUploadedFile(
            "file_name.wav", mock_wav, content_type="audio/x-wav"
        )
        wav_file, file_type = is_allowed_audio(wav_file)
        self.assertTrue(wav_file)
        self.assertEqual(file_type, "wav")
