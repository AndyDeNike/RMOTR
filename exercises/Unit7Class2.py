#Unit7/Functional Programming/Class2

'''
1) First Line from File

Write a function that receives a path to a text file as parameter, and returns the first line of that file.

Example:

  read_first_line('test-file.txt')  # "this is the first line"
'''

def read_first_line(path):
    with open(path) as fp:
        return fp.readline()

# Test Cases 

import tempfile

def test_read_first_line():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert read_first_line(fp.name) == 'this is line 1\n'

    fp.close()



'''
2) Nth Line from File

Write a function that receives a path to a text file and a line number as parameter, and returns the N-th line of that file.

Example:

read_line_number('test-file.txt', 2)  # "this is the line number 2"
'''

def read_line_number(filepath, line_number):
    with open(filepath) as fp:
        #readlines() returns a list of all the lines, indexed 
        return fp.readlines()[line_number-1]

# Test Cases 

import tempfile

def test_read_second_line():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert read_line_number(fp.name, 2) == 'this is line 2\n'

    fp.close()

#

import tempfile

def test_read_last_line():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert read_line_number(fp.name, 3) == 'this is line 3\n'

    fp.close()



'''
3) Count Lines in File

Write a function that receives a path to a text file as parameter, and 
returns the amount of lines that text file has.

count_lines('test-file.txt')  # 10
'''

def count_lines(filepath):
    with open(filepath) as fp:
        return len(fp.readlines())
        #count = 0
        #for line in fp:
            #count += 1 
        #return count

# Test Cases

import tempfile

def test_count_lines():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert count_lines(fp.name) == 3

    fp.close()



'''
4) Find Line with String

Write a function that receives a file path and a string as parameters, and
returns the line number where that string is in the file. If the string
is not in the file, it should return None.

Example:

which_line('file1.txt', 'hello world')  # 10
which_line('file1.txt', 'this is not in the file')  # None
'''

def which_line(filepath, a_string):
    with open(filepath) as fp:
        for index, line in enumerate(fp.readlines()):
            if line == a_string + "\n":
                return index + 1 
        return None 

# Test Cases

import tempfile

def test_string_not_present():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert which_line(fp.name, 'foobar') == None

    fp.close()

#

import tempfile

def test_string_present():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert which_line(fp.name, 'this is line 2') == 2
    
    fp.close()



'''
5) Count Lines Starting with each Letter

Write a function that receives the path to a text file that contains JUST ONE word
per line, and returns a dictionary with the counter of words starting with each
letter from 'a' to 'z'.

Example:

counter_by_letter('words.txt')  
# {
'a': 2,
'b': 10,
'c': 0,
...
'z': 1
}
'''

import string

def counter_by_letter(filepath):
    with open(filepath) as fp:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for word in fp.readlines():
            d[word[0]] += 1 
        return d 
       
'''
#alt jason solution
import string

def counter_by_letter(filepath):
    result = dict([(letter, 0) for letter in string.ascii_lowercase])
    with open(filepath) as fp:
        read_data = fp.readlines()
        for line in read_data:
            result[line[0]] += 1
return result
'''

# Test Cases

import tempfile

def test_first_letter_count():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('tree\n')
    fp.write('car\n')
    fp.write('car\n')
    fp.write('house\n')
    fp.flush()

    counter = counter_by_letter(fp.name)
    assert len(counter.keys()) == 26
    assert counter['c'] == 2
    assert counter['t'] == 1
    assert counter['h'] == 1
    assert counter['m'] == 0

    fp.close()



'''
6) Get Filename with Max Lines

Write a function that receives one or many file paths as parameters and returns
the name of the file with max amount of lines.

Example:

max_lines('file1.txt', 'file2.txt')  # 'file1.txt
max_lines('file1.txt')  # 'file1.txt
max_lines('file1.txt', 'file2.txt', 'file3.txt)  # 'file3.txt
'''

def max_lines(*file_names):
    max_len = 0
    max_file = ""
    for file_name in file_names:
        with open(file_name) as fp: 
            if len(fp.readlines()) > max_len:
                max_len = len(fp.readlines())
                max_file = file_name 
    return max_file

# Test Cases 

import tempfile

def test_one_file():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert max_lines(fp.name) == fp.name

    fp.close()

#

import tempfile

def test_two_files():
    fp1 = tempfile.NamedTemporaryFile(mode="w")
    fp1.write('this is line 1\n')
    fp1.write('this is line 2\n')
    fp1.write('this is line 3\n')
    fp1.flush()
    fp2 = tempfile.NamedTemporaryFile(mode="w")
    fp2.write('this is line 1\n')
    fp2.write('this is line 2\n')
    fp2.write('this is line 3\n')
    fp2.write('this is line 4\n')
    fp2.flush()

    assert max_lines(fp1.name, fp2.name) == fp2.name

    fp1.close()
    fp2.close()



