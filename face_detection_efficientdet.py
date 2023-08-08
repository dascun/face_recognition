import cv2
import numpy as np
import tensorflow as tf

### Need to get pre-trained weights (WIP)

# # Load the EfficientDet model
# model = (
#     tf.keras.applications.EfficientDetB0()
# )  # Change to the desired EfficientDet variant

# # Load the image
# image = cv2.imread(".\images\selfie.jpg")

# # Preprocess the image
# input_size = (224, 224)  # Change to the input size expected by the model
# input_image = cv2.resize(image, input_size)
# input_image = input_image / 255.0  # Normalize pixel values

# # Perform inference
# input_tensor = np.expand_dims(input_image, axis=0)
# predictions = model.predict(input_tensor)

# # Process and draw bounding boxes
# confidence_threshold = 0.5
# for prediction in predictions:  # Process the predictions accordingly
#     confidence = prediction[..., 4]
#     bounding_box = prediction[..., :4]

#     # Filter based on confidence threshold
#     filtered_indices = np.where(confidence > confidence_threshold)
#     filtered_boxes = bounding_box[filtered_indices]

#     # Draw bounding boxes
#     for box in filtered_boxes:
#         ymin, xmin, ymax, xmax = box
#         ymin *= input_size[0]
#         xmin *= input_size[1]
#         ymax *= input_size[0]
#         xmax *= input_size[1]

#         cv2.rectangle(
#             image,
#             (int(xmin), int(ymin)),
#             (int(xmax), int(ymax)),
#             (0, 255, 0),
#             2,
#         )

# # Display and save the image
# cv2.imshow("Detected Faces", image)
# cv2.imwrite("selfie_output_image_efficientdet.jpg", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
