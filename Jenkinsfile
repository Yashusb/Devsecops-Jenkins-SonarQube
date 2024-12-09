pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Cloning the repository
                git branch: 'main', credentialsId: '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', url: 'https://github.com/Yashusb/Devsecops.git'
            }    
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Running SonarQube analysis
                    withSonarQubeEnv('Yashvanth-sonar') { // Ensure this matches the name in SonarQube settings
                        sh "/opt/sonar-scanner/bin/sonar-scanner \
                            -Dsonar.projectKey=Sonar-jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://34.249.250.122:9000 \
                            -Dsonar.login=ssqu_66de582069b1811add5c2a8e72e0bdf40202d18f"
                    }
                }
            }
        }
        stage('Quality Gate') {
            steps {
                script {
                    // Wait for the quality gate result
                    timeout(time: 5, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }
           stage('Deploy Application') 
           {
            steps 
            {
                sshagent(['yashudev.pem']) 
                {
                    sh '''
                    ssh ec2-user@3.254.61.67 << EOF
                    cd /home/ubuntu/Devsecops
                    git pull origin main
                    source venv/bin/activate
                    python manage.py migrate
                
                }
            }
        }
    }
}