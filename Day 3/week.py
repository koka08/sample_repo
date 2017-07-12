week=["monday","tuesday","wednesday","thurday","friday","saturday","sunday"]
month=["january","febraury","march","april","may","june","july","august","september","october","november","december"]
st=str(raw_input("enter the string:").lower())
print(st)
if(st==week[0] or st==week[1] or st==week[2] or st==week[3] or st==week[4] or st==week[5] or st==week[6]):
	i=0
	while(True):
		if(st==week[i]):
			print(i+1)
			break
		i=i+1
else:
	i=0
	while(True):
		if(st==month[i]):
			print(i+1)
			break
		i=i+1
	
