import io
import os
import re
import shutil
import sys

# declare which header to look for as the table of contents
TOC_HEADER = 'Quicklinks'

def convert_header_to_anchor(header: str) -> str:

    remove_chars = [c for c in '<>?,./:";\'[]{}\\|!@#$%^&*()+=']

    # list of characters to replace during conversion

    for char in remove_chars:
        header = header.replace(char, '')
    header = header.replace(' ', '-')
    
    return '#{}'.format(header.lower())

def generate_toc_header(raw_string: str) -> str:
    '''Converts a raw string into a markdown compliant list item with anchor tag'''

    return '- [{}]({})'.format(raw_string, convert_header_to_anchor(raw_string))

def update_toc_headers(file_path: str, toc_header: str) -> None:
    '''
    Updates a markdown file at the given path, adding all sub-headers into
    a list under the `toc_header` subheading
    '''

    pattern = '^## (.*)$'

    toc_index = -1
    subheader_list = []

    toc_found = False
    anchor_count = 0 

    with open(file_path, 'r+') as f:
        data = f.readlines()

        for line_num in range(len(data)):
            line = data[line_num].strip()
            match = re.search(pattern, line)

            if match: 
                toc_found = False

                if match.group(1) != toc_header:
                    subheader_list.append(generate_toc_header(match.group(1)) + '\n')
                else:
                    toc_index = line_num
                    toc_found = True

            elif toc_found:
                anchor_count += 1

        data[toc_index+1:toc_index+anchor_count] = subheader_list

        f.seek(0)
        f.writelines(data)

if __name__ == '__main__':
    file_name = os.path.basename(sys.argv[1])
    parent_dir = os.path.dirname(sys.argv[1])

    shutil.copyfile(sys.argv[1], os.path.join(parent_dir, file_name + ".bak"))
    update_toc_headers(sys.argv[1], TOC_HEADER)
    