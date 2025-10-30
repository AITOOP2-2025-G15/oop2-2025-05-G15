import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = resized_capture_img[y, x]

    # "implement me" 3:
    # 書き込み処理と表示
    cv2.imwrite('images/composite_image.png', google_img)
    print("合成画像を 'images/composite_image.png' に保存しました。")

    # 結果をウィンドウに表示
    cv2.imshow('Composite Result', google_img)
    print("キーを押すとウィンドウが閉じます。")
    cv2.waitKey(0) # 何かキーが押されるまで待機
    cv2.destroyAllWindows() # ウィンドウを閉じる

# スクリプトとして実行された場合のみlecture05_01を実行
if __name__ == "__main__":
    lecture05_01()
                #implement me

    # 書き込み処理
    # implement me

