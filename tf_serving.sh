docker pull tensorflow/serving
git clone https://github.com/tensorflow/serving
TESTDATA="$(pwd)/keras-and-tensorflow-serving"
docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/cat_dog:/models/cat_dog" \
    -e MODEL_NAME=cat_dog \
    tensorflow/serving &
