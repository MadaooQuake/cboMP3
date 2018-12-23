import glob
from pydub import AudioSegment

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

    def check_file_to_convert(self):
        """
        check bitrate of mp3 file and remove
        :return:
        """



if __name__ == "__main__":
    cbo = CBOMp3()
