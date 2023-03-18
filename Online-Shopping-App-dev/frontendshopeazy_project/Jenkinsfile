pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', 
          branches: [[name: 'master']],
          userRemoteConfigs: [[url: 'https://github.com/kalyan126/Ecommerce-Website/tree/main/Online-Shopping-App-dev/frontendshopeazy_project']]
        ])
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
