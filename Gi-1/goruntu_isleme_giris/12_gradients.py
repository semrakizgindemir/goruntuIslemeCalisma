#goruntu gradyanı goruntudeki yogunluk veya 
# renkteki yonlu bir değişikliktir.kenar algılamada kullanılır

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\sudoku.jpg" , 0)
plt.figure(),plt.imshow(img , cmap = "gray") ,plt.axis("off") ,plt.title("orijinal img"), plt.show()

#x gradyan 
sobelx = cv2.Sobel(img,ddepth=cv2.CV_16S ,dx=1 , dy=0 ,ksize=5)
plt.figure(),plt.imshow(sobelx , cmap = "gray") ,plt.axis("off") ,plt.title("sobelx img"),plt.show()

#y gradyan
sobely = cv2.Sobel(img,ddepth=cv2.CV_16S ,dx=0 , dy=1 ,ksize=5)
plt.figure(),plt.imshow(sobely , cmap = "gray") ,plt.axis("off") ,plt.title("sobely img"),plt.show()

#LAPLACE GRADİAN
laplacian =cv2.Laplacian(img , ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian , cmap = "gray") ,plt.axis("off") ,plt.title("laplacian img"),plt.show()

 




