from PIL import Image
import face_recognition

image = face_recognition.load_image_file("./img/groups/team1.jpg")
face_locations = face_recognition.face_locations(image)

for face_locations in face_locations:
    top, right, bottom, left = face_locations

    face_image = image[top:bottom, left:right]

    pil_image = Image.fromarray(face_image)

    # his Command open SO image viewer with image faces
    pil_image.show()

    # This command .save() save images in your local project folder.
    pil_image.save(f'{top}.jpg')
