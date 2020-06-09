# ipynb2txt
Converts ipynb files to txt files. 

It's kinda irritating to manually convert ipynb notebooks to txt files for submission. Hence this tool! A directory full of multiple ipynb files or a single ipynb file, this tool handles them all. Saves the txt file in the same directory as the notebook and with the same name! 

**PS:** It also keeps outputs! If an output cell with error is encountered, it throws a note and skips the output cell. (Fix the error and rerun, the previous txt file will be replaced as if nothing happened!)

## Usage

```
python to_txt.py -l <full path to directory or ipynb file>
```
