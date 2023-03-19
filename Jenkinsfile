pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        checkout scmGit(branches: [[name: '*/main']], extensions: [], gitTool: 'Default', userRemoteConfigs: [[url: 'https://github.com/kalyan126/Ecommerce-Website.git']])
      }
    }
    
    stage('Deploy to server') {
      stages {
        stage('Execute Multiple Commands on Remote Shell') {
            steps {
                script {
                    def sshCommand = "ssh ansibleadmin@172.31.15.115 'cd /opt/docker;ls -al;mkdir ddos'"
                    sh sshCommand
                }
            }
        }
    }
    }
  }
}
