import unittest

testcases = [{
    'question' : "split string \"a_val\" into a list",
    'data' : ["AB CD","AF ET", "This is a test", "d w a r v e s"],
    'code' : "x.split()"
}]


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