#! /usr/bin/python3

startYear = int(input("année de depart: "))
endYear = int(input("année de fin: "))
y = (endYear-startYear)+1


for i in range(y):
	year = i+startYear
	YY=str(year)
	for m in range(13):
		month = m
		M=str(month)
		if(len(M) == 1):
			MM ="0"+M
		else :
			MM=M
		for d in range(32):
			day = d
			D=str(day)
			if(len(D) == 1):
				DD="0"+D
			else:
				DD=D
			date=YY+MM+DD	
			file=open("dateList.txt","a")
			file.write("\n"+date)
			file.close()	

			
			
