# Python --note

[TOC]

### identifier

* the fist character must be a letter/'_'
* the others can be letter/num/'_'
* identifier is case sensitive
* Python3 can even use Chinese char

### note

* single-line: #
* multi-lines: """"""

### code block

Python uses indent to splite code block

### string

* '' is the same as "" in Python
* multi-lines string: """"""
* r"" : r disable escape in ""
* operator: + to connect and * to reduplicate
* 2 types of index: 0 beginning; -1 end;

### import

* import somemodule
* from somemodule import somefunction

### variable

* In python, a variable has no type (while object has).
* A variable is only a pointer pointing to an object

```python
a = "Hello,world!"
b = [5,2,0]
# a is a pointer pointed to a string object
# b is a pointer pointed to a list object
```





## data type

### num

* int float bool complex
* type(): view data type
* isinstance(a,int): judge data type
* notice: 

```python
>>> 1 is True
False
>>> 0 is False
True
```

* in hybrid operation, int will be transformed to float

## Function

### definition

```python
def fun_name(arg1,arg2):
    "function body"
    ...
    ...
    
    return 
```

## Class

### definition

```python
class ClassName:
    """A class example"""
    
    def __init__(self,arg1,arg2):
        """Thie method will be automatically called when an instantiation happens"""
        """A method is distinguished to a function by the first argument(self)"""
        """arg1,arg2 are used to initialize attibutes in this class, they are incoming when an instantiation happens"""
        
# A complete example
class Student:
    """A class for students"""
    
    name = ""
    grade = ""
    major = ""
    ID = 0
    
    def __init__(self,name,grade,major,ID):
        """initialize fundamental attribution"""
        self.name = name
        self.garde = grade
        self.major = major
        self.ID = ID
        
    def selfintro(self):
        """A self-introduction"""
        print("I'm",self.name,"in grade",self.grade)
```
