import time
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# LeNet-5 모델 정의
def build_lenet():
    model = models.Sequential()
    model.add(layers.Conv2D(6, (3, 3), activation='tanh', input_shape=(28, 28, 1)))
    model.add(layers.AveragePooling2D(2))
    model.add(layers.Activation('sigmoid'))
    model.add(layers.Conv2D(16, (3, 3), activation='tanh'))
    model.add(layers.AveragePooling2D(2))
    model.add(layers.Activation('sigmoid'))
    model.add(layers.Conv2D(120, (3, 3), activation='tanh'))
    model.add(layers.Flatten())
    model.add(layers.Dense(84, activation='tanh'))
    model.add(layers.Dense(10, activation='softmax'))
    return model

# MNIST 데이터셋 불러오기 및 전처리
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0
X_train = X_train.reshape((-1, 28, 28, 1))
X_test = X_test.reshape((-1, 28, 28, 1))

# 모델 생성 및 컴파일
model = build_lenet()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 학습
print("모델 학습 시작!")
start_time = time.time()
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), verbose=1)
print(f"학습 완료! 소요 시간: {time.time() - start_time:.2f}초")

# 테스트 데이터 평가
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\n 최종 테스트 정확도: {test_acc:.4f}, 테스트 손실: {test_loss:.4f}")

# 모델 저장
tf.keras.saving.save_model(model, 'my_model.keras')
print("모델 저장 완료: lenet5_mnist.h5")

# 사용자 숫자 이미지 예측 함수
def predict_user_digit(img_2d):
    """
    2D 이미지 (28x28)를 받아서 0~9 숫자를 예측합니다.
    """
    if img_2d.shape != (28, 28):
        raise ValueError("입력 이미지 크기는 반드시 (28, 28)이어야 합니다.")

    # 전처리: 정규화 및 차원 추가
    img = img_2d / 255.0
    img = img.reshape(1, 28, 28, 1)

    # 예측
    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)

    print(f"✅ 예측 결과: {predicted_label}")
    return predicted_label

# 예시: 테스트 이미지 하나 예측해 보기
index = 0
sample = X_test[index].reshape(28, 28)  # 테스트셋 이미지 하나 가져오기

plt.imshow(sample, cmap='gray')
plt.title("Test Sample")
plt.axis('off')
plt.show()

predict_user_digit(sample)
