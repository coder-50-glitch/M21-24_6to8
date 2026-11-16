import cv2
import matplotlib.pyplot as plt
#import numpy as np
img=cv2.imread(r'C:\Users\sayak\Desktop\child.jpg')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
cv2.imwrite(r'C:\Users\sayak\Desktop\child11111.jpg',img)
plt.title("Child")
plt.axis("off")
plt.show()