day=int(raw_input("Enter a day:"))
month=int(raw_input("enter a month:"))
year=int(raw_input("Enter a year:"))
def generate(day,month,year):
    if((year%400==0 or year%4==0) and month==2):
        next_day=day+1
        next_month=month
        next_year=year
    elif(month==2 and day==28):
        next_day=1
        next_month=month+1
        next_year=year
    elif(month==12 and day==31):
        next_day=1
        next_month=1
        next_year=year+1
    elif(day==31 ):
        next_day=1
        next_month=month+1
        next_year=year
    elif((day==30) and (month==4 or month==6 or month==9 or month==11)):
        next_day=1
        next_month=month+1
        next_year=year
    else:
        next_day=day+1
        next_month=month
        next_year=year
    print(next_day,"-",next_month,"-",next_year)

generate(day,month,year)

