pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                echo 'Building..'
                sh 'docker version'
            }
        }
    }
}
