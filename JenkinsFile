pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile script/server.py script/generate.py' 
                stash(name: 'compiled-results', includes: 'script/*.py*') 
            }
        }
    }
}