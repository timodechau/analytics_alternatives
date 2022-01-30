import os

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap,CommentedSeq

yaml = YAML()

ALTERNATIVES_FOLDER = '../alternatives'
DOCS_FOLDER = '../alternatives_docs'

def get_alternatives_files(source_folder):
    alt_db = []
    for path, subdirs, files in os.walk(source_folder):
        if files != []:
            for alt_file in files:
                
                alt_db.append({
                    'path': f"{path}/{alt_file}",
                    'alternative': path.split('/')[-1]
                })
                
                
    return alt_db

def add_headline(headline,level,md_data):
    headline = f"{'#' * level} {headline.capitalize().replace('_',' ')}  \n\n"
    md_data += headline
    return md_data

def add_label_text(item,md_data):
    if item[0] in ['url','link']:
        text = f"[{item[1]}]({item[1]})  \n\n" 
    else:  
        text = f"{item[0].capitalize().replace('_',' ')}:\n{item[1]}  \n\n"
    md_data += text
    return md_data

def yaml_block(value,md_data,start_level):
    if isinstance(value,CommentedMap):
        # print(f"commented map: {value}")
        for item in value.items():
            if isinstance(item[1], str):
                if item[0] == 'name':
                    md_data = add_headline(item[1],start_level + 1, md_data)
                else:    
                    md_data = add_label_text(item,md_data)
                # print(f"after map: {md_data}")


    if isinstance(value,CommentedSeq):
        # print(f"commented seq: {value}")
        for item in value:
            # print(f"commented seq - item: {type(item)}")
            md_data = yaml_block(item,md_data,start_level + 1)
    
    return md_data


def yaml_to_md(alt_yaml,md_data):
    with open(alt_yaml['path']) as f:
        data = yaml.load(f)
        for item in data.items():
            
            data_key = item[0]
            value = item[1]
            
            #Block Headlines
            if data_key == "name":
                md_data = add_headline(value,1,md_data)
            else:
                md_data = add_headline(data_key,2,md_data)
                
            md_data = yaml_block(value,md_data,2)

             
    return md_data

def save_md_document(md_document,path):
    file_name = f"{DOCS_FOLDER}/{path.split('/')[2]}.md"
    f = open(file_name,'w')
    f.write(md_document)
    f.close()

def main():
    md_document = ""
    alt_db = get_alternatives_files(ALTERNATIVES_FOLDER)
    for alt_yaml in alt_db:
        md_document = yaml_to_md(alt_yaml,md_document)
        save_md_document(md_document,alt_yaml['path'])

if __name__ == '__main__':
    main()