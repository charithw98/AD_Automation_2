pipeline {
    agent {
        docker { image 'jenkins/jenkins:lts' }  // Ensure correct image
    }
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Run commands inside the container
                    sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip python3-ldap3
                    '''
                }
            }
        }
        stage('Verify Installation') {
            steps {
                sh 'python3 --version && pip3 --version'
            }
        }
        stage('Move AD User') {
            steps {
                echo 'Implement your AD user script here...'
            }
        }
    }
    post {
        failure {
            echo 'Build failed! Check logs for details.'
        }
    }
}
