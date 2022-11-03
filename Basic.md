# Backward indexing in Python!!

Consider the string

```python
mystr="Hello";
```

Here the string is represented in array format as follows:

**Forward indexing**

| "H" | "e" | "l" | "l" | "o" |
|:----|:---:|:---:|:---:|----:|
|0    |1    |2    |3    |4    |

**Backward indexing**

| "H" | "e" | "l" | "l" | "o" |
|:----|:---:|:---:|:---:|----:|
|-5    |-4    |-3    |-2    |-1    |


That's why this statement prints `o`

```python

print(mystr[-1]);
```

---
