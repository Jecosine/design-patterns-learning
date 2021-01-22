'''
Author: Jecosine
Date: 2021-01-22 03:35:46
LastEditTime: 2021-01-22 11:20:54
LastEditors: Jecosine
Description: Folder structure generator
'''

import os
import json
import copy
import sys

# folder structure dict
# has only one key: root
FOLDER_STRUCTURE = {
    'name': None, 
    'children': [
        {
            'name': 'Creational', 
            'children': [
                {'name': 'AbstractFactory', 'children': []}, 
                {'name': 'Builder', 'children': []}, 
                {'name': 'FactoryMethod', 'children':[]},
                {'name': 'Prototype', 'children': []}, 
                {'name': 'Singleton', 'children': []}
            ]
        }, 
        {
            'name': 'Structural', 
            'children': [
                {'name': 'AdapterBridge', 'children': []}, 
                {'name': 'Composite', 'children': []},
                {'name': 'Decorator', 'children': []}, 
                {'name': 'Facade', 'children': []}, 
                {'name': 'Flyweight', 'children': []}, 
                {'name': 'Proxy', 'children': []}
            ]
        }, 
        {
            'name': 'Behavioral', 
            'children': [
                {'name': 'ResponsibilityChain', 'children': []}, 
                {'name': 'Command', 'children': []},
                {'name': 'Interpreter', 'children': []}, 
                {'name': 'Iterator', 'children': []}, 
                {'name': 'Mediator', 'children': []}, 
                {'name': 'Memento', 'children': []}, 
                {'name': 'Observer', 'children': []}, 
                {'name': 'State', 'children': []}, 
                {'name': 'Strategy', 'children':[]}, 
                {'name': 'TemplateMethod', 'children': []}, 
                {'name': 'Visitor', 'children': []}
            ]
        }
    ]
}
BASE_PATH = os.path.abspath('.')
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("[Usage] python FolderGenerator.py <your-language-name>. \n\t e.g.\npython FolderGenerator.py C")
    if os.path.exists(path):
        os.chdir(path)
    else:
        os.mkdir(path)
    print("Make dir {}".format(path))
    os.chdir(path)
    make_subdir(FOLDER_STRUCTURE)
    
def make_subdir(d):
    for i in d["children"]:
        if i["name"]:
            os.mkdir(i["name"])
            os.chdir(i["name"])
            # mdfile = os.path.join(BASE_PATH, 'doc/{}.md'.format(i["name"]))
            # if not os.path.exists(mdfile):
            #     with open(mdfile, 'w') as f:
            #         pass
        make_subdir(i)
        if i["name"]:
            os.chdir("..")


def file_generator():
    """
    Generate markdown file to ./doc
    """

if __name__ == "__main__":
    main()
# make_subdir(FOLDER_STRUCTURE)