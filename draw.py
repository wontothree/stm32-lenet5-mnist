import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from tensorflow.keras import models
import matplotlib.pyplot as plt

class DrawApp:
    def __init__(self, canvas_size=280, grid_size=28):  # ▶️ 픽셀 10x10으로 키운 버전
        self.canvas_size = canvas_size
        self.grid_size = grid_size
        self.pixel_size = canvas_size // grid_size

        # Tkinter 기본 설정
        self.root = tk.Tk()
        self.root.title("✍️ 숫자 입력 캔버스 (28x28 픽셀)")

        # 캔버스 생성
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
        self.canvas.pack()

        # PIL 이미지와 드로잉 객체 (백엔드)
        self.image = Image.new("L", (canvas_size, canvas_size), color=255)
        self.draw = ImageDraw.Draw(self.image)

        # 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

        # 버튼
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="🧼 초기화", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="🤖 예측", command=self.extract_image).pack(side=tk.LEFT)

        self.root.mainloop()

    def paint(self, event):
        # 붓의 크기 조정
        brush_radius = 6
        x1, y1 = (event.x - brush_radius), (event.y - brush_radius)
        x2, y2 = (event.x + brush_radius), (event.y + brush_radius)

        # Tkinter에 그리기
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
        # PIL 이미지에도 그림
        self.draw.ellipse([x1, y1, x2, y2], fill=0)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=255)
        self.draw = ImageDraw.Draw(self.image)

    def extract_image(self):
        # 이미지를 28x28로 리사이즈하고, 정규화 및 반전
        resized = self.image.resize((self.grid_size, self.grid_size), Image.Resampling.LANCZOS)
        img_array = np.asarray(resized).astype(np.float32) / 255.0
        img_array = 1.0 - img_array  # 검정 = 1.0, 흰색 = 0.0
        img_array = img_array.reshape((28, 28, 1))  # CNN 입력 형태

        # 모델 로딩
        model = models.load_model("lenet_mnist.h5")

        # 예측 수행
        prediction = model.predict(img_array.reshape(1, 28, 28, 1))
        predicted_label = np.argmax(prediction)

        # 결과 출력
        print(f"\n✅ 예측 결과: {predicted_label}")
        plt.imshow(img_array.reshape(28, 28), cmap='gray')
        plt.title(f"🧠 예측: {predicted_label}")
        plt.axis('off')
        plt.show()

# 실행
if __name__ == "__main__":
    DrawApp()
