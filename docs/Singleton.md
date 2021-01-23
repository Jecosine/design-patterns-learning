# Singleton Pattern

## Description
<div id="description"></div>
Ensure a class has only one instance, and provide a global point of access to it.

确保只有一个实例, 并且自行实例化并向整个系统提供这个实例

- 确保在一个应用中只产生一个实例
- 这个实例时自己进行实例化的

下面的`java`例子展示了基本的逻辑, 但是它是一个**未考虑线程安全**的例子
```java
public class Singleton {
    private final Singleton singleton = null;
    // get instance
    public static Singleton getInstance() {
        if(singleton == null) {
            singleton = new Singleton();   
        }
        return singleton;
    }

    // use private constructor to ensure singleton in application
    private Singleton() {}

    // other method
    // ...
}
```

## Advantages

- 内存中只存在一个实例,减少内存开支
- 只产生一个实例
- 避免资源的多重占用,同时只有一个进程进行资源访问


## Disadvantages

- 难以拓展, 一般单例模式没有接口
- 不容易进行测试, 未完成的单例模式, 不能进行测试
- 单例模式与单一职责原则冲突

## Sceneries

- 需要共享访问点和数据
- 创建对象的开销过大
- 需要定义大量的静态常量和静态方法
  
## Attentions

单例模式存在多种实现方式. 主要注意的地方就是**线程同步**, 在高并发的情况下可能产生多个实例

如在上面<a href="#description">Description</a>的例子的`getInstance`函数中, 在高并发情况下, 存在一个时间段, 在第一个进程Singleton实例生成之前, 第二个进程的getInstance中`singleton == null`的判断也会为真

## Extensions

**有上限的单例模式**  
存在一些需求, 比如数据库的连接池, 如果有多个能够和数据库交互的连接的话, 相比只有一个连接, 也许会对性能有一定的提升.

## Implementation

### Lazy Initialization

实例在第一次调用的时候才会被初始化, 避免内存浪费

### Thread Security

线程安全性, 在多线程的情况下是否适用

### Java

