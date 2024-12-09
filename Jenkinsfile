pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER = 'Yashvanth-sonar' // Scanner name in Jenkins
        SONARQUBE_SERVER = 'YashuSoanrQube'       // SonarQube server name
        DEPLOY_SERVER = 'ec2-user@3.254.61.67'
        GITHUB_TOKEN = credentials('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')
    }
    stages {
        stage('Checkout Code') {
            steps {
                script 
                {
                withCredentials([[$class: 'UsernamePasswordCredentials', credentialsId: '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']]) {
                       // sh 'git clone https://github.com/Yashusb/Devsecops.git'
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=Sonar-jenkins \
                        -Dsonar.sources=Devsecops \
                        -Dsonar.host.url=http://34.249.250.122:9000 \
                        -Dsonar.login=squ_66de582069b1811add5c2a8e72e0bdf40202d18f
                    '''
                }
            }
        }
        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 5, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                sshagent(['yashudev.pem']) {
                    sh '''
                    ssh ec2-user@3.254.61.67 << EOF
                    cd /home/ubuntu/Devsecops
                    git pull origin main
                    source venv/bin/activate
                    python manage.py migrate
                    EOF
                    '''
                }
            }
        }
    }
}
}
