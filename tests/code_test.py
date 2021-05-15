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
    [(4), (5), (7)],
]


testcases = [{
        'question' : "split string \"a_val\" into a list",
        'data' : ["AB CD","AF ET", "This is a test", "d w a r v e s", "ef e eee'f"],
        'code' : "a_val.split()"
    },{
        'question' : "reverse list \"a_val\" ",
        'data' : ["[AB CD]","[AF ET]", "[This is a test]", "[d w a r v e s]"],
        'code' : "reversed(a_val)"
    },
    {
        'question' : "count the occurrences of items in \"a_val\" ",
        'data' : ["[AB CD]","[AF ET]", "[This is a test]", "[d w a r v e s]"],
        'code' : "count(a_val)"
    },
    {
        'question' : ""
    }
    #Generating a range.
    #Check if elem exists
    #Get duplicates from list.
    #iterate through dictionary "a_val"
    #Get nth element of list
    
    #Add filler word to end.
    #Change variable names
]



def t1():
    ans = []
    for data in testcases[0]['data']:
        x = data
        res = eval(testcases[0]['code'])
        ans.append(res)
    return ans


class TestAddFishToAquarium(unittest.TestCase):
    def testcase1(self):
        truth = t1()
        ans = []
        for data in testcases[0]['data']:
            ans.append(testcases[0]['question'].replace('a_val', data))

        print(ans, truth)

    # def test_add_fish_to_aquarium_exception(self):
    #     too_many_fish = ["shark"] * 25
    #     with self.assertRaises(ValueError) as exception_context:
    #         add_fish_to_aquarium(fish_list=too_many_fish)
    #     self.assertEqual(
    #         str(exception_context.exception),
    #         "A maximum of 10 fish can be added to the aquarium"
    #     )