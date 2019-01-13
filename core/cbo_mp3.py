import glob
import ffmpy
import os
from mutagen.mp3 import MP3

class CBOMp3:

    def get_mp3_files(self, dir_path):
        """
        Scan selected directory for search all mp3 files
        dir_path: path for selected directory
        :return: list of mp3 files
        """
        mp3_files = None
        try:
            mp3_files = glob.glob("{}*.mp3".format(dir_path))
        except:
            print("No mp3 files found!")
        return mp3_files

    def check_file_to_convert(self, mp3_files):
        """
        check bitrate of mp3 file and remove
        :return:
        """
        print(mp3_files)
        for mp3_file in mp3_files:
            audio = MP3(mp3_file)
            if audio.info.bitrate > 128000:
                print('File to convert: {}'.format(mp3_file))
            else:
                mp3_files.remove(mp3_file)
        return mp3_files

    def convert_files(self, mp3_files):
        """

        :param mp3_files:
        :return:
        """
        for mp3_file in mp3_files:
            dst_mp3 = self.create_dst_location(mp3_file)
            print(dst_mp3)
            ff = ffmpy.FFmpeg(
                inputs={mp3_file: None},
                outputs={dst_mp3: '-acodec libmp3lame -ab 128k'}
            )
            print(ff.cmd)
            ff.run()

    def create_dst_location(self, mp3_file):
        """

        :param mp3_file:
        :return:
        """
        mp3_file = mp3_file.split("\\")
        song = mp3_file[len(mp3_file)-1]
        # hardcodet tmp location
        mp3_file[len(mp3_file)-1] = "tmp"
        # join
        dst_file = '\\'.join([str(x) for x in mp3_file])
        self.create_tmp_dir(dst_file)
        return dst_file + "\\{}".format(song)

    def create_tmp_dir(self, dir_name):
        """

        :param dir_name:
        :return:
        """
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

