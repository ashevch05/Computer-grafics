import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Початкові координати вершин куба
vertices_initial = np.array([[0, 0, 0],
                             [1, 0, 0],
                             [1, 1, 0],
                             [0, 1, 0],
                             [0, 0, 1],
                             [1, 0, 1],
                             [1, 1, 1],
                             [0, 1, 1],
                             [0, 0, 0]])  # Додаємо початкову точку, щоб замкнути куб

# Масштабування куба (збільшення, зменшення у кілька разів)
scale_factor = 2
scaling_matrix = np.array([[scale_factor, 0, 0],
                           [0, scale_factor, 0],
                           [0, 0, scale_factor]])

# Застосування матриці масштабування до вершин куба
vertices_scaled = vertices_initial.dot(scaling_matrix)

# Масив з'єднаних точок для обох кубів
connected_points = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Симетричне відображення куба відносно початку координат
symmetry_matrix_origin = np.array([[-1, 0, 0],
                                   [0, -1, 0],
                                   [0, 0, -1]])

# Симетричне відображення куба відносно площини Z=0
symmetry_matrix_plane = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, -1]])

# Застосування матриць симетрії до збільшеного куба
vertices_symmetric_origin = vertices_scaled.dot(symmetry_matrix_origin)
vertices_symmetric_plane = vertices_scaled.dot(symmetry_matrix_plane)


# Виведення графіків
plt.figure(figsize=(12, 6))

# Виведення графіку кубів
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Малюємо з'єднані точки початкового куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_initial[p1], vertices_initial[p2]), color='r')

# Малюємо з'єднані точки збільшеного куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_scaled[p1], vertices_scaled[p2]), color='b')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Початковий і збільшений куби')

plt.show()

# Виведення графіку симетричного відображення відносно початку коодинат
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Малюємо з'єднані точки відображеного куба відносно початку коодинат
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_symmetric_origin[p1], vertices_symmetric_origin[p2]), color='g')

# Малюємо з'єднані точки збільшеного куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_scaled[p1], vertices_scaled[p2]), color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Симетричне відображення куба\nвідносно початку координат')

plt.show()

# Виведення графіку симетричного відображення куба відносно площини Z=0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Малюємо з'єднані точки відображеного куба відносно площини
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_symmetric_plane[p1], vertices_symmetric_plane[p2]), color='y')

# Малюємо з'єднані точки збільшеного куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_scaled[p1], vertices_scaled[p2]), color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Симетричне відображення куба\nвідносно площини Z=0')

plt.show()

#Кут повороту
phi_rad = np.deg2rad(90)

# Параметри прямої L та кут повороту
a, b, c = 2, 1, 3  # Координати точки A
l, m, n = 1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)  # Направляючий вектор прямої L

# Обчислення матриці повороту навколо прямої L
# Поетапне перетворення координат, використовуючи матриці повороту R_x, R_y, R_z та їх обернені.
R_x = np.array([[1, 0, 0, 0],
                [0, n / np.sqrt(m**2 + n**2), -m / np.sqrt(m**2 + n**2), 0],
                [0, m / np.sqrt(m**2 + n**2), n / np.sqrt(m**2 + n**2), 0],
                [0, 0, 0, 1]])

R_y = np.array([[np.sqrt(m**2 + n**2), 0, l, 0],
                [0, 1, 0, 0],
                [-l, 0, np.sqrt(m**2 + n**2), 0],
                [0, 0, 0, 1]])

R_z = np.array([[np.cos(phi_rad), -np.sin(phi_rad), 0, 0],
                [np.sin(phi_rad), np.cos(phi_rad), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

R_y_inv = np.linalg.inv(R_y)
R_x_inv = np.linalg.inv(R_x)

R = np.eye(4)
R = R @ np.linalg.inv(R_x) @ np.linalg.inv(R_y) @ R_z @ R_y @ R_x
R = R @ np.array([[1, 0, 0, -a],
                  [0, 1, 0, -b],
                  [0, 0, 1, -c],
                  [0, 0, 0, 1]])

# Поворот куба навколо прямої L
rotated_vertices = np.dot(R, np.hstack((vertices_initial, np.ones((9, 1), dtype=np.float32))).T).T[:, :3]

# Виведення графіка повернутого куба та прямої
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Малюємо з'єднані точки збільшеного куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_scaled[p1], vertices_scaled[p2]), color='b')

# Малюємо з'єднані точки повернутого куба
for p1, p2 in connected_points:
    ax.plot(*zip(rotated_vertices[p1], rotated_vertices[p2]), color='brown')

# Відображення прямої
point = np.array([a, b, c])
direction = np.array([l, m, n])
ax.quiver(point[0], point[1], point[2], direction[0], direction[1], direction[2], color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Повернутий куб навколо прямої та пряма')

plt.show()

# Три точки, що задають площину (за умови, що вони не лежать на одній прямій)
point1 = np.array([1, 0, 0])
point2 = np.array([0, 1, 0])
point3 = np.array([0, 0, 1])

# Знаходимо вектори, що утворюють площину
v1 = point2 - point1
v2 = point3 - point1

# Нормалізуємо вектор, що утворює площину
normal_vector = np.cross(v1, v2)
normal_vector = normal_vector.astype(np.float64)
normal_vector /= np.linalg.norm(normal_vector)

# Побудова матриці перетворення для симетрії відносно площини
symmetry_matrix_plane = np.eye(3) - 2 * np.outer(normal_vector, normal_vector)

# Застосування матриці симетрії до збільшеного куба
vertices_symmetric_plane = vertices_scaled.dot(symmetry_matrix_plane)

# Виведення графіка збільшеного куба і симетричного куба відносно площини
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Малюємо з'єднані точки збільшеного куба
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_scaled[p1], vertices_scaled[p2]), color='b')

# Малюємо з'єднані точки симетричного куба відносно площини
for p1, p2 in connected_points:
    ax.plot(*zip(vertices_symmetric_plane[p1], vertices_symmetric_plane[p2]), color='purple')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Збільшений куб та симетричний куб відносно площини')

plt.show()


