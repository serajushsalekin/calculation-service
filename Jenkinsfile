pipeline {
    agent any
    environment {
        registry = "salekin/calculation-service"
        registryCredential = 'dockerhub_creds'
        version = "$BUILD_NUMBER"
        DOCKER_CREDS = credentials('docker-creds')
    }
    stages {
        stage('Build') {
            steps {
                git 'https://github.com/serajushsalekin/calculation-service.git'
                sh 'docker build -t ${env.registry}:${env.version} .'
            }
        }

        stage('Test') {
            when {
                expression {
                    return env.CHANGE_BRANCH == 'merge-request' || env.CHANGE_BRANCH == 'master'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }

//         stage('Build and Push Docker Image') {
//             when {
//                 BRANCH_NAME == 'master'
//             }
//             steps {
//                 docker.withRegistry( '', registryCredential ) {
//                         dockerImage.push()
//                 }
//             }
//         }

        stage('Deploy (Production)') {
            steps {
                sh "echo 'deploying...'"
            }
        }
    }

    post {
        always {
            echo "Performing cleanup..."
            echo "DockerImage: ${env.registry}:${env.version}"
            // Remove all Docker images
            sh 'docker rmi ${env.registry}:${env.version}'
        }
    }
}
