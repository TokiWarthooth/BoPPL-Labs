# scanning file system, consecutively and parallel

import threading
import os
from utils import measure_time


def find_txt_files(directory):
    """Recursively find all .txt files in the given directory."""
    txt_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files


def scan_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        line = "1"
        while line != "":
            line = f.readline()
            if "key" in line:
                print(file_path)
                return


def search_files_regular(root_directory):
    txt_files = find_txt_files(root_directory)

    for f in txt_files:
        scan_file(f)


def search_files_parallel(root_directory, n_concurrent_threads):
    txt_files = find_txt_files(root_directory)

    for i in range(0, len(txt_files), n_concurrent_threads):
        parallel_files = txt_files[i : i + n_concurrent_threads]

        threads = [
            threading.Thread(target=scan_file, args=(f,)) for f in parallel_files
        ]

        for t in threads:
            t.start()
        for t in threads:
            t.join()


print("\n\n")
measure_time(search_files_regular, ["./rootDirectory"], "search_files_regular()")
measure_time(search_files_parallel, ["./rootDirectory", 16], "search_files_parallel()")
