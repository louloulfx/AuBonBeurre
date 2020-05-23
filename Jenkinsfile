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
                withEnv(["HOME=$(env.WORKSPACE}"]) {
		            sh 'pip install --user -r requirements.txt'
                    sh 'py.test --junit-xml test-reports/results.xml script/server.py'
                }
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}