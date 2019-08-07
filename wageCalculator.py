# wageCalculator.py
# Takes in parameters for the male wage and a boolean for if the person is in Korea or not. Also hi Jaz!
def convertWageMtoW(mWage, korea):
   if korea:
      wageGap = 0.346
   else:
      wageGap = 0.182
   ratio = 1-wageGap
   return mWage*ratio
print (convertWageMtoW(100, True))
print (convertWageMtoW(76.2, False))
print (convertWageMtoW(0, True))
