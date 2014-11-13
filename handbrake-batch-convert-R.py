#!/usr/bin/env python
import os
import argparse
import re


class VideoFile:

    def __init__(self, file_info, output_directory, target_extension='.m4v'):
        self.video_info = {}
        self.__directory_path = file_info[0]
        source_file_name, source_file_extension = os.path.splitext(file_info[1])

        self.video_info['source_directory'] = os.path.join(file_info[0], '')
        self.video_info['source_file'] = source_file_name
        self.video_info['source_file_extension'] = source_file_extension
        self.video_info['target_extension'] = target_extension
        self.video_info['output_directory'] = os.path.join(output_directory, '')

        self.video_info['scrubbed_input_directory'] = re.escape(self.video_info['source_directory'])
        self.video_info['scrubbed_input_file_name'] = re.escape(self.video_info['source_file']) + self.video_info['source_file_extension']
        self.video_info['scrubbed_output_file_name'] = re.escape(self.video_info['source_file']) + self.video_info['target_extension']
        self.video_info['scrubbed_output_directory_path'] = re.escape(self.video_info['output_directory'])


def buildSourceQueueR(source_files, output_directory):
    files_queue = []
    for in_file in listdirFullPath(source_files):
        for source_vid in in_file:
            file_name, file_extension = os.path.splitext(source_vid)
            if video_extensions.__contains__(file_extension):
                # v = VideoFile((source_files, source_vid), output_directory)
                v = VideoFile((source_files, file_name), output_directory)
                files_queue.append(v)

    return files_queue


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
    output_path_to_dir = path_to_file
    output_path_to_file = os.listdir(path_to_file)
    return (output_path_to_dir, output_path_to_file)


def doConversion(queue):
    for item in queue:
        print('Running...')
        run_command = handbrake_path + ' -v -Z \'' + preset + '\' -i ' + \
                      item.video_info['scrubbed_input_directory'] + item.video_info['scrubbed_input_file_name'] + \
                      ' -o ' + item.video_info['scrubbed_output_directory_path'] + item.video_info['scrubbed_output_file_name']
        print(run_command)
        if args.test != True:
            os.system(run_command)


parser = argparse.ArgumentParser(description='HandBrake Conversion Tool!')
parser.add_argument('-s', '--source', help='path to source directory [default: current directory]', default=os.path.abspath(os.curdir))
parser.add_argument('-o', '--output', help='path to output directory', required=True)
parser.add_argument('-t', '--test', help='Run through without actually converting', action='store_true', default=False)
parser.add_argument('-R', '--recursion', help='recursively select all video files in file tree', action='store_true', default=False)
args = parser.parse_args()

video_extensions = ('.mkv', '.avi', '.mp4', '.m4v', '.flv', '.mov')

handbrake_path = '/usr/local/bin/HandBrakeCLI'
preset = 'AppleTV 3'
default_extension = '.m4v'

conversion_queue = buildSourceQueueR(args.source, args.output)

for item in conversion_queue:
    print(item.video_info['source_directory'] + item.video_info['source_file'] + item.video_info['source_file_extension'])

# doConversion(conversion_queue)
