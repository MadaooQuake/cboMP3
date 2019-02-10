import unittest
import numpy
import struct
import os
from core.cbo_mp3 import CBOMp3


class CboMp3Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_get_mp3_files(self):
        self.assertEqual(CBOMp3().get_mp3_files("C:"), [])

    def test_2_get_mp3_files(self):
        self.assertEqual(CBOMp3().get_mp3_files("aaa"), [])

    def test_3_get_mp3_files(self):
        self.assertEqual(CBOMp3().get_mp3_files(""), [])

    def test_4_get_mp3_files(self):
        self.assertEqual(CBOMp3().get_mp3_files(), [])

    def test_5_get_mp3_files(self):
        createEnv().create_test_dir()

    def test_1_check_file_to_convert(self):
        self.assertEquals(1, 2)

    def test_1_convert_files(self):
        self.assertEquals(1, 2)

    def test_1_create_dst_location(self):
        self.assertEquals(1, 2)

    def test_1_create_tmp_dir(self):
        self.assertEquals(1, 2)


class createEnv:

    def create_test_dir(self):
        os.mkdir('test_tmp')
        os.chdir('test_tmp')

    def create_audio_file(self):
        sampling_rate = 44100
        frequency = 440
        sample = 44100/440
        interval = numpy.arange(sample)

if __name__ == '__main__':
    unittest.main()
