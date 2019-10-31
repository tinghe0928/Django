pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Hello world!' 
				sh 'mvn --version'
            }
        }
		stage('Test') {
            steps {
                echo 'Hello world!' 
				sh 'java -version'
            }
        }
    }
}
