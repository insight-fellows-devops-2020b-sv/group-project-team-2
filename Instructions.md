# group-project-team-2
   - Instructions to run the project
         - instance should have git and docker installed to run tf_serving.
         - Copy cat_dog folder (which has ml model) to your instance. This folder is required for running tf_serving.sh 
         - Run tf_serving.sh to start the tensorflow server: 
              sh tf_serving.sh
         - To run flask app, use Dockerfile : use 'docker build' and 'docker run' commands.
         - The port or tf server is 8501 on localhost and the port for Flask app is 80 on loalhost. These can be changed by changes in tf_serving.sh, app.py and Dockerfile.
   
   
   - TODO : 
         - Tests can be mentioned in manage.py which can run tests, or in app.py itself with separate route like: localhost:80/test_ml_model.
   
   - Problems
         - As tf_serving file has docker pull and docker run commands, tf_serving is separated from flask dockerfile. 
   

