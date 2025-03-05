pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Chiranthkalkatte/prod-prac.git'
            }
        }

        stage('Deploy to Server') {
            steps {
                sh 'scp -i ~/.ssh/id_rsa circularlist.py ubuntu@52.34.215.41:/home/ubuntu/circularlist.py'
            }
        }

        stage('Run Script on Server') {
            steps {
                sh 'ssh -i ~/.ssh/id_rsa ubuntu@52.34.215.41 "python3 /home/ubuntu/circularlist.py"'
            }
        }
    }
}
