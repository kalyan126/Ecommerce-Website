pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
         checkout scmGit(branches: [[name: '*/main']], extensions: [], gitTool: 'Default', userRemoteConfigs: [[url: 'https://github.com/kalyan126/Ecommerce-Website.git']])
      }
    }
    
    stage('Deploy to server') {
      steps {
        sshPublisher(publishers: [
          sshPublisherDesc(configName: 'server-ssh', transfers: [
            sshTransfer(cleanRemote: true, execCommand: "rsync -ravz --delete ${env.WORKSPACE}/ ansibleadmin@172.31.15.115:/opt/docker", execTimeout: 120000, excludes: '', flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/opt/docker')
          ])
        ])
      }
    }
  }
}
