from aip import AipFace
import numpy as np
import cv2
import base64

def Detection(image):
	global client  #声明client是全局的，即外面的那个client，因为我并没有传参

	imageType = "BASE64"

	''' call API without extra parameter '''
	return client.detect(image, imageType);

	''' call API with extra parameter(I comment them) '''
	'''
	options = {}
	options["face_field"] = "age"
	options["max_face_num"] = 2
	options["face_type"] = "LIVE"
	
	client.detect(image, imageType, options)
	'''


def GetPhoto():
	global cap

	ret, frame = cap.read() 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #设置输出为灰度图
 
	cv2.imwrite('photo.jpg', frame) 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		pass

	''' 关闭摄像头 '''
	cap.release() 
	cv2.destroyAllWindows()





def image_to_base64(photo):
 
    pic = cv2.imread(photo)
    image = cv2.imencode('.jpg',pic)[1]
    image_code = str(base64.b64encode(image))[2:-1]
 
    return image_code



if __name__ == '__main__':  #你可以把它看成C++里的int main(), 其实有些不同，想知道可以来问我

	'''    begin initializing API  '''
	APP_ID = '你的 App ID'
	API_KEY = '你的 Api Key'
	SECRET_KEY = '你的 Secret Key'

	''' 如果你忘记怎么弄这三个玩意儿了，可以问我，或者你不想问就用我的吧, 一天只有50次！！！ '''
	'''
	APP_ID = '15504734'
	API_KEY = 'XKMGcyfGbTvZKDmn8lykh2Zj'
	SECRET_KEY = 'bnCO1eWWKwX8LFGc4vHxRURRaWnDEV55'
	'''

	client = AipFace(APP_ID, API_KEY, SECRET_KEY)
	'''   end initializing   '''

	'''  initialize the camera  '''
	cap = cv2.VideoCapture(0) 
	''' end initial '''
	
	
	GetPhoto()
	photo = "photo.jpg" #此处填写截取下的图片路径
	image_code = image_to_base64(photo)
	result = Detection(image_code)

	#print(result)

	if result['error_msg'] == 'SUCCESS':
		print('face_num: ' + str(result['result']['face_num']))
	else:
		print('recognition error, please try again')