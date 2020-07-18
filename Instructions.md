# group-project-team-2
#Instructions to run the project
   1. instance should have git and docker installed to run tf_serving.
   2. Copy cat_dog folder (which has ml model) to your instance. This folder is required for running tf_serving.sh 
   3. Run tf_serving.sh to start the tensorflow server: 
        sh tf_serving.sh
   4. To run flask app, use Dockerfile : use 'docker build' and 'docker run' commands.
   5. The port or tf server is 8501 on localhost and the port for Flask app is 80 on loalhost. These can be changed by changes in tf_serving.sh, app.py and Dockerfile.
   
   
   
 #TODO : 
   1. Tests can be mentioned in manage.py which can run tests, or in app.py itself with separate route like: localhost:80/test_ml_model.
   
 #Problems
   1. As tf_serving file has docker pull and docker run commands, tf_serving is separated from flask dockerfile. 
   

