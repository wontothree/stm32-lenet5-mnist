# import tkinter as tk
# from PIL import Image, ImageDraw
# import numpy as np
# from tensorflow.keras import models
# import matplotlib.pyplot as plt

# class DrawApp:
#     def __init__(self, canvas_size=280, grid_size=28):
#         self.canvas_size = canvas_size
#         self.grid_size = grid_size
#         self.pixel_size = canvas_size // grid_size

#         # Tkinter 기본 설정
#         self.root = tk.Tk()
#         self.root.title("숫자 입력 캔버스 (28x28 픽셀)")

#         # 캔버스 생성
#         self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
#         self.canvas.pack()

#         # PIL 이미지와 드로잉 객체 (백엔드)
#         self.image = Image.new("L", (canvas_size, canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#         # 이벤트 바인딩
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)

#         # 버튼
#         button_frame = tk.Frame(self.root)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="초기화", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)
#         tk.Button(button_frame, text="예측", command=self.extract_image).pack(side=tk.LEFT)

#         self.root.mainloop()

#     def paint(self, event):
#         # 붓의 크기 조정
#         brush_radius = 10
#         x1, y1 = (event.x - brush_radius), (event.y - brush_radius)
#         x2, y2 = (event.x + brush_radius), (event.y + brush_radius)

#         # Tkinter에 그리기
#         self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
#         # PIL 이미지에도 그림
#         self.draw.ellipse([x1, y1, x2, y2], fill=0)

#     def clear_canvas(self):
#         self.canvas.delete("all")
#         self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#     def extract_image(self):
#         # 이미지를 28x28로 리사이즈하고, 정규화 및 반전
#         resized = self.image.resize((self.grid_size, self.grid_size), Image.Resampling.LANCZOS)
#         img_array = np.asarray(resized).astype(np.float32) / 255.0
#         img_array = 1.0 - img_array  # 검정 = 1.0, 흰색 = 0.0
#         img_array = img_array.reshape((28, 28, 1))  # CNN 입력 형태

#         # 모델 로딩
#         model = models.load_model("lenet5_mnist.h5")

#         # 예측 수행
#         prediction = model.predict(img_array.reshape(1, 28, 28, 1))
#         predicted_label = np.argmax(prediction)

#         # 결과 출력
#         print(f"\n 예측 결과: {predicted_label}")
#         plt.imshow(img_array.reshape(28, 28), cmap='gray')
#         plt.title(f"예측: {predicted_label}")
#         plt.axis('off')
#         plt.show()

# # 실행
# if __name__ == "__main__":
#     DrawApp()



# import tkinter as tk
# from PIL import Image, ImageDraw
# import numpy as np
# from tensorflow.keras import models
# import matplotlib.pyplot as plt
# import scipy.ndimage

# class DrawApp:
#     def __init__(self, canvas_size=280, grid_size=28):
#         self.canvas_size = canvas_size
#         self.grid_size = grid_size
#         self.pixel_size = canvas_size // grid_size

#         # Tkinter 기본 설정
#         self.root = tk.Tk()
#         self.root.title("숫자 입력 캔버스 (28x28 픽셀)")

#         # 캔버스 생성
#         self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
#         self.canvas.pack()

#         # PIL 이미지와 드로잉 객체 (백엔드)
#         self.image = Image.new("L", (canvas_size, canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#         # 이벤트 바인딩
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)

#         # 버튼
#         button_frame = tk.Frame(self.root)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="초기화", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)
#         tk.Button(button_frame, text="예측", command=self.extract_and_predict).pack(side=tk.LEFT)

#         # 모델 로딩
#         self.model = models.load_model("lenet5_mnist.h5")
#         print("✅ LeNet-5 모델 로딩 완료!")

#         self.root.mainloop()

#     def paint(self, event):
#         brush_radius = 10
#         x1, y1 = (event.x - brush_radius), (event.y - brush_radius)
#         x2, y2 = (event.x + brush_radius), (event.y + brush_radius)

#         self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
#         self.draw.ellipse([x1, y1, x2, y2], fill=0)

#     def clear_canvas(self):
#         self.canvas.delete("all")
#         self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#     def extract_and_predict(self):
#         processed_img = self.preprocess_image(self.image)
#         prediction = self.model.predict(processed_img.reshape(1, 28, 28, 1), verbose=0)
#         predicted_label = int(np.argmax(prediction))

#         # 결과 출력
#         print(f"\n🎯 예측 결과: {predicted_label}")
#         plt.imshow(processed_img.reshape(28, 28), cmap='gray')
#         plt.title(f"예측: {predicted_label}")
#         plt.axis('off')
#         plt.show()

#     def preprocess_image(self, img_pil):
#         # 1. 리사이즈 (280x280 → 28x28)
#         resized = img_pil.resize((28, 28), Image.Resampling.LANCZOS)

