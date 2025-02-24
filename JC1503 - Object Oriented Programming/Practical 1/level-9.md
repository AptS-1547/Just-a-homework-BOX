# level-9

## Question

This is a job interview question.  
What is the output of the following code and explain why:  

```python
def f(x,l=[]): 
    for i in range(x): 
        l.append(i*i) 
        print(l) 
 
f(2) 
f(3,[3,2,1])
f(3)
```

## Answer

f(2) will output the following:

```python
[0]
[0, 1]
```

f(3,[3,2,1]) will output the following:

```python
[3, 2, 1, 0]
[3, 2, 1, 0, 1]
[3, 2, 1, 0, 1, 4]
```

f(3) will output the following:

```python
[0, 1, 0]
[0, 1, 0, 1]
[0, 1, 0, 1, 4]
```

The reason for this is that the default value of the list `l` is an empty list. When the function is called with the default value, the same list is used across all calls to the function. This is because the default value is evaluated only once when the function is defined, not each time the function is called.