'''
7) 
Write List of Strings into File

Write a function that receives a path to a text file as first parameter and
a list of string as second one. The function should write each string in a new
line of the text file. If 5 strings are given in the list, the resulting file
should have 5 lines.

Example:

write_lines('test-file.txt', ['hello', 'world'])
'''

def write_lines(filepath, list_of_strings):
    with open(filepath, 'a') as fp:
        for string in list_of_strings:
            fp.write(string + "\n")

# Test Cases 

import tempfile

def test_write_lines_to_file():
    fp = tempfile.NamedTemporaryFile(mode="w")
    write_lines((fp.name), ['my', 'name', 'is', 'john'])

    with open(fp.name) as fp:
        assert len(fp.readlines()) == 4
        fp.seek(0)
        assert fp.readlines()[2] == 'is\n'



'''
8) Write String to File Optional Overwrite

Write a function that receives a path to a text file as first parameter,
a string and an optional "ovewrite_all" boolean.
If overwrite_all is false, the function should
append the string at the end of current content in the text file.
If it's true, it should clean the content in the file and
write only given string.

There should always be a new line char at the end of the written line.
See test cases for more details.

Example:

write_string('test-file.txt', 'this is the string', overwrite_all=False)
'''

# Test Cases 

def write_string(filepath, a_string, overwrite_all=False):
    if not overwrite_all:
        with open(filepath, 'a') as fp: 
            fp.write(a_string + "\n")
    else: 
        with open(filepath, 'w') as fp:
            fp.write(a_string + "\n")

import tempfile

def test_write_string_with_overwrite():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()
    
    write_string(fp.name, 'my name is john', overwrite_all=True)

    with open(fp.name) as fp:
        assert len(fp.readlines()) == 1
        fp.seek(0)
        assert fp.readlines()[0] == 'my name is john\n'

#

import tempfile

def test_write_string_no_overwrite():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()
    
    write_string(fp.name, 'my name is john')

    with open(fp.name) as fp:
        assert len(fp.readlines()) == 4
        fp.seek(0)
        assert fp.readlines()[3] == 'my name is john\n'



'''
9) Copy Content from One File to Another

Write a function that receives a path to two text files as parameters and copies
the content of the first file into the second, overwriting the content of the second
file if it's not empty.

Example:

copy_file('test-file.txt', 'copy.txt')
'''

def copy_file(source_file, target_file):
    with open(source_file) as fp:
        file_content = fp.readlines()
        with open(target_file, 'w') as fp2:
            fp2.writelines(file_content)

# Test Cases 

import tempfile

def test_copy_file():
    fp1 = tempfile.NamedTemporaryFile(mode="w")
    fp1.write('this is line 1\n')
    fp1.write('this is line 2\n')
    fp1.write('this is line 3\n')
    fp1.flush()
    fp2 = tempfile.NamedTemporaryFile(mode="w")
    
    copy_file(fp1.name, fp2.name)

    fp1.close()

    with open(fp2.name) as fp2:
        assert len(fp2.readlines()) == 3
        fp2.seek(0)
        assert fp2.readlines()[2] == 'this is line 3\n'



'''
10) Sort Lines in Text File

Write a function that receives the path to a text file and sorts all the
lines in the file ascending or descending, depending on the 'sorting'
parameter.

Example:

sort_lines('file1.txt', sorting='asc')
sort_lines('file1.txt', sorting='desc')
'''

def sort_lines(filepath, sorting='asc'):
    with open(filepath) as fp:
        file_list = list(fp)
        if sorting == 'desc':
            file_list.sort(reverse = True)
        else: 
            file_list.sort()
    with open(filepath, 'w') as fp: 
        fp.writelines(file_list)

# Test Cases

import tempfile

def test_asc_order():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('line 3\n')
    fp.write('line 1\n')
    fp.write('line 2\n')
    fp.write('line 4\n')
    fp.flush()
    
    sort_lines(fp.name)

    with open(fp.name) as fp:
        assert fp.readlines()[0] == 'line 1\n'
        fp.seek(0)
        assert fp.readlines()[1] == 'line 2\n'

test desc order - Run Test

#

def test_desc_order():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('line 3\n')
    fp.write('line 1\n')
    fp.write('line 2\n')
    fp.write('line 4\n')
    fp.flush()
    
    sort_lines(fp.name, sorting='desc')

    with open(fp.name) as fp:
        assert fp.readlines()[0] == 'line 4\n'
        fp.seek(0)
        assert fp.readlines()[1] == 'line 3\n'

               
             
                
        
               
