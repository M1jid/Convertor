# Convertor
Convert persian xml file to yolo format
# Plate Data Processing

This repository contains a Python script for processing plate data from XML files.

## Dependencies

- `os`
- `shutil`
- `xmltodict`

## Description

The script reads XML files containing plate data, extracts relevant information, and writes it to text files. Additionally, it copies JPEG images to an output directory.

## Classes

The following classes are defined for mapping characters to numerical values:

```python
Class = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "الف": 10, "ب": 12, "پ": 13, "ت": 14, "ث": 15, "ج": 16, "چ": 17, "ح": 18, "خ": 19, "د": 20, "ذ": 21, "ر": 22, "ز": 23, "ژ (معلولین و جانبازان)": 24, "س": 25, "ش": 26, "ص": 27, "ض": 28,
"ط": 29, "ظ": 30, "ع": 31, "غ": 32, "ف": 33, "ق": 34, "ک": 35, "گ": 36, "ل": 37, "م": 38, "ن": 39, "و": 40, "ه‍": 41, "ی": 42}
```
Usage
Make sure you have the necessary dependencies installed.
Modify the images and output_pass variables to specify input and output directories.
Run the script
