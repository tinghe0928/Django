    pipeline {
    agent any 
	tools{
	    maven 'apache-maven-3.0.1'
	}
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
	post{
	    always{
		    sh 'ls -l'
		}
	
	}
}
