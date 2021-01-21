'''
Author: Jecosine
Date: 2021-01-22 03:35:46
LastEditTime: 2021-01-22 05:43:27
LastEditors: Jecosine
Description: Folder structure generator
'''

import os
import json
import copy

# folder structure dict
# has only one key: root
FOLDER_STRUCTURE = {'name': None, 'children': [{'name': 'Creational', 'children': [{'name': 'AbstractFactory', 'children': []}, {'name': 'Builder', 'children': []}, {'name': 'FactoryMethod', 'children':
                                                                                                                                                                      []}, {'name': 'Prototype', 'children': []}, {'name': 'Singleton', 'children': []}]}, {'name': 'Structural', 'children': [{'name': 'AdapterBridge', 'children': []}, {'name': 'Composite', 'children': []}, {'name': 'Decorator', 'children': []}, {'name': 'Facade', 'children': []}, {'name': 'Flyweight', 'children': []}, {'name': 'Proxy', 'children': []}]}, {'name': 'Behavioral', 'children': [{'name': 'ResponsibilityChain', 'children': []}, {'name': 'Command', 'children': []}, {'name': 'Interpreter', 'children': []}, {'name': 'Iterator', 'children': []}, {'name': 'Mediator', 'children': []}, {'name': 'Memento', 'children': []}, {'name': 'Observer', 'children': []}, {'name': 'State', 'children': []}, {'name': 'Strategy', 'children':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      []}, {'name': 'TemplateMethod', 'children': []}, {'name': 'Visitor', 'children': []}]}]}
s = """- Creational
  - AbstractFactory  
  - Builder
  - FactoryMethod  
  - Prototype
  - Singleton
- Structural
  - AdapterBridge
  - Composite
  - Decorator
  - Facade
  - Flyweight
  - Proxy
- Behavioral
  - ResponsibilityChain
  - Command
  - Interpreter
  - Iterator
  - Mediator
  - Memento
  - Observer  
  - State
  - Strategy
  - TemplateMethod
  - Visitor"""

l = s.split("\n")
template = {"name": None, "children": []}
root = copy.deepcopy(template)
parent = root
current = []
for i in l:
    parent["children"] = current
    x = copy.deepcopy(template)
    x["name"] = i.strip().split("-")[-1].strip()
    if i[0] == " ":
        current.append(x)
    else:
        root["children"].append(x)
        parent = x
        current = []
