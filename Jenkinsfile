pipeline {
    agent {
        any {
            image 'jenkins/jenkins:lts'  // Ensure Jenkins is running in Docker
            args '-u root'               // Run the container as root during this stage
        }
    }
    environment {
        CONTAINER_NAME = 'jenkins_container'  // Update this with your container's actual name
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Accessing container as root and installing dependencies..."
                    sh '''
                    apt update &&
                    apt install -y python3 python3-pip python3-ldap3 &&
                    echo "Dependencies installed successfully"
                    '''
                }
            }
        }

        stage('Verify Installation') {
            steps {
                sh '''
                python3 -c "import ldap3; print(ldap3.__version__)"
                '''
            }
        }

        stage('Move AD User') {
            steps {
                echo "Proceeding with AD User operation..."
                // Add your AD User script/commands here
            }
        }
    }

    post {
        always {
            echo "Build completed!"
        }
        failure {
            echo "Build failed! Check logs for details."
        }
    }
}
