# Random Number Merger

A Python script that demonstrates list manipulation, sorting algorithms, and file input/output operations. It generates random datasets and merges them into a single sorted master file.

## Functionality

The script performs the following operations automatically:
1.  **Generate:** Creates two separate lists of random integers (range 0-1000).
2.  **Sort & Save:** Sorts each list and saves them to `numbers1.txt` and `numbers2.txt`.
3.  **Merge:** Combines both lists into one master dataset.
4.  **Finalize:** Sorts the combined data and writes it to `all_numbers.txt`.

## Prerequisites

* Python 3.x

## Installation

1.  **Download the Script:**
    * Click the green **<> Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer.

2.  **Open Terminal:**
    * Navigate to the extracted folder.

        cd path/to/random-number-merger

## Usage

Run the script using Python:

    python combined.py

**Output Files:**
After running the script, check your folder for these three text files:
* `numbers1.txt`: The first set of sorted random numbers.
* `numbers2.txt`: The second set of sorted random numbers.
* `all_numbers.txt`: The complete, sorted list containing all numbers from the previous two files.
