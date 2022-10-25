# cboMP3

Tool convert mp3 Files to mp3 to any bitrate.

## Install pip

```bash
pip install cboMP3
```

## Install if not installing with pip and just wanting to run core/cbo_mp3.py directly as a MAIN after cloning this repo

```bash
pip install ffmpy
pip install mutagen
```

## Usage

```python
from cboMP3 import core.cbo_mp3 as CBOMp3
cbo = CBOMp3(bitrate=320)
mp3_files = cbo.get_mp3_files('J:\\myLargeMp3s\\') # Or Linux or mac paths should work too (untested)
mp3_files = cbo.check_file_to_convert(mp3_files) # This filters out files that are already below the correct target bitrate
cbo.convert_files(mp3_files) # Run The Job
```

Or you can use the command line tool if you download the git repo and install dependencies separately

```bash
  cd cboMP3/core
  python cbo_mp3.py myfile.mp3 128
```

Or just the file path if you like 128 kb/s

```bash
  cd cboMP3/core
  python cbo_mp3.py myfile.mp3
```

## Warning

This tool will overwrite your files. Make sure you have backups prior to using
