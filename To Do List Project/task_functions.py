# from operator import index
# from turtle import done
# from unicodedata import name
from asyncio import tasks
import csv
import os

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """ 
    print("==========================")
    print("What would you like to do?")
    # TODO: Loop-over the dictionary `menu`
    # to print the keys and options
    for x in menu:
        print(f'{x} - {menu.get(x)}')
    print("==========================")

def get_written_date(date_list):
    """ 
    The parameter is a list of strings in
    the formate of [MM, DD, YYYY] and returns 
    the date as a string [month, day, year]. The function should
    return None if the input is invalid and
    if the input is not a list or if the input list
    is empty or does not contain 3 string elements.
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]

    date = ""
    new_month = int(month)
    date = date + str(month_names.get(new_month))
    
    date = date + " " + str(int(day)) + ", " + str(int(year))
    return date

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_task(task, priority_map, name_only = False):
    """
    param: task (dict) - a dictionary object that is expected
            to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
    - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
            (displayed as a written-out date)
    - "done": a string representing whether a task is completed or not

    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed for the
            priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.

    returns: None; only prints the task values

    Helper functions:
    - get_written_date() to display the 'duedate' field
    """
    if name_only is True:
        for x in task:
            if x == "name":
                print(task.get(x))
    else:
        for x in task:
            if x == "name":
                print(task.get(x))
            elif x == "info":
                if task.get(x) != "":
                    print(f'  * {task.get(x)}')
            elif x == "duedate":
                duedate1 = task.get(x)
                print(f'  * Due: {get_written_date(duedate1.split("/"))}  (Priority: {priority_map.get(int(task["priority"]))})')
            elif x == "done":
                print(f'  * Completed? {task.get(x)}')
                
def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*42)
    for task in task_list: # go through all tasks in the list
        if show_idx: # if the index of the task needs to be displayed
            print(f"{task_list.index(task)+start_idx}.", end=" ")
        if completed == "all":
            print_task(task, priority_map, name_only)
        elif task.get("done") == completed:
            print_task(task, priority_map, name_only)

def is_valid_month(date_list):
    """
    The parameter is a list of strings [MM, DD, YYYY] format 
    and returns True if the provided month number is a possible 
    month in the U.S. the integer for month should be between 
    1 and 12.
    """
    if len(date_list) == 3:
        if type(date_list[0]) != str:
            return False
        if date_list[0].isdigit():
            if int(date_list[0]) >= 1 and int(date_list[0]) <= 12:
                return True
    return False
    
