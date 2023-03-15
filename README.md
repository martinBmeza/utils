# Utils scripts


## Making command line commands

1. Mark the python file as executable

```
$ chmod +x my_script.py
```
2. Add an interpreter shebang. With this, we can drop the extension 

```python
#!/usr/bin/env python
```

3. Add the program to the PATH
Create a user bin directory and then add it to the PATH

```
$ mkdir -p ~/bin
$ cp my_script ~/bin
```
In order to add this to the PATH permanently, do:
+ add this line to .bash_profile in your home directory:
```
$ export PATH=$PATH":$HOME/bin"
```
+ reload the shell 
