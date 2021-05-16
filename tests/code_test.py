import unittest

lists = [
    [],
    [1,2,3,4,5,6,7,8,9],
    [5,6,7],
    [1],
    [33333, 44444, 55555],
    ["a"],
    ["A", "B", "C", "D", "E", "F"],
    ["AB", "CD", "EF"],
    ["F", "E", "A", "G", "X", "D"],
    ["This", "Is", "A", "Test"],
    ["This is another ", "test"],
    ['d', 'w', 'a', 'r', 'v', 'e', 's'],
    [55.5],
    [55.5, 432.4442, 55.4, 2.56, 9894.3333],
    ["text", [1, 2,3], 5, 66.5],
    [(1,2,3), (5,4,3), (2,3,4), (2), (5,4)],
    [(4), (5), (7), (9)],
]

dicts = [
    {},
    {1:1},
    {1:1, 2:2, 3:3, 4:4 ,5:5, 6:6},
    {"1":"1", "2":"2", "3":"3", "4":"4"},
    {"This is a test": "This is test result", "String here":"String there"},
    {1:"1", 2:"2", 3:"3", 4:"4", 5:"5"},
    {(1,2,3):(1,2,3)},
    {55.5:99.3, 443.112:434.332}
]

strings = [
    "String test one",
    "string",
    "t",
    "",
    "55 522 04",
    "      ",
    "s o m e s t r i n g"
]


var_name = "a_val"

testcases = [{
        'question' : "split string {var_name} into a list",
        'data' : strings,
        'code' : "{var_name}.split()"
    },{
        'question' : "reverse the elements in list {var_name}",
        'data' : lists,
        'code' : "var_name.reverse()"
    },
    {
        'question' : "count the occurrences of items in {var_name}}",
        'data' : strings + lists + strings,
        'code' : "count({var_name})"
    },
    {
        'question' : " Get duplicate elements from list {var_name}",
        'data' : lists,
        'code' : "[{var_name}[i] for i in range(len({var_name})) if not i == {var_name}.index({var_name}[i])]"
    },
    {
        'question' : 'Generate a list containing consecutive numbers between 5 and 10',
        'data' : lists,
        'code' :  "[x for x in range(5, 11)]"
    },
    {
        'question' : "Get the element of list {var_name} at index 1",
        'data' : lists,
        'code' : "a_val[2]"
    },
    
    #Add filler word to end.
    #Change variable names
]


def runtest(testcase):
    question = testcase['question']
    data = testcase['data']
    code = testcase['code']
    for d in data:
        eval("{var_name} = {d}")
        res = eval(code)
        print(res)
    return

for ts in testcases:
    runtest(ts)
    break

# def t1():
#     ans = []
#     for data in testcases[0]['data']:
#         x = data
#         res = eval(testcases[0]['code'])
#         ans.append(res)
#     return ans


# class RunComparison(unittest.TestCase):
#     def testcase1(self):
#         truth = t1()
#         ans = []
#         for data in testcases[0]['data']:
#             ans.append(testcases[0]['question'].replace('a_val', data))

#         print(ans, truth)
