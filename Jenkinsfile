pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7' 
                    args '-u root:root'
                }
            }
            steps {
                sh 'pip install mysql-connector-python'
                sh 'python -m py_compile script/generate.py script/server.py'
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