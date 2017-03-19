# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 8 different degrees (and one with no degree listed).  
> PhD - 31  
> ScD - 6  
> MS - 2  
> MPH - 2  
> MD - 1  
> JD - 1  
> MA - 1  
> B.S.Ed. - 1  


#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> There are 3 titles:  
> Professor - 13  
> Associate Professor - 12  
> Assistant Professor - 12  


#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']



#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> There are 4 different email domains. ['mail.med.upenn.edu', 'email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu']

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> [('Xie', {'degree': ' PhD', 'title': 'Assistant Professor of Biostatistics', 'email': 'dxie@upenn.edu'}), ('French', {'degree': ' PhD', 'title': 'Associate Professor of Biostatistics', 'email': 'bcfrench@mail.med.upenn.edu'}), ('Joffe', {'degree': ' MD MPH Ph.D', 'title': 'Professor of Biostatistics', 'email': 'mjoffe@mail.med.upenn.edu'})]


#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> [(('Phyllis A.', 'Gimotty'), {'email': 'pgimotty@upenn.edu', 'title': 'Professor of Biostatistics', 'degree': ' Ph.D'}), (('Wei-Ting', 'Hwang'), {'email': 'whwang@mail.med.upenn.edu', 'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.'}), (('Matthew W', 'Bryan'), {'email': 'bryanma@upenn.edu', 'title': 'Assistant Professor of Biostatistics', 'degree': ' PhD'})]


#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> [(('Scarlett L.', 'Bellamy'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Sc.D.', 'email': 'bellamys@mail.med.upenn.edu'}), (('Warren B.', 'Bilker'), {'title': 'Professor of Biostatistics', 'degree': 'Ph.D.', 'email': 'warren@upenn.edu'}), (('Matthew W', 'Bryan'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' PhD', 'email': 'bryanma@upenn.edu'}), (('Jinbo', 'Chen'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'jinboche@upenn.edu'}), (('Jonas H.', 'Ellenberg'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'jellenbe@mail.med.upenn.edu'}), (('Susan S', 'Ellenberg'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'sellenbe@upenn.edu'}), (('Rui', 'Feng'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D', 'email': 'ruifeng@upenn.edu'}), (('Benjamin C.', 'French'), {'title': 'Associate Professor of Biostatistics', 'degree': ' PhD', 'email': 'bcfrench@mail.med.upenn.edu'}), (('Phyllis A.', 'Gimotty'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D', 'email': 'pgimotty@upenn.edu'}), (('Wensheng', 'Guo'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D', 'email': 'wguo@mail.med.upenn.edu'}), (('Yenchih', 'Hsu'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'hsu9@mail.med.upenn.edu'}), (('Rebecca A', 'Hubbard'), {'title': 'Associate Professor of Biostatistics', 'degree': ' PhD', 'email': 'rhubb@mail.med.upenn.edu'}), (('Wei-Ting', 'Hwang'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'whwang@mail.med.upenn.edu'}), (('Marshall M.', 'Joffe'), {'title': 'Professor of Biostatistics', 'degree': ' MD MPH Ph.D', 'email': 'mjoffe@mail.med.upenn.edu'}), (('J. Richard', 'Landis'), {'title': 'Professor of Biostatistics', 'degree': ' B.S.Ed. M.S. Ph.D.', 'email': 'jrlandis@mail.med.upenn.edu'}), (('Mingyao', 'Li'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'mingyao@mail.med.upenn.edu'}), (('Hongzhe', 'Li'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D', 'email': 'hongzhe@upenn.edu'}), (('Yimei', 'Li'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'liy3@email.chop.edu'}), (('A. Russell', 'Localio'), {'title': 'Associate Professor of Biostatistics', 'degree': ' JD MA MPH MS PhD', 'email': 'rlocalio@upenn.edu'}), (('Nandita', 'Mitra'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'nanditam@mail.med.upenn.edu'}), (('Knashawn H.', 'Morales'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Sc.D.', 'email': 'knashawn@mail.med.upenn.edu'}), (('Kathleen Joy', 'Propert'), {'title': 'Professor of Biostatistics', 'degree': ' Sc.D.', 'email': 'propert@mail.med.upenn.edu'}), (('Mary E.', 'Putt'), {'title': 'Professor of Biostatistics', 'degree': ' PhD ScD', 'email': 'mputt@mail.med.upenn.edu'}), (('Sarah Jane', 'Ratcliffe'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'sratclif@upenn.edu'}), (('Michelle Elana', 'Ross'), {'title': 'Assistant Professor is Biostatistics', 'degree': ' PhD', 'email': 'michross@upenn.edu'}), (('Jason A.', 'Roy'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'jaroy@mail.med.upenn.edu'}), (('Mary D.', 'Sammel'), {'title': 'Professor of Biostatistics', 'degree': ' Sc.D.', 'email': 'msammel@cceb.med.upenn.edu'}), (('Pamela Ann', 'Shaw'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' PhD', 'email': 'shawp@upenn.edu'}), (('Russell Takeshi', 'Shinohara'), {'title': 'Assistant Professor of Biostatistics', 'degree': '0', 'email': 'rshi@mail.med.upenn.edu'}), (('Haochang', 'Shou'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'hshou@mail.med.upenn.edu'}), (('Justine', 'Shults'), {'title': 'Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'jshults@mail.med.upenn.edu'}), (('Alisa Jane', 'Stephens'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'alisaste@mail.med.upenn.edu'}), (('Andrea Beth', 'Troxel'), {'title': 'Professor of Biostatistics', 'degree': ' ScD', 'email': 'atroxel@mail.med.upenn.edu'}), (('Rui', 'Xiao'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' PhD', 'email': 'rxiao@mail.med.upenn.edu'}), (('Sharon Xiangwen', 'Xie'), {'title': 'Associate Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'sxie@mail.med.upenn.edu'}), (('Dawei', 'Xie'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' PhD', 'email': 'dxie@upenn.edu'}), (('Wei (Peter)', 'Yang'), {'title': 'Assistant Professor of Biostatistics', 'degree': ' Ph.D.', 'email': 'weiyang@mail.med.upenn.edu'})]


Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

