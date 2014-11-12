#!/usr/bin/env python
import os
import argparse
import re

#os.path.join(path, '')

class VideoFile:
    video_info = {}

    def __init__(self, file_info, output_directory, target_extension='.m4v'):
        self.__directory_path = file_info[0]
        source_file_name, source_file_extension = os.path.splitext(file_info[1])

        self.video_info = {
            'source_directory': os.path.join(file_info[0], ''),
            'source_file': source_file_name,
            'source_file_extension': source_file_extension,
            'target_extension': target_extension,
            'output_directory': os.path.join(output_directory, ''),
            'scrubbed_input_file_name': re.escape(source_file_name) + source_file_extension,
            'scrubbed_output_file_name': re.escape(source_file_name) + target_extension,
            'scrubbed_output_directory_path': re.escape(output_directory),
            'scrubbed_input_directory': re.escape(file_info[0]),
        }
    # def getFile(self):
    #     return self.__file_name + self.__file_extension
    #
    # def getDir(self):
    #     return self.__directory_path

    # def getFullPath(self):
    #     # return (self.__directory_path + '/' + re.escape(self.__file_name) + self.__file_extension,
    #     #         self.__scrubbed_directory_path + '/' + re.escape(self.__scrubbed_file_name) + self.__target_extension)
    #     return (self.video_info['source_directory'] + '/' + self.video_info['source_file'] + self.video_info['source_file_extension'],
    #
    #     )


def buildSourceQueue(source_files, output_directory):
    files_queue = []
    for in_file in listdirFullPath(source_files):
        for source_vid in in_file:
            file_name, file_extension = os.path.splitext(source_vid)
            if video_extensions.__contains__(file_extension):
                v = VideoFile((source_files, source_vid), output_directory)
                files_queue.append(v)

    return files_queue


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

conversion_queue = buildSourceQueue(args.source, args.output)

for item in conversion_queue:
    print('Running...')
    print('### ' + item.video_info['source_directory'] + '###')
    run_command = handbrake_path + ' -v -Z \'' + preset + '\' -i ' + \
                  item.video_info['scrubbed_input_directory'] + item.video_info['scrubbed_input_file_name'] + \
                  ' -o ' + item.video_info['scrubbed_output_directory_path'] + item.video_info['scrubbed_output_file_name']
    print(run_command)
    # os.system(run_command)