# Lab 6: Parallel Processing and Performance Comparison

This lab demonstrates the implementation and performance comparison of sequential vs parallel processing in Python using threading. The lab consists of two main exercises that showcase different use cases for parallel processing.

## Files Structure

```
lab_6/
├── lab_6_1.py          # Web scraping with parallel processing
├── lab_6_2.py          # File system scanning with parallel processing
├── utils.py            # Utility functions for timing and setup
├── rootDirectory/      # Test directory for file scanning
└── README.md           # This file
```

## lab_6_1.py - Web Scraping Performance Comparison

### Purpose
This script compares the performance of sequential vs parallel web scraping operations. It fetches webpage titles from multiple URLs and measures execution time for both approaches.

### Setup

Fetching and parsing are implemented using third-party libraries. Make sure to install them before executing the script

```bash
pip install requests beautifulsoup4
```

### How to Run
```bash
python lab_6_1.py
```

### What it does
1. **Defines a list of 10 URLs** to scrape

2. **Implements functions**:
   - `page_title(url)`: Fetches a webpage and extracts its title using `requests` and `BeautifulSoup`
   - `process_websites_regular(urls)`: Processes URLs sequentially, one after another
   - `process_websites_parallel(urls, threads_count=4)`: Processes URLs in parallel using threading (default: 4 threads, but called with 10 threads in the script)

3. **Measures execution times** using the `measure_time()` utility function

### Expected Output
The script will display:
- Webpage titles as they are fetched
- Execution time for sequential processing
- Webpage titles as they are fetched (yes, once again)
- Execution time for parallel processing

## lab_6_2.py - File System Scanning Performance Comparison
 
### Purpose
This script compares the performance of sequential vs parallel file system scanning operations. It searches for `.txt` files containing the word "key" in a directory structure.

### Setup

The `lab_6_2.py` script requires a directory structure with `.txt` files to scan. The `rootDirectory` folder is initially empty, so you need to populate it with test files.

One way (there are others) to do that is to run this command:

```bash
# Navigate to the lab_6 directory first
cd lab_6
python -c "from utils import set_up_task; set_up_task('./rootDirectory', max_depth=4, max_dirs=2, max_files=2)"
```

Executing this command may result in this kind of file structure:

```
rootDirectory/
├── ANSWER.TXT                    # Contains the path to the file with "key"
├── file_1.txt                    # Random content
├── file_2.txt                    # Random content
├── subdir_1_1/
│   ├── file_1.txt                # Random content
│   ├── file_2.txt                # Random content (might contain "key")
│   └── subdir_2_1/
│       ├── file_1.txt            # Random content
│       └── subdir_3_1/
│           └── file_1.txt        # Random content
└── subdir_1_2/
    ├── file_1.txt                # Random content
    └── subdir_2_1/
        └── file_1.txt            # Random content
```

*Note: Since the function uses random generation, the exact structure will be random each time you run it. The example above shows just one of many possible outcomes. The actual directory and file counts may vary*

### How to Run
```bash
python lab_6_2.py
```

### What it does
1. **Implements functions**:
    - `find_txt_files(directory)`: Recursively finds all `.txt` files in the given directory
    - `scan_file(file_path)`: Reads a file and searches for the word "key"
    - `search_files_regular(root_directory)`: Scans files sequentially
    - `search_files_parallel(root_directory, n_concurrent_threads)`: Scans files in parallel using threading (default: 16 threads)
2. **Measures execution times** using the `measure_time()` utility function

### Clean Up
After running `lab_6_2.py`, you might want to clean up the test directory to remove all test files and subdirectories, start fresh for another test run, or free up disk space
 
You can wipe the entire file structure with the `cleanup()` utility function if needed. Here's an example call of `cleanup()` using a console command:

```bash
python -c "from utils import cleanup; cleanup('./rootDirectory')"
```

All inner files and directories will be removed, while the `rootDirectory` itself will remain

### Expected Output
The script will display:
- File path that contain the word "key"
- Execution time for sequential scanning
- Same file path that contain the word "key"
- Execution time for parallel scanning

## Running the Complete Lab

To run the whole lab, you can navigate to `lab_6/` directory and execute these commands:

```bash
pip install requests beautifulsoup4 # 0 (optional) Install required dependencies if needed

python lab_6_1.py # 1 Run web scraping exercise

python -c "from utils import set_up_task; set_up_task('./rootDirectory')" # 2 Set up test directory for file scanning

python lab_6_2.py # 3 Run file scanning exercise

python -c "from utils import cleanup; cleanup('./rootDirectory')" # 4 (optional) Clean up test directory 

pip uninstall requests beautifulsoup4 -y # 5 (optional) Uninstall packages 
```

## Expected Performance Results

Parallel processing should greatly outpace sequential processing in both file system scanning and web scraping