pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Behave tests') {
            steps {
                bat 'behave --junit --junit-directory reports'
            }
        }

        stage('Publish test results') {
            steps {
                junit 'reports/*.xml'
            }
        }
    }
}
