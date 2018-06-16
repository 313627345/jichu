# 递归函数
定义：在函数内调用当前函数本身的函数就是递归；</br>
记点：递归函数要注意每次递归都会生成一个栈，栈在超出系统默认值就会报错。</br>
例如：</br>
def fact(n):</br>
    if n==1:</br>
        return 1</br>
    return n * fact(n - 1)</br>
    
 例如：</br>
 fact(100) 程序可以运行，当fact(1000)程序就会报错。</br>
 如下:</br>
 /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/dong/Desktop/jichu/digui.py </br>
Traceback (most recent call last): </br>
  File "/Users/dong/Desktop/jichu/digui.py", line 17, in <module> </br>
    print(fact(1000))
  File "/Users/dong/Desktop/jichu/digui.py", line 15, in fact </br>
    return n * fact(n - 1)
  File "/Users/dong/Desktop/jichu/digui.py", line 15, in fact </br>
    return n * fact(n - 1) </br>
  File "/Users/dong/Desktop/jichu/digui.py", line 15, in fact </br>
    return n * fact(n - 1) </br>
  [Previous line repeated 994 more times] </br>
  File "/Users/dong/Desktop/jichu/digui.py", line 13, in fact </br>
    if n==1: </br>
RecursionError: maximum recursion depth exceeded in comparison </br>

解释：这是由于系统有默认栈的深度，</br>
解决方法：在程序表头前加入如下代码，修改栈的默认深度值（默认深度值972）</br>
import sys</br>
sys.setrecursionlimit(1000000) </br>

 
