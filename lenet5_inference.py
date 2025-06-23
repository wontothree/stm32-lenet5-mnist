import numpy as np
from tensorflow.keras import datasets, models
import matplotlib.pyplot as plt
import random

model = models.load_model("lenet5_mnist.h5")
print("Complete to load LeNet-5!")

# MNIST 데이터 불러오기 및 전처리
(_, _), (X_test, y_test) = datasets.mnist.load_data()
X_test = X_test / 255.0
X_test = X_test.reshape((-1, 28, 28, 1))  # CNN 입력 형태로 변형

# 랜덤 샘플 선택
index = random.randint(0, len(X_test) - 1)
sample_image = X_test[index] # 샘플링된 이미지
sample_label = y_test[index] # 정답

# print(sample_image)
# print("sample_image 타입:", type(sample_image))
# print("sample_image shape:", sample_image.shape)
# print("sample_image dtype:", sample_image.dtype)

# 예측 수행
prediction = model.predict(sample_image.reshape(1, 28, 28, 1))
predicted_label = np.argmax(prediction)

# 결과 출력
plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Actual: {sample_label} | Predicted: {predicted_label}")
plt.axis('off')
plt.show()

print(f"실제 레이블: {sample_label}")
print(f"예측 결과: {predicted_label}")
