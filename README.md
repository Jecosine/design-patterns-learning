# Design Patterns Learning 



## Description

本仓库计划包含学习设计模式过程中使用的各种语言实现  
列出预计实现的设计模式

- [Creational](doc/Creational.md)
  - [Abstract Factory](doc/abstract-factory.md)  
  - [Builder](doc/Builder.md)
  - [Factory Method](doc/FactoryMethod.md)  
  - [Prototype](doc/Prototype.md)
  - [Singleton](doc/Singleton.md)
- [Structural](doc/Structural.md)
  - [Adapter Bridge](doc/AdapterBridge.md)
  - [Composite](doc/Composite.md)
  - [Decorator](doc/Decorator.md)
  - [Facade](doc/Facade.md)
  - [Flyweight](doc/Flyweight.md)
  - [Proxy](doc/Proxy.md)
- [Behavioral](doc/Behavioral.md)
  - [Chain of Responsibility](doc/ResponsibilityChain.md)
  - [Command](doc/Command.md)
  - [Interpreter](doc/Interpreter.md)
  - [Iterator](doc/Iterator.md)
  - [Mediator](doc/Mediator.md)
  - [Memento](doc/Memento.md)
  - [Observer](doc/Observer.md)
  - [State](doc/State.md)
  - [Strategy](doc/Strategy.md)
  - [Template Method](doc/TemplateMethod.md)
  - [Visitor](doc/Visitor.md)

### Language

计划包含的语言实现

- [ ] C# 
- [ ] Python
- [ ] Java
  - [ ] JavaSE
  - [ ] JavaEE (Spring)
- [ ] Go
- [ ] Lua
- [ ] JavaScript
- [ ] C++ (?)

### Structure

每种语言有对应文件夹, 文件夹下的结构按照设计模式的分级组织. 详见 `ExampleLanguage` 文件夹

文件夹分级如下

<pre style="font-family: 'FiraCode NF'; font-variant-ligatures: common-ligatures iscretionary-ligatures historical-ligatures;">
Your-Language
├─Behavioral
│  ├─Command
│  ├─Interpreter
│  ├─Iterator
│  ├─Mediator
│  ├─Memento
│  ├─Observer
│  ├─ResponsibilityChain
│  ├─State
│  ├─Strategy
│  ├─TemplateMethod
│  └─Visitor
├─Creational
│  ├─AbstractFactory
│  ├─Builder
│  ├─FactoryMethod
│  ├─Prototype
│  └─Singleton
└─Structural
    ├─AdapterBridge
    ├─Composite
    ├─Decorator
    ├─Facade
    ├─Flyweight
    └─Proxy
</pre>

手动创建这些文件夹会占用很多时间,所以可以使用 `util`下的脚本 `FolderGenerator.py` 创建具备上述结构的文件夹.首先确保自己在项目根目录下
```bash
> pwd
/your-path/design-patterns-learning

> python util/FolderGenerator.py Your-Language
Make dir Your-Language
```

## Reference

[1] *Design Patterns Elements of Reusable Object-Oriented Software by Erich Gamma, Richard Helm, Ralph Johnson, John M. Vlissides*  
[2] *设计模式之禅 秦小波*