#!/usr/bin/python3

import sys
import re

def write_line_to_file(line, filename):
    with open(filename, 'a') as x:
        x.write(line)

def main():
    info = {}
    file_to_split = sys.argv[1]
    current_insert = None
    print(f"[+] Start splitting file {file_to_split}")
    with open(file_to_split, 'r', errors="replace") as f:
        line = f.readline()
        while line:
            if 'INSERT INTO' in line:
                current_insert = re.search('.*`(.*)`.*', line).group(1)
                print(f"[+] New INSERT {current_insert}")
            if not current_insert:
                write_line_to_file(line, 'info.part')
                if info.get("info") is None:
                    info["info"] = 0
                info["info"] += 1
            else:
                write_line_to_file(line, f"{current_insert}.part")
                if info.get(current_insert) is None:
                    info[current_insert] = 0
                info[current_insert] +=1
            line = f.readline()
    print(info)

if __name__ == "__main__":
    main()