#         # 2. 넘파이 배열로 변환 및 반전
#         img_array = np.asarray(resized).astype(np.float32)
#         img_array = 255.0 - img_array  # 흰 배경(255) → 0, 검정 글씨(0) → 255

#         # 3. 임계값 적용 (흐릿한 숫자 제거)
#         img_array[img_array < 100] = 0
#         img_array[img_array >= 100] = 255

#         # 4. 정규화
#         img_array = img_array / 255.0

#         # 5. 중심 정렬
#         img_array = self.center_image(img_array)

#         # 6. 채널 추가
#         img_array = img_array.reshape((28, 28, 1))

#         return img_array

#     def center_image(self, img):
#         cy, cx = scipy.ndimage.center_of_mass(img)
#         if np.isnan(cx) or np.isnan(cy):
#             return img  # 아무것도 안 그린 경우
#         shift_y = int(img.shape[0] // 2 - cy)
#         shift_x = int(img.shape[1] // 2 - cx)
#         shifted_img = scipy.ndimage.shift(img, shift=[shift_y, shift_x], mode='constant', cval=0.0)
#         return shifted_img

# # 실행
# if __name__ == "__main__":
#     DrawApp()


# center of mass
# import tkinter as tk
# from PIL import Image, ImageDraw, ImageFilter
# import numpy as np
# from tensorflow.keras import models
# import matplotlib.pyplot as plt
# import scipy.ndimage


# class DrawApp:
#     def __init__(self, canvas_size=280, grid_size=28):
#         self.canvas_size = canvas_size
#         self.grid_size = grid_size

#         # Tkinter 기본 설정
#         self.root = tk.Tk()
#         self.root.title("숫자 입력 캔버스 (28x28 픽셀)")

#         # 캔버스 생성
#         self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
#         self.canvas.pack()

#         # PIL 이미지 생성
#         self.image = Image.new("L", (canvas_size, canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#         # 이벤트 바인딩
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)

#         # 버튼
#         button_frame = tk.Frame(self.root)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="초기화", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)
#         tk.Button(button_frame, text="예측", command=self.extract_and_predict).pack(side=tk.LEFT)

#         # 모델 로딩
#         self.model = models.load_model("lenet5_mnist.h5")
#         print("✅ LeNet-5 모델 로딩 완료!")

#         self.root.mainloop()

#     def paint(self, event):
#         brush_radius = 10
#         x1, y1 = (event.x - brush_radius), (event.y - brush_radius)
#         x2, y2 = (event.x + brush_radius), (event.y + brush_radius)

#         self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
#         self.draw.ellipse([x1, y1, x2, y2], fill=0)

#     def clear_canvas(self):
#         self.canvas.delete("all")
#         self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=255)
#         self.draw = ImageDraw.Draw(self.image)

#     def extract_and_predict(self):
#         processed_img = self.preprocess_image(self.image)
#         prediction = self.model.predict(processed_img.reshape(1, 28, 28, 1), verbose=0)
#         predicted_label = int(np.argmax(prediction))
#         confidence = float(np.max(prediction))

#         # 시각화
#         plt.imshow(processed_img.reshape(28, 28), cmap='gray')
#         plt.title(f"예측: {predicted_label} (신뢰도: {confidence:.2f})")
#         plt.axis('off')
#         plt.show()

#         # 콘솔 출력
#         if confidence < 0.5:
#             print(f"🤔 예측 신뢰도가 낮습니다. ({confidence:.2f}) 다시 입력해 보세요!")
#         else:
#             print(f"🎯 예측 결과: {predicted_label} (신뢰도: {confidence:.2f})")

#     def preprocess_image(self, img_pil):
#         # 1. Blur로 노이즈 제거
#         blurred = img_pil.filter(ImageFilter.GaussianBlur(radius=1))

#         # 2. 28x28로 리사이즈
#         resized = blurred.resize((28, 28), Image.Resampling.LANCZOS)
#         img_array = np.asarray(resized).astype(np.float32)

#         # 3. 반전: 검정 → 255, 흰색 → 0
#         img_array = 255.0 - img_array

#         # 4. Thresholding
#         img_array[img_array < 80] = 0
#         img_array[img_array >= 80] = 255

#         # 5. 정규화
#         img_array = img_array / 255.0

#         # 6. 중심 정렬
#         img_array = self.center_image(img_array)

#         # 7. 숫자 자동 확대 + padding
#         img_array = self.crop_and_resize(img_array)

#         # 8. 채널 추가
#         img_array = img_array.reshape((28, 28, 1))

#         return img_array

#     def center_image(self, img):
#         cy, cx = scipy.ndimage.center_of_mass(img)
#         if np.isnan(cx) or np.isnan(cy):
#             return img  # 아무 것도 안 그린 경우
#         shift_y = int(img.shape[0] // 2 - cy)
#         shift_x = int(img.shape[1] // 2 - cx)
#         return scipy.ndimage.shift(img, shift=[shift_y, shift_x], mode='constant', cval=0.0)

