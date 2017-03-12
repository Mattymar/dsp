# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are both sequences of values that are indexed by integers. The values can be accessed in much the same ways, including slicing. Lists are mutable, while tuples are not. Tuples can set multiple variables simultaneously. 
> Tuples can serve as keys in a dictionary, since they are immutable and dictionary keys must be immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets can be thought of as lists without any repeating elements. Since all values of a set must be unique, you'll often use a set to ensure you don't have any repeating values in a collection.  For example, if you wanted to find all teams who've won at least one Super Bowl in the last ten years, you might first make a list: 
> `super_bowl_winners = list('NE', 'DEN', 'NE', 'SEA', 'BAL', 'NYG', 'GB', 'NO', 'PIT', 'NYG')`
> And use a set to weed out the repeats:
> `set(super_bowl_winners`
> Sets are faster for lists in finding elements because they can make use of hashing, while lists my search through each element one by one.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is used to create an unnamed "throw-away" function. It's used a lot when passing as an argument to another function, when you don't plan on using the function again for anything else.  
> The sorted() function is a good example, as you'll often need to apply some computation to tell teh function what you want to sort by.
> `people_ages = [('Smith', 'John', 28), ('Jones', 'Jane', 26), ('Maresca', 'Matt', 33)]
> sorted(people_ages, key=lambda people: people[2])`

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a quick way to apply a function to every item in a list in one line. For example:
> `a = [1, 2, 3, 4, 5, 6]
> [x % 2 for x in a]`
> This takes a list and sets the value 1 for odd numbers and 0 for even.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





