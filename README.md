# StatusGrabber
Takes a CSV list of domains and outputs an identical CSV with HTTP status codes in column B.

## Required arguments
**-i, --input** | The file for the program to use
**-o, --output** | The destination of the output file

## Optional arguments
**-nv, --noverify** | Toggle to disable SSL verification

## Command syntax
```python grabber.py -i [input filepath] -o [output filepath] -nv```

## Input file specifications
Input files should conform to the following requirements:
- Must be CSV format
- No header row. Domains should start on row 1
- No more than 1 column
- Domains must have a protocol, either http:// or https://
