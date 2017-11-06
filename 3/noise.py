import sys
import cv2
import numpy as np

def Add_salt_pepper_Noise(srcArr, pa, pb):
	amount1 = srcArr.shape[0] * srcArr.shape[1] * pa
	amount2 = srcArr.shape[0] * srcArr.shape[1] * pb
	
	counter = 0
	for counter in range(0, int(amount1)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 0

	for counter in range(0, int(amount2)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 255

def Add_gaussian_Noise(srcArr, mean, sigma):
    NoiseArr = srcArr.copy()
    cv2.randn(NoiseArr, mean, sigma)
    cv2.add(srcArr, NoiseArr, srcArr)

def main():
	
	image = cv2.imread(sys.argv[1])
	
	meanVals = [0, 5, 10, 20]	
	sigmaVals = [0, 20, 50, 100]
	kernelVals = [3, 5, 7]
	paVals = [0.01, 0.03, 0.05, 0.4]
	pbVals = [0.01, 0.03, 0.05, 0.4]
	dir = "Results/"
	for kernel in kernelVals:
		for mean in meanVals:
			for sigma in sigmaVals:
				noise_img = image.copy() 
				Add_gaussian_Noise(noise_img, mean, sigma)
				cv2.imwrite(dir+"GaussNoise"+"-M"+str(mean)+"-S"+str(sigma)+".png",noise_img)

				noise_dst = noise_img.copy()
				cv2.blur(noise_dst, (kernel,kernel))
				cv2.imwrite(dir+"BoxFilter"+"-M"+str(mean)+"-S"+str(sigma)+"-K"+str(kernel)+".png",noise_dst)

				noise_dst1 = noise_img.copy()
				cv2.GaussianBlur(noise_dst1, (kernel,kernel), 1.5)
				cv2.imwrite(dir+"GaussFilter"+"-M"+str(mean)+"-S"+str(sigma)+"-K"+str(kernel)+".png",noise_dst1)

				noise_dst2 = noise_img.copy()
				cv2.medianBlur(noise_dst2, kernel)
				cv2.imwrite(dir+"MedianFilter"+"-M"+str(mean)+"-S"+str(sigma)+"-K"+str(kernel)+".png",noise_dst2)

				
		for pa in paVals:
			for pb in pbVals:
				noise_img2 = image.copy()
				Add_salt_pepper_Noise(noise_img2, pa, pb)
				cv2.imwrite(dir+"SnPNoise"+"-pa"+str(pa)+"-pb"+str(pb)+".png",noise_img2)

				noise_dst3 = noise_img2.copy()
				cv2.blur(noise_dst3, (kernel,kernel))
				cv2.imwrite(dir+"SnP_BoxFilter"+"-pa"+str(pa)+"-pb"+str(pb)+"-K"+str(kernel)+".png",noise_dst3)

				noise_dst4 = noise_img2.copy()
				cv2.GaussianBlur(noise_dst4, (kernel,kernel), 1.5)
				cv2.imwrite(dir+"SnP_GaussFilter"+"-pa"+str(pa)+"-pb"+str(pb)+"-K"+str(kernel)+".png",noise_dst4)				

				noise_dst5 = noise_img2.copy()
				cv2.medianBlur(noise_dst5, kernel)
				cv2.imwrite(dir+"SnP_MedianFilter"+"-pa"+str(pa)+"-pb"+str(pb)+"-K"+str(kernel)+".png",noise_dst5)	


	cv2.waitKey(0)
	
if __name__ == '__main__':
    main()