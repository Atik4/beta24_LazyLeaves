import re
import string

def preprocess(test_string):
    #test_string = "I+wish+to+Travel+From%3A-+Mata+Mandir+Bhopal+To%3A-+Manit+Bhopal"

    test_string=test_string.replace("+"," ")
    test_string=test_string.replace("-"," ")

    print(test_string)

    for i in test_string:

        if i=="%":
            loc = test_string.index(i)
            test_string.replace(i," ")
            test_string = test_string.replace(test_string[loc+1], " ")
            test_string = test_string.replace(test_string[loc+2], " ")


    res = re.sub('['+string.punctuation+']', '', test_string).split()#

    resultant_string = " ".join(res)

    print(resultant_string)
    return resultant_string
