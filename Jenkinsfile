pipeline {
    agent any

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
                script {
                    echo 'Installing dependencies...'
                    // Run installation commands as root
                    sh """
                        apt-get update
                        apt-get install -y python3 python3-pip python3-ldap3
                        apt-get clean
                    """
                }
            }
        }

        stage('Move AD User') {
            steps {
                script {
                    // Retrieve user input parameters
                    def username = params.AD_USERNAME
                    def target_ou = params.TARGET_OU
                    def server_ip = env.AD_SERVER
                    def ad_user = env.AD_USER
                    def ad_password = env.AD_PASSWORD

                    // Execute the Python script to move the AD user
                    sh """
                        python3 move_user.py "${username}" ${target_ou} ${server_ip} ${ad_user} ${ad_password}
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
