/*
 * @Author: Jecosine
 * @Date: 2021-01-24 02:02:28
 * @LastEditTime: 2021-01-24 04:00:00
 * @LastEditors: Jecosine
 * @Description: Singleton Implementation
 */
import java.io.*;

public class Singleton {
    public Singleton() {
        
    }
    public static void main(String[] args) {
        System.out.println("?");
   }
}

/**
 * @description:
 * <ul>
 *  <li>lazy initialization [yes]</li>
 *  <li>thread safe         [no]</li></ul>
 */
class Singleton1 {
    
    private static Singleton1 INSTANCE = null;

    private Singleton1() {}

    public static Singleton1 getInstance() {
        if (INSTANCE == null)
            INSTANCE = new Singleton1();
        return INSTANCE;
    }
    
}

/**
 * @description: 使用了classloader的特性
 * <ul>
 *  <li>lazy initialization [no]</li>
 *  <li>thread safe         [yes]</li></ul>
 * 
 */
class Singleton2 {
    
    private static final Singleton2 INSTANCE = new Singleton2();

    private Singleton2() {}

    public static Singleton2 getInstance() {
        return INSTANCE;
    }
    
}

/**
 * @description: 使用了classloader的特性, 通过静态内部类的方式实现了懒加载
 * <ul>
 *  <li>lazy initialization [yes]</li>
 *  <li>thread safe         [yes]</li></ul>
 * 
 */
class Singleton3 {

    private Singleton3() {}
    
    private static class InnerSingleton {
        private static Singleton3 INSTANCE = new Singleton3();
    }
    
    public static Singleton3 getInstance() {
        return InnerSingleton.INSTANCE;
    }
}
