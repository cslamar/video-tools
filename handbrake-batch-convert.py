#!/usr/bin/env python
import sys
import os
import argparse
from re import escape


def buildSourceQueue(source_files):
    files_queue = []
    for in_file in testList(source_files):
        for source_vid in in_file:
            file_name, file_extension = os.path.splitext(source_vid)
            if video_extensions.__contains__(file_extension):
                print(source_vid)
                files_queue.append(in_file)

    return files_queue



def testList(path_to_file):

    return (os.path.dirname(path_to_file), os.listdir(path_to_file))


def listdirFullPath(path_to_file):
    # return [os.path.join(path_to_file, f) for f in os.listdir(path_to_file)]
    return (os.path.dirname(path_to_file), os.listdir(path_to_file))


def scrubNames(videos_list):
    scrubbed_names = []
    for name in videos_list:
        scrubbed_names.append(escape(name))

    return scrubbed_names


parser = argparse.ArgumentParser(description='HandBrake Conversion Tool!')
parser.add_argument('-s', '--source', help='path to source directory [default: current directory]', default=os.path.abspath(os.curdir))
parser.add_argument('-o', '--output', help='path to output directory', required=True)
parser.add_argument('-R', '--recursion', help='recursively select all video files in file tree', default=False)
args = parser.parse_args()

video_extensions = ('.mkv', '.avi', '.mp4', '.m4v', '.flv', '.mov')

handbrake_path = '/usr/local/bin/HandBrakeCLI'
preset = 'AppleTV 3'
default_extension = '.m4v'

# print args.source
# print args.output


print('#####')
buildSourceQueue(args.source)
print('#####')


# convert_queue = buildSourceQueue(args.source)
#
# print('Converting following files to ' + args.output)
#
# for f in convert_queue:
#     print(f)
#
# print('----')
# output_queue = scrubNames(convert_queue)
#
# print('Scrubbed names are:')
#
# for f in output_queue:
#     print(f)
#
# print('----')

# for source_video in convert_queue:
#     print(handbrake_path + ' -v -Z \'' + preset + '\' -i ' + source_video + ' -o ' + args.output)
