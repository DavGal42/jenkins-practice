pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'
        SERVER_CREDENTIALS = credentials('server-credentials')
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    echo "Building the application..."
                    echo "This is a new version: ${NEW_VERSION}"
                    echo 'This is a new version: ${NEW_VERSION}'
                '''
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
                withCredentials([
                    usernamePassword(credentials: 'server-credentials', usernameVariable: USER, passwordVariable: PWD)
                ]) {
                    sh 'echo "${USER}, ${PWD}"'
                }
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