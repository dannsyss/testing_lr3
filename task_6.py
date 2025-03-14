import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от -3π до 3π
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Вычисляем значения функции y = (sin(3x) * cos(2x)) / (3x)
# Чтобы избежать деления на ноль, заменяем x=0 на очень маленькое значение
x_corrected = np.where(x == 0, 1e-10, x)
y = (np.sin(3 * x_corrected) * np.cos(2 * x_corrected)) / (3 * x_corrected)

plt.plot(x, y, color='green')

# Добавляем названия осей
plt.xlabel('x')
plt.ylabel('y')

# Задаем подписи оси x, кратные π
plt.xticks(
    np.arange(-3 * np.pi, 3.5 * np.pi, np.pi),
    ['-3π', '-2π', '-π', '0', 'π', '2π', '3π']
)

plt.title('График функции y = (sin(3x) * cos(2x)) / (3x)')

plt.grid(True)

plt.show()