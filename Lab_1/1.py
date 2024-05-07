import numpy as np
import matplotlib.pyplot as plt

# Задаємо восьмикутник
def generate_octagon():
    x = np.array([3, 3, 5, 8, 10, 10, 8, 5, 3])
    y = np.array([6, 8, 10, 10, 8, 6, 4, 4, 6])
    return np.column_stack((x, y))

# Зменшуємо восьмикутник
def reduce_octagon(octagon, scale_factor=1.5):
    return octagon / scale_factor

# Відображаємо восьмикутник відносно початку координат
def reflect_octagon(octagon):
    return -octagon

# Задаємо точки для прямої
point1 = np.array([0, -5])
point2 = np.array([15, 10])

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

# Визначаємо коефіцієнти прямої
k = (point2[1] - point1[1]) / (point2[0] - point1[0])
c = point1[1] - k * point1[0]

# Задаємо матриці перетворень
# Матриця зміщення на вектор (0, -c)
T1 = np.array([[1, 0], [0, 1]])
b1 = np.array([0, -c])
# Матриця повороту на кут -fi
fi = np.arctan(k)
T2 = np.array([[np.cos(-fi), -np.sin(-fi)], [np.sin(-fi), np.cos(-fi)]])
# Матриця симетричного відображення відносно осі Ox
T3 = np.array([[1, 0], [0, -1]])
# Матриця повороту на кут fi
T4 = np.array([[np.cos(fi), -np.sin(fi)], [np.sin(fi), np.cos(fi)]])
# Матриця зміщення на вектор (0, c)
T5 = np.array([[1, 0], [0, 1]])
b5 = np.array([0, c])


def plot_octagon(octagon1, octagon2, octagon3, octagon4, title):
    plt.figure(figsize=(8, 6))
    plt.plot(octagon1[:, 0], octagon1[:, 1], 'b-', label='Початковий 8-кутник')
    plt.fill(octagon1[:, 0], octagon1[:, 1], 'b', alpha=0.3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20,20,-20,20])
    plt.title(title[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(octagon2[:, 0], octagon2[:, 1], 'r-', label='Зменшений 8-кутник (в 1.5 рази)')
    plt.fill(octagon2[:, 0], octagon2[:, 1], 'r', alpha=0.3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20,20,-20,20])
    plt.title(title[1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(octagon3[:, 0], octagon3[:, 1], 'g-', label='Відображений 8-кутник (початок координат)')
    plt.fill(octagon3[:, 0], octagon3[:, 1], 'g', alpha=0.3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20,20,-20,20])
    plt.title(title[2])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, 'y-', label='Пряма')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20,20,-20,20])
    plt.title(title[3])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(octagon4[:, 0], octagon4[:, 1], 'c-', label='Відображений 8-кутник (відносно прямої)')
    plt.fill(octagon4[:, 0], octagon4[:, 1], 'c', alpha=0.3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20,20,-20,20])
    plt.title(title[4])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(octagon1[:, 0], octagon1[:, 1], 'b-', label='Початковий 8-кутник')
    plt.fill(octagon1[:, 0], octagon1[:, 1], 'b', alpha=0.3)
    plt.plot(octagon2[:, 0], octagon2[:, 1], 'r-', label='Зменшений 8-кутник (в 1.5 рази)')
    plt.fill(octagon2[:, 0], octagon2[:, 1], 'r', alpha=0.3)
    plt.plot(octagon3[:, 0], octagon3[:, 1], 'g-', label='Відображений 8-кутник (початок координат)')
    plt.fill(octagon3[:, 0], octagon3[:, 1], 'g', alpha=0.3)
    plt.plot(x_values, y_values, 'y-', label='Пряма')
    plt.plot(octagon4[:, 0], octagon4[:, 1], 'c-', label='Відображений 8-кутник (відносно прямої)')
    plt.fill(octagon4[:, 0], octagon4[:, 1], 'c', alpha=0.3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-20, 20, -20, 20])
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Відображення точок відносно прямої
octagon = generate_octagon()
octagon_reflected = octagon.copy()
octagon_reflected = np.dot(octagon_reflected + b1, T1.T)
octagon_reflected = np.dot(octagon_reflected, T2.T)
octagon_reflected = np.dot(octagon_reflected, T3.T)
octagon_reflected = np.dot(octagon_reflected, T4.T)
octagon_reflected = np.dot(octagon_reflected + b5, T5.T)
reduced_octagon = reduce_octagon(octagon, scale_factor=1.5)
reflected_reduced_octagon = reflect_octagon(reduced_octagon)
plot_octagon(octagon, reduced_octagon, reflected_reduced_octagon, octagon_reflected, 'загальний графік')



