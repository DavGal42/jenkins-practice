pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
            }
        }   
        stage('Test') {
            steps {
                sh 'echo "Testing the application..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
            }
        }
    }

    post {
        always {
            sh 'echo "Hello Post"'
        }
        success {
            sh 'echo "Hello Post"'
        }
        failure {
            sh 'echo "Hello Post"'
        }
    }
}