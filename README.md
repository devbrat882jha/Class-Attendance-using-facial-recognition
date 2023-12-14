# Class-Attendance-using-facial-recognition
Modules used-facial recognition,open CV, os,numpy,pandas,matplotlib

PROJECT  DESCRIPTION
<br>
This programme recognises any student whose image has been uploaded in image folder,the imagefile should be named after student.
<br>
Firstly os module make a list of all files saved in image folder,i have used only two images of public figures.Any number of images could be added in folder.
<br>
Then  have used for to iterate each image and load data,this data and appended to list.
<br>
It is must to convert the data into rgb form so that it could be processed by face recognition module.
<br>
I have made separate function to store encodings of images, encodings are set of measurements of facial features such as distance between eyes.It is these encodings with which COMPARE function do matching.
<br>
I have functions of cv2 to capture video frame by frame, this frame will be our image with which we will compare with encoding list.
<br>
I have used while loop so that function capture contniously until 'a' key pressed.
<br>
Whenver person is matched ,it returns boolean value True at same index as encoded list of student.For example encoded list of student [student A, studentB] if the frame is matched with student a the result list will be [true,false].
<br>
we can use this index to find out which student was matched.
<br>
This programme also create dataframe of of all students present in class and marked Present whenever student is matched .It also updates the time at which student was detetcted.
<br>
Finally, it plots graph of number of students present and absent against total students.



