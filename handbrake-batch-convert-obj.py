#!/usr/bin/env python
import os
import argparse
import re


class VideoFile:
    def __init__(self, file_info):
        self.__directory_path = file_info[0]
        self.__file_name, self.__file_extension = os.path.splitext(file_info[1])

    def getFile(self):
        return self.__file_name + self.__file_extension


def listdirFullPath(path_to_file):
    # output_path_to_dir = os.path.dirname(path_to_file)
    output_path_to_dir = path_to_file
    output_path_to_file = os.listdir(path_to_file)
    return (output_path_to_dir, output_path_to_file)

parser = argparse.ArgumentParser(description='HandBrake Conversion Tool!')
parser.add_argument('-s', '--source', help='path to source directory [default: current directory]', default=os.path.abspath(os.curdir))
parser.add_argument('-o', '--output', help='path to output directory', required=True)
# parser.add_argument('-R', '--recursion', help='recursively select all video files in file tree', default=False)
args = parser.parse_args()

video_extensions = ('.mkv', '.avi', '.mp4', '.m4v', '.flv', '.mov')

handbrake_path = '/usr/local/bin/HandBrakeCLI'
preset = 'AppleTV 3'
default_extension = '.m4v'

v = VideoFile(('/tmp/', 'test.mkv'))
print(v.getFile())