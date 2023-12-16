import face_recognition as fr
import cv2
import os
import numpy as np 
import pandas as pd 
import time
import matplotlib.pyplot as plt


#-----------code----------------------------------------------------------------------------------
list=os.listdir('images')
student_image_list=[]#color loaded capimage list
students_names=[]

# students_encodedface=[]
for item in list:
    
    studentimage=fr.load_image_file(f"images\\{item}")
    studentimage=cv2.cvtColor(studentimage,cv2.COLOR_BGR2RGB )
    student_image_list.append(studentimage)
    
    students_names.append(os.path.splitext(item)[0])#returns  list of text and split text
def enco(images):
    students_encodedface=[] 
    for i in images:

        encodings=fr.face_encodings(i)[0]#we have to put index 0 to acces first element because it in [([])] encodings which in list in tupple(first index)in outer list, we need only list
        # print(encodings)
        students_encodedface.append(encodings)
    return students_encodedface
x=enco(student_image_list)#x is nothing but encoded list
# print(students_names)

df=pd.DataFrame({'ROLL_NO.':[r for r in range(len(students_names))],
                 'NAMES':[n for n in students_names],
                 'attendence':[None for _ in range(len(students_names))],#null values
                 'Time':[None for _ in range(len(students_names))]
                 })


capture=cv2.VideoCapture(0)
while True:
    ret,capimage=capture.read()
    
    capimage=cv2.cvtColor(capimage,cv2.COLOR_BGR2RGB )
    
    faceloc=fr.face_locations(capimage)
    
    encodingtest=fr.face_encodings(capimage,faceloc)#helps ecoding function to operate on facelocation
    
    for en,fa in zip(encodingtest,faceloc):
        match=fr.compare_faces(x,en)#comapare function matches current frame with each elements of lits of images we have and gives t on same index
        # print(match)
       
        if True in match:
           index_value=match.index(True)
        #    print(index_value)
           print(students_names[index_value])
           cv2.rectangle(capimage,(fa[3],fa[0]), (fa[1],fa[2]),(255,0,0),2)
           cv2.putText(capimage, str(students_names[index_value]), (fa[3]+6, fa[2]), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


           df.loc[index_value,'attendence']='Present'#update present at students location(student name list index is same as database index)
           if pd.isnull(df.loc[index_value, 'Time']):#if data is empty then it will update at specific location
              curr_time = time.strftime("%H:%M:%S", time.localtime())
              df.loc[index_value, 'Time'] = curr_time
           # print(faceloc)#contionously finding face location in tupple within list , if you mave your face out of camera it will return empty li
    cv2.imshow('h',capimage)
    if cv2.waitKey(1)==ord('a'):#wiaitkey will stop capture capimage for 1 sec ,adn while loop ensure frame is captured continously
        break#The key point 
cv2.destroyAllWindows
print(df)
df.to_csv('attendencelist.csv')#can save in any folder
present=(df['attendence']=='Present').sum()#sum calcuted in this case boolean values true or false
absent=len(students_names)-present
barl=plt.bar(['present','absent'],[present,absent],width=0.2,label=['present','absent'])
plt.bar_label(barl)
plt.title(f'{time.strftime("%d-%m-%Y",time.localtime())}')
plt.legend()
plt.show()










