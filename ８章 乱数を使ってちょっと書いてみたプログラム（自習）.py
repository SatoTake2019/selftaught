import random
import statistics

meanvs = []
nums = []

for n in range(0, 5):
    for j in range(0, 5):
            for i in range(0, 10):
                nums.append(random.random())
                meanvs.append(statistics.mean(nums))
print(meanvs)

# 中心極限定理を視覚化してみたかったが、
# Pythonについて、まだ全然知識が足りないので、
# グラフィックとかいろいろ知識が付いたら、また弄ってみようと思う。
# 2019 6/21



    

    
