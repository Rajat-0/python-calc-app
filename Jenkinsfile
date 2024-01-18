pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from your version control system (e.g., Git)
                git 'git@github.com:Rajat-0/python-calc-app.git'
                echo 'Chekout complete'
            }
        }

        stage('Build') {
            steps {
                // Your build steps here
                echo 'Building the project...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Your test steps here
                echo 'Running tests...'
                sh 'python test_calculator.py'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                // Deploy only if the build is successful
                echo 'Deploying the application...'
            }
        }
    }

    post {
        success {
            // Actions to perform when the pipeline succeeds
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions to perform when the pipeline fails
            echo 'Pipeline failed! Notify the team...'
        }
    }
}
