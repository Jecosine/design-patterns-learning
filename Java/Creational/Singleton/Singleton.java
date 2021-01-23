/*
 * @Author: Jecosine
 * @Date: 2021-01-24 02:02:28
 * @LastEditTime: 2021-01-24 02:39:48
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
 * method 1
 *  lazy initialization [yes]
 *  thread safe         [yes]
 */
class Singleton1 {
    
    private static Singleton1 INSTANCE = null;

    private static Singleton1 getInstance() {
        if (INSTANCE == null)
            INSTANCE = new Singleton1();
        return INSTANCE;
    }
    
}
/**
 * @description: 
 * method 2
 *  lazy initialization [no]
 *  thread safe         [yes]
 * 使用了classloader的特性，
 */
class Singleton2 {
    
    private static final Singleton2 INSTANCE = new Singleton2();

    private static Singleton2 getInstance() {
        return INSTANCE;
    }
    
}

