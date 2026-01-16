import cv2
import numpy as np

# 讀取您的原圖 (假設檔名為 card.jpg)
img = cv2.imread('C:/222.jpeg')
h, w = img.shape[:2]

# 1. 在四個角落畫上黑色的定位點 (20x20像素)
size = 20
cv2.rectangle(img, (0, 0), (size, size), (0, 0, 0), -1)          # 左上
cv2.rectangle(img, (w-size, 0), (w, size), (0, 0, 0), -1)       # 右上
cv2.rectangle(img, (0, h-size), (size, h), (0, 0, 0), -1)       # 左下
cv2.rectangle(img, (w-size, h-size), (w, h), (0, 0, 0), -1)    # 右下

# 2. 模擬加上左側同步碼 (對齊 1-40 題的位置)
# 此部分座標需視您的實際欄位高度調整，範例為間隔顯示
for i in range(40):
    y_pos = 200 + (i * 20) # 假設起始於 200px，每題間隔 20px
    cv2.line(img, (5, y_pos), (25, y_pos), (0, 0, 0), 2)

# 3. 標註混合題區域 (方便裁切定位)
cv2.rectangle(img, (w//2 + 20, 100), (w-30, h-50), (0, 0, 0), 3)

# 儲存優化後的母片
cv2.imwrite('optimized_answer_card.jpg', img)
print("優化版答案卡母片已生成！")
