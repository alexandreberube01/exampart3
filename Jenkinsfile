pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                echo 'Installation des dépendances Python...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run scraper') {
            steps {
                echo 'Exécution du script scraper.py...'
                bat 'python scraper.py'
            }
        }

        stage('Archive data.csv') {
            steps {
                echo 'Archivage du fichier CSV...'
                archiveArtifacts artifacts: 'data.csv', fingerprint: true
            }
        }
    }
}