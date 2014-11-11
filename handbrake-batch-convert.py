#!/usr/bin/env python
import os
import argparse
import re


def buildSourceQueue(source_files):
    files_queue = []
    for in_file in listdirFullPath(source_files):
        for source_vid in in_file:
            file_name, file_extension = os.path.splitext(source_vid)
            if video_extensions.__contains__(file_extension):
                # print('DEBUG: ' + source_files + '/' + source_vid)
                files_queue.append((source_files, source_vid))

    # print('')
    return files_queue


def listdirFullPath(path_to_file):
    # output_path_to_dir = os.path.dirname(path_to_file)
    output_path_to_dir = path_to_file
    output_path_to_file = os.listdir(path_to_file)
    return (output_path_to_dir, output_path_to_file)


def createConversionQueue(videos_list):
    scrubbed_names = []
    for dir, name in videos_list:
        file_name, file_extension = os.path.splitext(name)
        scrubbed_names.append((dir + '/' + re.escape(name), re.escape(file_name) + default_extension))

    return scrubbed_names


parser = argparse.ArgumentParser(description='HandBrake Conversion Tool!')
parser.add_argument('-s', '--source', help='path to source directory [default: current directory]', default=os.path.abspath(os.curdir))
parser.add_argument('-o', '--output', help='path to output directory', required=True)
# parser.add_argument('-R', '--recursion', help='recursively select all video files in file tree', default=False)
args = parser.parse_args()

video_extensions = ('.mkv', '.avi', '.mp4', '.m4v', '.flv', '.mov')

handbrake_path = '/usr/local/bin/HandBrakeCLI'
preset = 'AppleTV 3'
default_extension = '.m4v'


convert_queue = buildSourceQueue(args.source)
output_queue = createConversionQueue(convert_queue)

# print('Converting following files to ' + args.output)
# print('----')
#
# for f in convert_queue:
#     print('DEBUG: ' + str(f))
# print('----')
#
# print('Scrubbed names are:')
#
# for f in output_queue:
#     print('DEBUG: ' + str(f))
# print('----')


for source_file, output_file in output_queue:
    print('Running...')
    run_command = handbrake_path + ' -v -Z \'' + preset + '\' -i ' + source_file + ' -o ' + args.output + '/' + output_file
    print(run_command)
    os.system(run_command)
