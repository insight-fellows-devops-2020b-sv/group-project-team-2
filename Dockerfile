FROM python:3.6-slim
# COPY ./app.py /deploy/
# COPY ./requirements.txt /deploy/
# COPY ./iris_trained_model.pkl /deploy/
# WORKDIR /deploy/
COPY . /
RUN sudo pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN chmod +x tf_serving.sh
# RUN tf_serving.sh
EXPOSE 80
ENTRYPOINT ["python", "app.py"]
