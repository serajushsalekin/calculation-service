pipeline {
    agent any
    environment {
        registry = "salekin/calculation-service"
        version = "$BUILD_NUMBER"
    }
    stages {
        stage('Build') {
            steps {
                git 'https://github.com/serajushsalekin/calculation-service.git'
                sh "docker build -t ${env.registry}:${env.version} ."
            }
        }

        stage('Test') {
            when {
                expression {
                    BRANCH_NAME == 'master'
                }
            }
            agent {
                docker { image "${env.registry}:${env.version}" }
            }
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            when {
                expression {
                    BRANCH_NAME == 'master'
                }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'usr', passwordVariable: 'passwrd')]) {
                        sh "echo $passwrd | docker login -u $usr --password-stdin"
                        sh "docker image push ${env.registry}:${env.version}"
                    }
                }
            }
        }

        stage('Deploy (Production)') {
            steps {
                sh "echo 'deploying...'"
            }
        }
    }

    post {
        always {
            echo "Performing cleanup..."
            echo "Removing docker image: ${env.registry}:${env.version}"
            sh "docker rmi ${env.registry}:${env.version}"
            echo "Removing pipeline artifact..."
            cleanWs()
        }
    }
}
