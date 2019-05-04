import glob
import ffmpy
import os
from mutagen.mp3 import MP3


class CBOMp3:

    @staticmethod
    def get_mp3_files(dir_path=""):
        """
        Scan selected directory for search all mp3 files
        dir_path: path for selected directory
        :return: list of mp3 files
        """
        return glob.glob("{}*.mp3".format(dir_path))

    @staticmethod
    def check_file_to_convert(mp3_files):
        """
        check bitrate of mp3 file and remove
        :return:
        """
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
            ff = ffmpy.FFmpeg(
                inputs={mp3_file: None},
                outputs={dst_mp3: '-acodec libmp3lame -b 256k'}
            )
            try:
                ff.run()
            except ffmpy.FFRuntimeError:
                print('File {} already exists.'.format(dst_mp3))

    def create_dst_location(self, mp3_file):
        """

        :param mp3_file:
        :return:
        """
        mp3_file = mp3_file.split("\\")
        song = mp3_file[len(mp3_file) - 1]
        mp3_file[len(mp3_file) - 1] = "tmp"
        # join
        dst_file = '\\'.join([str(x) for x in mp3_file])
        self.create_tmp_dir(dst_file)
        return dst_file + "\\{}".format(song)

    @staticmethod
    def create_tmp_dir(dir_name):
        """

        :param dir_name:
        :return:
        """
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


if __name__ == "__main__":
    cbo = CBOMp3()
    mp3_files = cbo.get_mp3_files('F:\\Robocik\\')
    mp3_files = cbo.check_file_to_convert(mp3_files)
    cbo.convert_files(mp3_files)
