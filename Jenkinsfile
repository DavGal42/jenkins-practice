pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'
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
            when {
                expression {
                    BRANCH_NAME == 'dev' || BRANCH_NAME == 'master'
                }
            }

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