pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KyoTimz/devops-158-Expi2b-tp.git'
            }
        }

        stage('Pull latest code') {
            steps {
                dir('/home/kyo/devops-158-Expi2b') {
                    git branch: 'main', url: 'https://github.com/KyoTimz/devops-158-Expi2b-tp.git'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('/home/kyo/devops-158-Expi2b') {
                    sh '''
                        . venv/bin/activate
                        pip install flask pytest
                    '''
                }
            }
        }

        stage('Run unit tests') {
            steps {
                dir('/home/kyo/devops-158-Expi2b') {
                    sh '''
                        . venv/bin/activate
                        python -m pytest test_app.py -v --tb=short
                    '''
                }
            }
            post {
                success {
                    echo 'Tous les tests unitaires sont passés avec succès !'
                }
                failure {
                    echo 'Échec des tests unitaires. Le déploiement est annulé.'
                }
            }
        }

        stage('Restart Flask app') {
            steps {
                script {
                    sh 'pkill -f "python app.py" || true'
                    sh '''
                        cd /home/kyo/devops-158-Expi2b
                        . venv/bin/activate
                        JENKINS_NODE_COOKIE=dontKillMe nohup python app.py > flask.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
