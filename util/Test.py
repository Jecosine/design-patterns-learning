'''
Author: Jecosine
Date: 2021-01-22 05:43:45
LastEditTime: 2021-01-22 05:44:02
LastEditors: Jecosine
Description: Test
'''

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

