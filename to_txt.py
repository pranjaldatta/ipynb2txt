import json
import os
#from clean_meta import clean_meta_json, read_ipynb
import argparse
from glob import glob
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



def check_txt_exists(path, name):
    """
    Checks if a text file exists or not

    Parameters:
        -> path : path where to store txt file
        -> name : name of txt file

    Return: 
        -> 1 : if file is created
        -> 0 : file exists    
    """
    if not os.path.exists(os.path.join(path, name)):
        print("Creating file at ", os.path.join(path, name))
        try:
            os.popen("touch {}.txt".format(os.path.join(path, name)))
        except:
            print("error durin touching", path, name)
        return 1
    else:
        return 0

def convert(cells, path, name):
    _ = check_txt_exists(path, name)
    f = open("{}.txt".format(os.path.join(path, name)), mode="w+", encoding='UTF-8')
    try:
        count = 0
        for i in cells:
            if i['cell_type'] == 'code':
                f.write("#"*60+"\n")               
                f.write("#CODE:\n\n")
                for text in i['source'][:]:
                    f.write(text)
                
                if len(i['outputs']) > 0  :   
                    if i['outputs'][0]['output_type'] == 'stream' : 
                        f.write("\n\n"+"#Outputs: "+"\n\n")
                        if len(i['outputs']) > 0 : 
                            #print(i['outputs'][0])
                            for item in i['outputs'][0]['text']:
                                f.write(item)

                        f.write("\n"+"#"*60+"\n")
                        f.write("\n\n\n")
                    else:
                        print("Contains error in output. Rectify please."\
                                "Skipping error cell. Cell no:", count+1) 
                        f.write("\n"+"#"*60+"\n")
                        f.write("\n\n\n")                                        
                else:
                    f.write("\n"+"#"*60+"\n")
                    f.write("\n\n\n")                        
                count += 1
                #print("-"*50)
                      
            

    finally:     
        print("Closing")
        f.close()    
        
        


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="converts ipynb to txt")
    parser.add_argument("-l", "--loc", action="store", help="path to ipynb file")

    args = parser.parse_args()

    if os.path.isdir(args.loc):
        
        notebooks = glob(os.path.join(args.loc, "*.ipynb"))
        
        for nb in notebooks:
            path = os.path.dirname(nb)
            name = os.path.basename(nb).split(".")[0]
    
            cells = clean_meta_json(nb)
            convert(cells, path, name)

    elif not os.path.exists(args.loc):
        raise FileNotFoundError("{} not a valid path".format(args.loc))
    elif os.path.exists(args.loc):
        path = os.path.dirname(args.loc)
        name = os.path.basename(args.loc).split(".")[0]
    
        cells = clean_meta_json(args.loc)
        convert(cells, path, name)
    

