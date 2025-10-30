import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存 capture_imgにはqキーを押した際の画像が代入される
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = app.get_img()

    # 画像サイズを取得
    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape

    # 画像サイズを表示
    print(google_img.shape)
    print(capture_img.shape)

    # 走査
    for x in range(g_width):
        for y in range(g_height):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # 余りを求めることで格子状に配置
                google_img[y, x] = capture_img[y % c_height, x % c_width]
    
    # 結果を保存
    cv2.imwrite('output_images/lecture05_01_k24145.png', google_img)

