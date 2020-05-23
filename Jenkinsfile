pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7' 
                }
            }
            steps {
		        sh 'virtualenv -p /usr/bin/python3 venv'
		        sh 'source venv/bin/activate && pip install -r requirements.txt'
                stash(name: 'compiled-results', includes: 'script/*.py*') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml script/server.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}