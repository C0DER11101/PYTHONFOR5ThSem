# About [1.py](https://github.com/C0DER11101/PYTHONFOR5ThSem/blob/DaaPY/FileIOWithPython/1.py)

`f` used here is a file pointer.

`f.read()` basically reads the contents from `hello.txt` and whatever is read is stored in a separate variable called `content`.

`print(content)` prints those stored contents that were read from `hello.txt`.


Remember one thing, 

```python

f=open("hello.txt");

content=f.read();

print(content);

for line in f:
	print(line);
```
never do this, once you have used a file pointer, if you are re-using that same file pointer without closing the file, then it's not going to give you anything because that file pointer has already been used in reading the text file, so it's "empty" now. If you want to re-use `f` then you must close the file `hello.txt` using `f.close();` and then again re-open the same file using the same pointer `f`.

```python
f=open("hello.txt");

print(f.readlines());
```

The `readlines()` function reads the contents from `hello.txt` and stores them in a list along with all the escape characters!!
