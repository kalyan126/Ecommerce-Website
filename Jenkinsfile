pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          doGenerateSubmoduleConfigurations: false, 
                          extensions: [], 
                          submoduleCfg: [], 
                          userRemoteConfigs: [[url: 'https://github.com/kalyan126/Ecommerce-Website.git']]])
            }
        }
        
        stage('Deploy') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'ansible',
                            transfers: [
                                sshTransfer(
		                    execCommand:' cd /opt/docker && git clone https://github.com/kalyan126/Ecommerce-Website.git',
                                    execTimeout: 120000
                                )
                            ]
                        )
                    ]
                )
            }
        }
    }
}