def is_valid_day(date_list):
    """
    The parameteris a list of strings in 
    the [MM, DD, YYYY] and returns True 
    if the provided day is a possible day 
    for the given month
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if is_valid_month(date_list):
        if date_list[1].isdigit():
            if int(date_list[1]) >= 1 and int(date_list[1]) <= num_days.get(int(date_list[0])):
                return True
    return False
            
def is_valid_year(date_list):
    """
    The parameter is a list of strings in the 
    [MM, DD, YYYY] format and returns True if the provided
    year is a possible year: a positive integer.
    """
    if len(date_list) == 3:
        if type(date_list[2]) != str:
            return False
        if date_list[2].isdigit():
            if int(date_list[2]) > 1000:
                return True
    return False

def is_valid_date(date_list):
    """
    Takes the input string in the format of MM/DD/YYYY
    and valid is_valid_month, is_valid_day, and is_valid_year
    """
    new_date_list = date_list.split("/")
    if is_valid_month(new_date_list) == False or is_valid_day(new_date_list) == False or is_valid_year(new_date_list) == False:
        return False
    return True

def is_valid_name(name):
    """
    Takes the input string that is supposed to
    contain between 3 and 25 characters returns a 
    Boolean True if the text is of the valid length;
    False, otherwise
    """
    if len(name) >= 3 and len(name) <= 25 :
        return True
    else:
        return False
    
def is_valid_priority(priority_value, priority_scale):
    """
    A string that is expected to contain an integer priority value 
    (uses str.isdigit()); gets validated against the keys in the dictionary, 
    provided as the second parameter.
    A dictionary that contains the mapping between the integer priority value
     (key) to its representation (e.g., key 1 might map to the priority value 
     "Highest" or "Lowest")
    Returns a Boolean True if the text contains an integer value that maps 
    to a key in the provided dictionary; False, otherwise
    """
    if priority_value.isdigit() == True:
        if int(priority_value) in priority_scale:
            return True
    return False  

def is_valid_completion(done):
    """
    Takes the input string that is expected to contain a text "yes" or "no"
    and returns a Boolean True if it's a text with the valid value; 
    False, otherwise
    """
    if done == 'yes' or done == 'no':
        return True
    else:
        return False
        
def get_new_task(task_list, task_dict):
    """
    First parameter to be a list with 5 strings. 
    If the size of the list is not correct, then the function returns the 
    integer size of the provided list. Calling get_new_task() with an empty 
    list as its first argument should return 0 .
    If any of the elements on the list are not of type string,
    the get_new_task() returns a tuple with ("type", <value>), where the <value> 
    is substituted with the first corresponding value from the list that was not a string.
    Each validation function will also be in charge of validating that its input parameter 
    (the item from the list) is of the correct type (just in case it is called separately).
    If the size of the list is correct, the function calls the helper functions to  
    validate the fields.
    If the validation succeeds, returns a new dictionary with the task keys set to
    the provided parameters (stripped of whitespace and converted to the proper type, if necessary).
    If any of the validation functions fail, return a tuple with the name of the parameter and the 
    corresponding value/parameter that caused it to fail.

    """
    new_dict = {}
    if len(task_list) != 5:
        return len(task_list)
    for task in task_list:
        if type(task) != str:
            return "type", task
    else:
        if is_valid_name(task_list[0]) == False:
            return "name", task_list[0]
        else:
            new_dict["name"] = task_list[0]
        new_dict["info"] = task_list[1] 
        if is_valid_priority(task_list[2],task_dict) == False:
            return "priority", task_list[2]
        else:
            new_dict["priority"] = int(task_list[2])
        # new_date_list = task_list[3].split('/')
        # if is_valid_month(new_date_list) == False or is_valid_day(new_date_list) == False or is_valid_year(new_date_list) == False:
        if is_valid_date(task_list[3]) is False:
            return "duedate", task_list[3]
        else:
            new_dict["duedate"] = task_list[3]
        if is_valid_completion(task_list[4]) == False:
            return 'done', task_list[4]
        else:
            # if task_list[4] == 'yes':
            #     task_list[4] == True
            # elif task_list[4] == 'no':
            #     task_list[4] == False
            new_dict['done'] = task_list[4]
    return new_dict
        
def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an 
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    
    if idx.isdigit() == False:
        return False
    if int(idx) < start_idx:
        return False
    if int(idx) - start_idx >= len(in_list):
        return False
    return True

def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    if (len(info_list) == 0):
        return 0
    if is_valid_index(idx, info_list, start_idx) == False:
        return -1
    for x in info_list:
        if field_key not in x:
            return -2
    new_idx = int(idx) - start_idx
    if field_key == 'name':
        if is_valid_name(field_info) == False:
            return field_key
        else:
            info_list[new_idx][field_key] = field_info
    elif field_key == 'info':
        info_list[new_idx][field_key] = field_info
    elif field_key == 'priority':
        if is_valid_priority(field_info, priority_map) == False:
            return field_key
        else:
            info_list[new_idx][field_key] = int(field_info)
    elif field_key == 'duedate':
        # new_date = field_info.split('/')
        # if is_valid_month(new_date) == False or is_valid_day(new_date) == False or is_valid_year(new_date) == False:
        if is_valid_date(field_info) is False:
            return field_key
        else:
            info_list[new_idx][field_key] = field_info
    elif field_key == 'done':
        if is_valid_completion(field_info) == False:
            return field_key
        else: 
            info_list[new_idx][field_key] = field_info
    return info_list[new_idx]
    
def delete_item(in_list, idx, start_idx = 0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.

    returns:
    If the input list is empty, return 0.
    If idx is not of type string or start_idx is not an int, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.

    Helper functions:
    - is_valid_index()
    """
    if len(in_list) == 0:
        return 0
    if type(idx) != str or type(start_idx) != int:
        return None
    if is_valid_index(idx, in_list, start_idx) == False:
        return -1
    new_idx = int(idx) - start_idx
    deleted_element = in_list[new_idx]
    in_list.remove(in_list[new_idx])
    return deleted_element

def load_tasks_from_csv(filename, in_list, priority_map):
    """
    param: filename (str) - A string variable that represents the
            name of the file from which to read the contents.
    param: in_list (list) - A list of task dictionary objects to which
            the tasks read from the provided filename is appended.
            If in_list is not empty, the existing tasks are not dropped.
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed by the helper function.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in "read" mode. For each row in the csv file, the function will
    proceed to create a new task using the `get_new_task()` function.
    - If the function `get_new_task()` returns a valid task object,
    it gets appended to the end of the `in_list`.
    - If the `get_new_task()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid task data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_task().

    Helper functions:
    - get_new_task()
    """
    
    if filename[-4:] != ".csv":
        return -1
    if os.path.exists(filename) is False:
        return None
    with open(filename, 'r') as file:
        error_list = []
        temp = csv.reader(file)
        for ind, row in enumerate(temp):
            if type(get_new_task(row, priority_map)) == dict:
                in_list.append(get_new_task(row, priority_map))
            elif type(get_new_task(row, priority_map)) != dict:
                error_list.append(ind + 1)
    file.close()
    return error_list

def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    if filename[-4:] != ".csv":
        return -1 
    with open(filename, 'w', newline='') as file:
        task_writer = csv.writer(file)
        for current_dict in tasks_list:
            task_data = []
            for values in current_dict.values():
                task_data.append(values)
            task_writer.writerow(task_data)
    return None

