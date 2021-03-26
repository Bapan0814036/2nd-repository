votes=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
votecounter={}
for i in votes:
   if i in votecounter:
      votecounter[i]=votecounter.get(i,0)+1
   else:
      votecounter[i]=1
print(votecounter)