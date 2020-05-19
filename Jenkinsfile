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
                sh 'easy_install pathlib'
                sh 'python -m py_compile script/server.py script/generate.py' 
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