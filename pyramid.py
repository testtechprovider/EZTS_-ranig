"""pyramids sum"""
pyramid=[[1],[2,1,2],[3,2,1,2,3],[4,3,2,1,2,3,4],[5,4,3,2,1,2,3,4,5]]
total=0
for row in pyramid:
    total +=sum(row)
print(total)