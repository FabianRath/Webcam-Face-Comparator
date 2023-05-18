# Webcam-Face-Comparator
This script will access a webcam that is connected to the computer and try to find a face. If a face has been found it will match that face against a reference image, when the two are different a picture of the webcam will be taken and saved.

This script uses the dlib library for the detection of the face.

To use this, you just need to have an image named 'reference_image.jpg' in the same folder as the script. When there is no match, a new folder will be created named no_match_faces into which a picture will be saved. The name of these images will be for e.g., no_match_2023-05-18_12-46-38.png.

Make sure that your face looks directly into the camera, and it is decently lighted.
