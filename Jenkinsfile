pipeline {
    agent {
        any {
            image 'python:3.11'  // Use an official Python image
            args '-u root'  // Run as root to install dependencies
        }
    }

    parameters {
        string(name: 'AD_USERNAME', description: 'Enter the AD username to move')
        choice(name: 'TARGET_OU', choices: ['TestOU1', 'TestOU2'], description: 'Select the target OU')
    }

    environment {
        AD_SERVER = '10.101.16.42'
        AD_USER = 'tase'
        AD_PASSWORD = 'Testuser@123'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install ldap3
                '''
            }
        }

        stage('Move AD User') {
            steps {
                script {
                    def username = params.AD_USERNAME
                    def target_ou = params.TARGET_OU
                    def server_ip = env.AD_SERVER
                    def ad_user = env.AD_USER
                    def ad_password = env.AD_PASSWORD

                    // Run the Python script
                    sh """
                        python3 move_user.py "${username}" "${target_ou}" "${server_ip}" "${ad_user}" "${ad_password}"
                    """
                }
            }
        }
    }

    post {
        success {
            echo "User '${params.AD_USERNAME}' moved successfully to '${params.TARGET_OU}'."
        }
        failure {
            echo "Failed to move the user '${params.AD_USERNAME}'. Check logs for details."
        }
    }
}
