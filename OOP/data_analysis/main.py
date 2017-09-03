from datahandler import *

#전체 학년 평균 : 50점

dh = DataHandler('class_1.xlsx', '2-3')
#dh = DataHandler('class_1.dat', '2-3')

dh.GetEvaluation(50)

print("the lowest score : ({} = {})".format(
    dh.WhoIsLowest(), dh.GetLowestScore()))

print("the highest score : ({} = {})".format(
    dh.WhoIsHighest(), dh.GetHighestScore()))

