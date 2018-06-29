pipeline {
    agent {docker { image 'python'}}
    stages {
        stage('build') {
            steps {
                echo 'Building..'
                sh 'docker version'
            }
        }
    }
}
