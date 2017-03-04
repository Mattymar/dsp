# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > `pwd` - show current working directory path  
> `mkdir` - create a directory  
> `rm -r <directory>` - deletes a directory (and all of its contents)  
> `touch <filename>` - create a file  
> `rm <filename>` - deletes a file
> `mv <old_filename> <new_filename>` - rename a file  
> `ls -a` - list all contents (including hidden files and directories)  
> `cp <file to copy> <directory to copy to>` - copy a file from one directory to another  
> `cat <filename>` - outputs the contents of a file to the terminal  
> `grep <regex> <filename>` - "global regular expression", searches file for lines that match pattern and returns results


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - List files and directories in working directory  
> `ls -a` - List all contents (including hidden files and directories) in working directory   
> `ls -l` - List all contents of a directory in long format  
> `ls -lh` - List of contents in long format with human readable file sizes  
> `ls -lah` - List all contents (including hidden) in long format with human readable file sizes  
> `ls -t` - Order files and directories by the time they were last modified  
> `ls -Glp` - List files/directories in working directory in long format without group information and append an indicator (/, =, or @) to entries

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -d` - Displays only directories  
> `ls -g` - Long format without owner name  
> `ls -L` - Shows file/directory referenced by a symlink  
> `ls -og` - Long format without group or owner name  
> `ls -u` - Displays by file access time

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` is used to apply a command to a series of things. For example, suppose you wanted to remove all files from the current directory that began with the letter "a". You could run  
> `find . -name "a*.txt" | xargs rm`  
> and that would do it in one fell swoop.

 

