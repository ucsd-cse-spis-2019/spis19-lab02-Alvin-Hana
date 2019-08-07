# wageCalculator.py
def convertWageMtoW(mWage):
   wageGap = 0.182
   ratio = 1-wageGap
   return mWage*ratio
print (convertWageMtoW(100))
print (convertWageMtoW(76.2))
print (convertWageMtoW(0))
