pipeline {
    agent {
	    docker { image 'docker.io/jenkins/jenkins:lts' }	
	}
    stages {
        stage('Say Hello') {
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
		stage('Example') {
			input {
				message "Should we continue?"
				ok "Yes, we should."
				submitter "alice,bob"
				parameters {
					string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
				}
			}
			steps {
				echo "Hello, ${PERSON}, nice to meet you."
			}
		}
    }		
	post{
	    always{
		    sh 'ls -l'
		}
	
	}
}