#     def crop_and_resize(self, img_array, target_size=28):
#         coords = np.argwhere(img_array > 0)
#         if coords.shape[0] == 0:
#             return img_array  # 아무것도 안 그린 경우

#         y0, x0 = coords.min(axis=0)
#         y1, x1 = coords.max(axis=0) + 1

#         cropped = img_array[y0:y1, x0:x1]

#         # 정사각형 패딩
#         h, w = cropped.shape
#         side = max(h, w)
#         padded = np.zeros((side, side), dtype=np.float32)
#         padded[(side - h)//2:(side - h)//2 + h, (side - w)//2:(side - w)//2 + w] = cropped

#         # 리사이즈
#         resized = Image.fromarray((padded * 255).astype(np.uint8))
#         resized = resized.resize((target_size, target_size), Image.Resampling.LANCZOS)
#         return np.asarray(resized).astype(np.float32) / 255.0


# # 실행
# if __name__ == "__main__":
#     DrawApp()


import tkinter as tk
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from tensorflow.keras import models
import matplotlib.pyplot as plt


class DrawApp:
    def __init__(self, canvas_size=280, grid_size=28):
        self.canvas_size = canvas_size
        self.grid_size = grid_size

        # Tkinter 기본 설정
        self.root = tk.Tk()
        self.root.title("숫자 입력 캔버스 (28x28 픽셀)")

        # 캔버스 생성
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
        self.canvas.pack()

        # PIL 이미지 생성
        self.image = Image.new("L", (canvas_size, canvas_size), color=255)
        self.draw = ImageDraw.Draw(self.image)

        # 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

        # 버튼
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="초기화", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="예측", command=self.extract_and_predict).pack(side=tk.LEFT)

        # 모델 로딩
        self.model = models.load_model("lenet5_mnist.h5")
        print("✅ LeNet-5 모델 로딩 완료!")

        self.root.mainloop()

    def paint(self, event):
        brush_radius = 10
        x1, y1 = (event.x - brush_radius), (event.y - brush_radius)
        x2, y2 = (event.x + brush_radius), (event.y + brush_radius)

        self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
        self.draw.ellipse([x1, y1, x2, y2], fill=0)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=255)
        self.draw = ImageDraw.Draw(self.image)

    def extract_and_predict(self):
        processed_img = self.preprocess_image(self.image)
        prediction = self.model.predict(processed_img.reshape(1, 28, 28, 1), verbose=0)
        predicted_label = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        # 시각화
        plt.imshow(processed_img.reshape(28, 28), cmap='gray')
        plt.title(f"예측: {predicted_label} (신뢰도: {confidence:.2f})")
        plt.axis('off')
        plt.show()

        # 콘솔 출력
        if confidence < 0.5:
            print(f"🤔 예측 신뢰도가 낮습니다. ({confidence:.2f}) 다시 입력해 보세요!")
        else:
            print(f"🎯 예측 결과: {predicted_label} (신뢰도: {confidence:.2f})")

    def preprocess_image(self, img_pil):
        # 1. Blur로 노이즈 제거
        blurred = img_pil.filter(ImageFilter.GaussianBlur(radius=1))

        # 2. 28x28로 리사이즈
        resized = blurred.resize((28, 28), Image.Resampling.LANCZOS)
        img_array = np.asarray(resized).astype(np.float32)

        # 3. 반전: 검정 → 255, 흰색 → 0
        img_array = 255.0 - img_array

        # 4. Thresholding
        img_array[img_array < 80] = 0
        img_array[img_array >= 80] = 255

        # 5. 정규화
        img_array = img_array / 255.0

        # 6. Bounding Box 중심 정렬
        img_array = self.center_image_bbox(img_array)

        # 7. 채널 추가
        img_array = img_array.reshape((28, 28, 1))

        return img_array

    def center_image_bbox(self, img):
        coords = np.argwhere(img > 0)
        if coords.size == 0:
            return img  # 아무것도 안 그린 경우

        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0) + 1
        cropped = img[y0:y1, x0:x1]

        h, w = cropped.shape
        side = max(h, w)

        # 정사각형 패딩
        square = np.zeros((side, side), dtype=np.float32)
        square[(side - h)//2:(side - h)//2 + h, (side - w)//2:(side - w)//2 + w] = cropped

        # 중앙 배치
        padded = np.zeros((28, 28), dtype=np.float32)
        offset_y = (28 - side) // 2
        offset_x = (28 - side) // 2
        padded[offset_y:offset_y + side, offset_x:offset_x + side] = square

        return padded


# 실행
if __name__ == "__main__":
    DrawApp()
