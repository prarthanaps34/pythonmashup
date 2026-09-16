attendance=[18,20,19,15,21];
full_days= 0;
total_attendance=0;
for x in attendance:
    if x >=20:
        print(x,"full")
        full_days +=1
    else:
        print(x,"not full")
        
    total_attendance += x
print(full_days,"-full days attendance");
print(total_attendance,"-total attendance");