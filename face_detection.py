import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load the image
image = cv2.imread(".\images\selfie.jpg")

# Convert the image to grayscale (face detection works better on grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(100, 100)
)

# Draw rectangles around the detected faces
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Resize the image to fit within the screen
max_height, max_width = 800, 1200  # Define your desired maximum dimensions
resized_image = image.copy()

# Resize if the image dimensions exceed the maximum
if image.shape[0] > max_height or image.shape[1] > max_width:
    resized_image = cv2.resize(resized_image, (max_width, max_height))


# Save the resized image with detected faces
output_path = ".\images\selfie_output_image.jpg"
cv2.imwrite(output_path, resized_image)

# Display the resized image with detected faces
cv2.imshow("Resized Image with Detected Faces", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
