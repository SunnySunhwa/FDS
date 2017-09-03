from normal_dist import *
import openpyxl
from pickle import *

class DataHandler:
    #클래스 멤버 : 연산기 하나 
    evaluator = NormDist()
    
     #class method : 전역함수처럼 쓸 수 있다              
    @classmethod
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows
        
        for name, score in g:
            dic[name.value] = score.value

        return dic

    #openpyxl이 없으신 분들을 위한 파일 로드 함수
    @classmethod
    def get_data_from_file(cls, filename):
        raw_data = {}
        f = open(filename, 'rb')
        try:
            while True:
                data = load(f)
                raw_data.update(data)
        except EOFError:
            pass
        return raw_data
    
    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        #self.rawdata = DataHandler.get_data_from_file(filename)
        self.clsname = clsname 
        #연산한 값을 저장해두는 저장소
        #필요할 때 연산하되
        #이미 연산된 값이면 연산 없이 저장된 값을 반환
        self.cache = {}
        
    def GetScores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
        
        return self.cache.get('scores')
      
    def GetAverage(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(
                self.GetScores())
        
        return self.cache.get('average')

    def GetVariance(self):
        if "variance" not in self.cache:
            self.cache["variance"] = self.evaluator.variance(
                self.GetScores(), self.GetAverage())

        return self.cache.get("variance")

    def GetStandardDeviation(self):
        if "standard_deviation" not in self.cache:
            self.cache["standard_deviation"] = self.evaluator.std_dev(
                self.GetVariance())

        return self.cache.get("standard_deviation")
    
    def WhoIsHighest(self):
        if "highest" not in self.cache:
            self.cache['highest'] = reduce(lambda a, b:
                              a if self.rawdata.get(a) > self.rawdata.get(b) else b,
                            self.rawdata.keys())
            
        return self.cache.get("highest")
    
    def GetHighestScore(self):
        return self.rawdata[self.WhoIsHighest()]
    
    def WhoIsLowest(self):
        if "lowest" not in self.cache:
            self.cache['lowest'] = reduce(lambda a, b:
                                a if self.rawdata.get(a) < self.rawdata.get(b) else b,
                                         self.rawdata.keys())
            
        return self.cache.get('lowest')
    
    def GetLowestScore(self):
        return self.rawdata[self.WhoIsLowest()] 
    
    def GetEvaluation(self, total_avrg):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(
            self.clsname,
            self.GetAverage(),
            self.GetVariance(),
            self.GetStandardDeviation()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass(total_avrg)

    def evaluateClass(self, total_avrg):
        avrg = self.GetAverage()
        std_dev = self.GetStandardDeviation()
        
        if avrg <total_avrg and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > total_avrg and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < total_avrg and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > total_avrg and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
