# Factory Method

## Description

<div id="description"></div>

Define an interface for creating an object,but let subclasses decide which class to instantiate.Factory Method lets a class defer instantiation to subclasses.

定义一个用于创建对象的接口, 但是让子类来决定生成哪一个类的实例. 工厂模式将一个类的实例化推迟到其子类

![image-20210124044057946](img\image-20210124044057946.png)

## Advantages

- 封装性好, 代码结构清晰, 代码的耦合度低
- 扩展性好, 产品类增加时修改量小


## Disadvantages

## Sceneries

- 创建另一个类之前无法预知要创建的类的类型
- 需要子类来指定创建的类
- 需要灵活, 可扩展的框架时
- 可以在测试驱动框架中使用

## Implementation