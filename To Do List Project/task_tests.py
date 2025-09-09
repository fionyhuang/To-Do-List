
from task_functions import*

assert get_written_date(["01", "02", "2022"]) == 'January 2, 2022'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'
assert get_written_date(["04", "10", "1756"]) == "April 10, 1756"

assert is_valid_priority("5", {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}) == True
assert is_valid_priority("11", {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}) == False

assert delete_item([], 1, 1) == 0
assert delete_item([1], '-2') == -1
assert delete_item([1, 2, 3], '2') == 3

assert is_valid_month(["01", "01", "1970"]) == True
assert is_valid_month(["12", "31", "2021"]) == True
assert is_valid_day(["02", "03", "2000"]) == True
assert is_valid_day(["12", "31", "2021"]) == True
assert is_valid_year(["10", "15", "2022"]) == True
assert is_valid_year(["12", "31", "2021"]) == True
assert is_valid_month(["21", "01", "1970"]) == False

assert is_valid_month(["-2", "31", "2021"]) == False
assert is_valid_month(["March", "31", "2021"]) == False
assert is_valid_day(["02", "33", "2000"]) == False
assert is_valid_day(["02", "31", "2021"]) == False
assert is_valid_day(["02", "1st", "2021"]) == False
assert is_valid_day(["14", "1st", "2021"]) == False
assert is_valid_year(["10", "15", "22"]) == False
assert is_valid_year(["12", "31", "-21"]) == False


assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('2', ["Quizzes", 25.5], 1) == True

prio = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}
sample_task_list = ['Book tickets', 'Verify dates', '3', '05/05/2022', 'no']
sample_task_list1 = ['Book tickets', 'Verify dates', '3', '05/05/2022']
expected_result = {'name': 'Book tickets', 'info': 'Verify dates', 'priority': 3, 'duedate': '05/05/2022', 'done': 'no'}
assert get_new_task(sample_task_list , prio) == expected_result
assert get_new_task(sample_task_list1 , prio) == 4
new_task = [{
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
    }]

expected_res = {
        "name": "hip",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    }


assert update_task(new_task, "0",  prio, "name", "hip") == expected_res
assert update_task(new_task, "1000",  prio, "name", "hp") == -1


assert save_tasks_to_csv(new_task, "hello") == -1
assert save_tasks_to_csv(new_task, "hello.csv") == None


assert load_tasks_from_csv('missing-date.csv', new_task, prio) == [1]
assert load_tasks_from_csv('missing-date', new_task,prio) == -1

assert is_valid_date("03/05/2002") == True
assert is_valid_date("13/05/2002") == False

assert is_valid_name("d") == False
assert is_valid_name("dad") == True
assert is_valid_name("dadsfjaodshfoasdhfoahdfoahsdofhaodhfoadhfoiahd") == False

assert is_valid_completion("yes") == True
assert is_valid_completion("ye") == False
assert is_valid_completion("no") == True
