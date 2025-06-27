import numpy as np
from tensorflow.keras import datasets, models
import matplotlib.pyplot as plt
import random

# 모델 로드
model = models.load_model("lenet5_mnist.h5")
print("LeNet-5 모델 로딩 완료!")

# MNIST 테스트 데이터 불러오기 및 전처리
(_, _), (X_test, y_test) = datasets.mnist.load_data()
X_test = X_test / 255.0
X_test = X_test.reshape((-1, 28, 28, 1))  # CNN 입력 형태로 변형

# 전체 테스트셋에 대한 정확도 평가
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\n🎯 전체 테스트 정확도: {test_acc:.4f}")
print(f"🧪 전체 테스트 손실: {test_loss:.4f}")

# 예시: 랜덤 샘플 하나 예측 시각화
index = random.randint(0, len(X_test) - 1)
sample_image = X_test[index]
sample_label = y_test[index]

prediction = model.predict(sample_image.reshape(1, 28, 28, 1), verbose=0)
predicted_label = np.argmax(prediction)

plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Actual: {sample_label} | Predicted: {predicted_label}")
plt.axis('off')
plt.show()

print(f"실제 레이블: {sample_label}")
print(f"예측 결과: {predicted_label}")
