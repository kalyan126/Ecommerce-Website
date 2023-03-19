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
        
        stage('Deploy to Server') {
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: 'ansible-controlnode',
                                                          transfers: [sshTransfer(
                                                              execCommand: "rsync -ravz --delete ${env.WORKSPACE}/ ansibleadmin@172.31.15.115:/opt/docker",
                                                              remoteDirectory: "/opt/docker")])])
            }
        }
    }
    
    post {
        success {
            script {
                // continuously build and deploy on changes
                while (true) {
                    def scmVars = checkout([$class: 'GitSCM', 
                                            branches: [[name: '*/main']], 
                                            doGenerateSubmoduleConfigurations: false, 
                                            extensions: [], 
                                            submoduleCfg: [], 
                                            userRemoteConfigs: [[url: 'https://github.com/your-github-repo.git']]])
                    
                    if (scmVars.GIT_COMMIT != currentBuild.previousBuild?.actions.last()?.lastBuiltRevision?.SHA1String) {
                        // the latest commit hash is different from the previous build, so we need to deploy
                        sshPublisher(publishers: [sshPublisherDesc(configName: 'ansible-controlnode',
                                                                  transfers: [sshTransfer(
                                                                      execCommand: "rsync -ravz --delete ${env.WORKSPACE}/ ansibleadmin@172.31.15.115:/opt/docker",
                                                                      remoteDirectory: "/opt/docker")])])
                    }
                    
                    sleep 60 // wait 60 seconds before checking again
                }
            }
        }
    }
}
