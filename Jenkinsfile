pipeline {
    agent {
        label 'linux'
    }
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('davidgalstyan-dockerhub')
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t davidgalstyan/dp-alpine:latest .'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push davidgalstyan./dp-alpine:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}