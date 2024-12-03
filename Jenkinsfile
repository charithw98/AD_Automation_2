pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'jenkins_container'  // Replace with your actual container name
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Accessing container as root and installing dependencies..."
                sh """
                docker exec -u root ${CONTAINER_NAME} bash -c '
                apt-get update &&
                apt-get install -y python3 python3-pip python3-ldap3 &&
                echo "Dependencies installed successfully"
                '
                """
            }
        }

        stage('Verify Installation') {
            steps {
                echo "Verifying dependency installation..."
                sh """
                docker exec ${CONTAINER_NAME} bash -c '
                python3 -c "import ldap3; print(ldap3.__version__)"
                '
                """
            }
        }

        stage('Move AD User') {
            steps {
                echo "Proceeding with AD User operation..."
                // Add your AD User movement script or command here
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
