import unittest
import json

lists = [
    [],
    [1,2,3,4,5,6,7,8,9],
    [8,8,8],
    [5,6,7],
    [1],
    [33333, 44444, 55555],
    ["a"],
    ["A", "B", "C", "D", "E", "E"],
    ["AB", "CD", "EF"],
    ["F", "E", "A", "G", "X", "D"],
    ["This", "Is", "A", "Test"],
    ["This is another ", "test"],
    ["Test test test"],
    ['d', 'w', 'a', 'r', 'v', 'e', 's'],
    [55.5],
    [55.5, 432.4442, 55.4, 55.4, 9894.3333],
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
        'question' : f"split string {var_name} into a list",
        'data' : strings,
        'code' : f"{var_name}.split()",
        'inplace' : False
    },{
        'question' : f"reverse the elements in list {var_name} in place",
        'data' : lists,
        'code' : f"{var_name}.reverse()",
        'inplace' : True
    },
    {
        'question' : f"count the number of unique elements in {var_name}",
        'data' : lists + strings,
        'code' : f"len(set({var_name}))",
        'inplace' : False
    },
    {
        'question' : f"get duplicate elements from list {var_name}",
        'data' : lists,
        'code' : f"[{var_name}[i] for i in range(len({var_name})) if not i == {var_name}.index({var_name}[i])]",
        'inplace' : False
    },
    {
        'question' : f'generate a list containing consecutive numbers between 5 and 10',
        'data' : lists,
        'code' :  f"[x for x in range(5, 11)]",
        'inplace' : False
    },
    {
        'question' : f"Get the element of list {var_name} at index 1",
        'data' : lists,
        'code' : f"{var_name}[2]",
        'inplace' : False
    },
    
    #Add filler word to end.
    #Change variable names
]


def runtest(testcase):
    question = testcase['question']
    data = testcase['data']
    code = testcase['code']
    for d in data:
        out_val = json.dumps(d)
        exec(f"{var_name} = {out_val}")
        print(f"{var_name} = {out_val}")
        print(code)
        res = eval(code)
        if(testcase['inplace']):
            res = eval("{var_name}")
        print(res)
    return

for ts in testcases:
    runtest(ts)

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
