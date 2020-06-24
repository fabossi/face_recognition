import face_recognition

image = face_recognition.load_image_file("./img/groups/team2.jpg")
face_locations = face_recognition.face_locations(image)

# Array of coordenates
# print(face_locations)

print(f'there are {len(face_locations)} people(s) in this image')
