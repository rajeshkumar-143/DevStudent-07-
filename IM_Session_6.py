user = input("Enter your name = ")
Maths = int(input("Enter your Maths marks = "))
Science = int(input("Enter your Science marks = "))
English = int(input("Enter your English marks = "))    
Total_marks = Maths+Science+English    
Average = Total_marks//3  
print(Average)                                 
if (Maths<0 or Maths>100 or Science<0 or Science>100 or English<0 or English>100)  :
    print("Invalid marks") 
else :
    Average = Total_marks/3 
    print(f"Student name = {user }")
    print(f"Total marks = {Total_marks}")
    print("Persentage: {:.2f}".format(Average))
    if  Maths >= 40 and Science >= 40 and English >= 40 :
          print("Status: Pass")
          if Average >= 70:
                print("Grade A")
          elif Average >=60 :
                print("Grade B")
          elif Average >= 40 :
                print("Grade C")
          else :
                print("Status: Fail")
    else :
          print("Fail")