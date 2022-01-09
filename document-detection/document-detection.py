import cv2
from PIL import Image
import pytesseract as p

camera = cv2.VideoCapture(0)

cv2.namedWindow("capture-image")

counter = 0
i=0
text=""

while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to capture frame")
        break
    cv2.imshow("capture-image", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, captured images")
             
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "captured-image_{}.jpg".format(counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        counter += 1

camera.release()

cv2.destroyAllWindows()

print("writing text to txt files")
while i<counter:
            input_image = "captured-image_{}.jpg".format(i)
            img=Image.open(input_image)
            text+=p.image_to_string(img)
            print(text)
            
            print("complted round {}", i)
            i+=1

file1 = open("output_file.txt","w")
file1.write(text)
file1.close() 


file1 = open("output_file.txt","r+") 
  
print("Output of Read function is ")
print(file1.read())
 
# initializing test list
test_list = ['Analytics', 'Risk']
 
# using list comprehension
# checking if string contains list element
res = [ele for ele in test_list if(ele in text)]

print("Does string contain any list element : " + str(bool(res)))

print()
file1.close()