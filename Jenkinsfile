pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building..'
                sh 'docker cp'
                sh 'python virtualserver.py'
            }
        }
    }
}
