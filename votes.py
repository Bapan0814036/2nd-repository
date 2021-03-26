import operator
votes=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
votecounter=dict()
for i in votes:
   vote=votecounter.get(i,0)+1
   votecounter[i]=vote
print(votecounter)
n=max(votecounter.items(),key=operator.itemgetter(1))
print(n[0])
