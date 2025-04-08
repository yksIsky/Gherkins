pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'D:/Python/python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Behave tests') {
            steps {
                bat 'D:/Python/python.exe -m behave --junit --junit-directory reports'
            }
        }

        stage('Publish test results') {
            steps {
                junit 'reports/*.xml'
            }
        }
    }
}
