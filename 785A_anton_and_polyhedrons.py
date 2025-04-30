faces = {
    "cube": 6,
    "tetrahedron": 4,
    "octahedron": 8,
    "dodecahedron": 12,
    "icosahedron": 20,
}

n = int(input())
faces_count = 0

for _ in range(n):
    polyhedron = input().lower()
    faces_count = faces_count + faces[polyhedron]


print(faces_count)
