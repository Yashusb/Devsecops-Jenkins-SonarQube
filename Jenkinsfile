pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                script {
            checkout scm: [
                $class: 'GitSCM',
                branches: [[name: '*/main']],
                userRemoteConfigs: [[
                    url: 'https://t',
                    credentialsId: 'Git-token-new'
                ]]
            ]
        }      
    }
 }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Running SonarQube analysis here
                    withSonarQubeEnv('YashuSonar') { // Ensure this matches the name in SonarQube settings
                        sh "/opt/sonar-scanner/bin/sonar-scanner \
                            -Dsonar.projectKey=Sonar-jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://34.249.250.122:9000 \
                            -Dsonar.login=s"
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
            stage('Email Notification') {
             steps {
                 script {
                     // Sending an email report
                     emailext
                     (
                         subject: "SonarQube Analysis Report",
                         body: "SonarQube analysis for your project has been completed. Check the report at: http://34.241.174.22:9000/dashboard?id=sonarserver",
                         to: 'xcirl.ie')
                 }
             }
         }
    }
}
