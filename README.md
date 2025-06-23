# LeNet-5 on STM32

# LeNet-5

```py
# LeNet-5 model
model = models.Sequential()
model.add(layers.Conv2D(6, (3, 3), activation='tanh', input_shape=(28, 28, 1)))  # Adjusted filter size
model.add(layers.AveragePooling2D(2))
model.add(layers.Activation('sigmoid'))
model.add(layers.Conv2D(16, (3, 3), activation='tanh'))  # Adjusted filter size
model.add(layers.AveragePooling2D(2))
model.add(layers.Activation('sigmoid'))
model.add(layers.Conv2D(120, (3, 3), activation='tanh'))  # Adjusted filter size
model.add(layers.Flatten())
model.add(layers.Dense(84, activation='tanh'))
model.add(layers.Dense(10, activation='softmax'))
```

- Trained on MNIST

# Tested Environment

- STM32N6 (Cortex-M55) / STM32N6 Nucleo-144 board (MB1940)

# Reference

[GradientBased Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)
