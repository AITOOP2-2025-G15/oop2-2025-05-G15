import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    app = MyVideoCapture()
    app.run()
    app.write_img()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('output_images/camera_capture.png') # MyVideoCapture.run()が保存する画像を読み込む

    # 画像が正しく読み込まれたか確認
    if google_img is None:
        print("Error: 'output_images/camera_capture.png' not found or could not be loaded.")
        return
    if capture_img is None:
        print("Error: 'output_images/camera_capture.png' not found or could not be loaded.")
        return

    g_hight, g_width, g_channel = google_img.shape 
    c_hight, c_width, c_channel = capture_img.shape 
    # 元のprint文
    print(google_img.shape)
    print(capture_img.shape)



    for y in range(g_hight):
        for x in range(g_width):
        # OpenCVはBGR順
         b, g, r = google_img[y, x] 

        # 白色 (255, 255, 255) かどうかを判定
        if (b, g, r) == (255, 255, 255):  
            google_img[y, x] = capture_img[y % c_hight, x % c_width]
        


    # 書き込み処理
    # 実装: 最終的な画像をファイルに保存
    cv2.imwrite('output_images/lecture05_01_k19117.png', google_img)

           