start =input("from: ")
end =input("to: ")
gender= input("gender : ")
fare=0
stations={'potheri':0,'guduvancheri':1,'urapakam':2,'vandalur':3,'tambaram':4,'airport':5}
sv=stations.get(start)
ev=stations.get(end)
if sv > ev:
    dis= sv-ev
else:
    dis= ev-sv
fare=dis*5
if gender== 'm':
    age= int(input("age : "))
    if age<7:
        discount=fare*5/100
        fare=fare-discount
elif gender=='f':
    fare=0
print("ticket")
print(f"start :{start}")
print(f"end :{end}")
print(f"fare: {fare} rupees")