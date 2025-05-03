faces = {
    "Cube": 6,
    "Tetrahedron": 4,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

n = int(input())
faces_count = 0

for _ in range(n):
    polyhedron = input()
    faces_count = faces_count + faces[polyhedron]


print(faces_count)
