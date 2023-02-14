import re

isodates = r'(?P<year>[0-9]{4})[/-]?(?P<month>[0-9]{1,2})[/-]?(?P<day>[0-9]{1,2})((T|\s*)(?P<hour>[0-9]{1,2})\:(?P<minute>[0-9]{1,2})\:(?P<second>[0-9]{1,2})((?P<second_fract>\.[0-9]*))?(?P<timezone>Z|[+-])?)?'
usdates  = r"(?P<month>[0-9]{1,2})[/-]?(?P<day>[0-9]{1,2})[/-]?(?P<year>[0-9]{4})"

def matchdate( input_str ):
    for regex in [isodates, usdates]:
        matched = re.match(regex, input_str)
        if matched:
            return matched



def runtest( testCase, label=None ):
    input = testCase["input"]
    print(f"Performing Test{': '+label if label else ''}")
    
    result = matchdate( input )
    test_result = "PASS" if result else "FAIL"
    print("\tresult={}".format("matched" if result else "no match"))
    if "results" in testCase:
        print("\tresults=")
        for key in testCase["results"]:
            print(f"\t\t{key}\tPASS ({result.group(key)})" if str(testCase['results'][key]) == str(result.group(key)) else f"\t\t{key}\tFAIL ({testCase['results'][key]}, got {result.group(key)})")
            if (test_result == "PASS") and (str(testCase['results'][key]) != str(result.group(key))):
                test_result = "FAIL"
    return test_result


my_tests= [
            {'input': '1245/01/23', 
            'results': { 'year': 1245,
                        'month': '01',
                        'day': '23',},
            'name':"ISO"},

            {'input': '1245/1/23', 
            'results': { 'year': 1245,
                        'month': '01',
                        'day': '23',},
            'name':"ISO"},
            
            {'input': '1245/1/2', 
            'results': { 'year': 1245,
                        'month': '01',
                        'day': '02',},
            'name':"ISO"},

            
            {'input': '1245-1-2', 
            'results': { 'year': 1245,
                        'month': '01',
                        'day': '02',},
            'name':"ISO"},


            {'input': '1245-01-23', 
            'year': 1234},
            {'input': '12450123', 
            'year': 1234},
            {'input': '12450123T', 
            'year': 1234},
            {'input': '12450123', 
            'year': 1234},
            {'input': '12450123    ', 
            'year': 1234},
            {'input': '2023/02/13 00:44:40', 
            'year': None},
            {'input': '2023/02/13 00:44:40.1234567890', 
            'year': None},
            {'input': '12-23-1234    ', 
            'results': { 'year': 1234,
                        'month': '12',
                        'day': '23',},
            }
            ]




for count, testCase in enumerate(my_tests):
    label = testCase["name"] if "name" in testCase else f"Unnamed Test #{count + 1}"

    myresult = runtest(testCase, label)
    print(myresult)




















# import iso_8601


# month = date = year = hours = minutes = seconds = milliseconds = None
# y, m, d, h, m, s, ms
# J
# W
# E

#regex = r'([a-zA-z]*)\s+([0-9]*)\s+([0-9]*) ([0-9][0-9]):([0-9][0-9]):([0-9,\.]*)'


# regex_compiled = re.compile(regex)



    # input = testCase["input"]
    
    # print(f"Performing Test: {label}")
    # print(f"\tinput={input}")

    # result = runmatch( input, regex )
    # print("\tresult={}".format("matched" if result else "no match"))
    # if "results" in testCase:
    #     print("\tresults=")
    #     for key in testCase["results"]:
    #         # print(f"\t\t{key}")
    #         # print(f"\t\t{testCase['results'][key]} =? {result.group(key)}")
    #         print(f"\t\t{key}\tPASS ({result.group(key)})" if str(testCase['results'][key]) == str(result.group(key)) else f"\t\t{key}\tFAIL ({testCase['results'][key]}, got {result.group(key)})")
    # # break


# regex = r'(?P<month>[0-9]{1,2})[/-](?P<day>[0-9]{1,2})[/-](?P<year>[0-9]{4})'
# print(runmatch( '01/23/1234', regex ))


# print(regex_compiled.groupindex)


# print(.1234567890 * 1000000)
# print(.123456789 * 1000000)
# print(.12345678 * 1000000)
# print(.1234567 * 1000000)
# print(.123456 * 1000000)
# print(.12345 * 1000000)
# print(.1234 * 1000000)

# print(.123 * 1000000)

# print(.12 * 1000000)

# print(.1* 1000000)

# print(.05 * 1000000)
# print(.005 * 1000000)
# print(.0005 * 1000000)
# print(.00005 * 1000000)
# print(.000005 * 1000000)
# print(.0000005 * 1000000)
# print(.00000005 * 1000000)
# print(.000000005 * 1000000)

