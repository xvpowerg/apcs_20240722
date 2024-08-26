from statistics import mean
score = [87,66,90,65,70]

scoreMax = score[0]
scoreMin = score[0]
for i in range(1,len(score)):
     if score[i] > scoreMax:
         scoreMax = score[i]        
     if score[i] < scoreMin:
         scoreMin = score[i]
print(scoreMax)
print(scoreMin)

print(sum(score))
print(max(score))
print(min(score))
print(mean(score))
print(sum(score)/len(score))
