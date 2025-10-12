import os
import shutil
from random import randint
import time

# ------------------------
# ----- common utils -----
# ------------------------


def measure_time(function, args, function_name="function"):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    duration = end_time - start_time
    print(f"{function_name} took {duration:.2f} seconds to complete.")


# --------------------------
# ----- task 6.2 utils -----
# --------------------------


def cleanup(root_directory="./rootDirectory"):
    """Remove all contents inside the specified directory, leaving it empty."""
    if os.path.exists(root_directory):
        shutil.rmtree(root_directory)
        os.makedirs(root_directory)  # Recreate the empty root directory
    else:
        print(f"The directory '{root_directory}' does not exist.")


def set_up_task(root_directory="./rootDirectory", max_depth=4, max_dirs=6, max_files=6):
    """Set up a directory structure with text files. Some random text file will contain word 'key'"""

    text_files = []

    def create_txt_files(directory, num_files):
        RND_STRINGS = [
            "pslZVrWSuRaRjngqpgDz\n",
            "bWdUcimbdzHJigTHVuHZ\n",
            "JlufnoCuoTSUORtjPpZR\n",
            "qdoDjiSTCliAQHvRQxlj\n",
            "dafhOzUjRnLaWwwsdufS\n",
            "NOPDQFxilrAqCUTXXOcD\n",
            "IDWnlrWtntrNbXPpiMum\n",
            "RLcQwTuRhXUhVFaUnhNT\n",
            "oCPZdjMAIblmLoMDccqd\n",
            "wbccmSQLAvtJihhuOcPU\n",
            "cJRmtRINzVlgnNBbdvFt\n",
            "CRTcqJpTguafcIQGiBPm\n",
            "lRgqOGWLZcnRILuOhNBW\n",
            "BLfxsOnPdCSzhhLGZFXp\n",
            "wSWwShDnOxBwPBUodVQN\n",
        ]

        for i in range(num_files):
            file_path = os.path.join(directory, f"file_{i + 1}.txt")
            text_files.append(file_path)
            with open(file_path, "w") as f:
                for i in range(4):
                    f.write(RND_STRINGS[randint(0, len(RND_STRINGS) - 1)])

    if not os.path.exists(root_directory):
        os.makedirs(root_directory)

    def create_structure(current_directory, current_depth):
        if current_depth < max_depth:
            num_subdirs = randint(1, max_dirs)
            for subdir_index in range(num_subdirs):
                subdir_name = f"subdir_{current_depth + 1}_{subdir_index + 1}"
                subdir_path = os.path.join(current_directory, subdir_name)
                os.makedirs(subdir_path, exist_ok=True)

                num_files_in_subdir = randint(0, max_files)
                create_txt_files(subdir_path, num_files_in_subdir)

                create_structure(subdir_path, current_depth + 1)

    create_structure(root_directory, 0)
    path_to_key_file = text_files[randint(0, len(text_files) - 1)]
    print(path_to_key_file)
    with open(path_to_key_file, "a") as f:
        f.write("key")
    with open(os.path.join(root_directory, "ANSWER.TXT"), "w") as f:
        f.write(f"k3y file:\n{path_to_key_file}")
