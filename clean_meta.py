import json


def read_ipynb(locfile):
    """
    reads an ipynb file and returns a string
    """
    f = open(locfile)
    ipynb_str = f.read()
    f.close()
    return ipynb_str

def clean_meta_json(locfile):
    """
    converts an ipynb to json. returns cell meta.

    Parameters: 
        -> locfile: location of file

    Returns: 
        -> Dictionary of cell meta    
    """
    string_file = read_ipynb(locfile)
    json_file = json.loads(string_file)
    try:
        cells = json_file["cells"]
    except:
        print("error!")    
    return cells

