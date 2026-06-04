pipeline {
    agent any

    stages{
        stage("Cloning from Github.."){
            steps{
                script{
                    echo 'Cloning from Github..'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-id-1', url: 'https://github.com/abhichris63/MLOPS_project.git']])
                }
            }
        }
    }
<<<<<<< HEAD:jenkinsfile
}
=======
)
>>>>>>> f0a2b4720b5c4d9a9b65dfa5c29dbd8e2de6d2de:Jenkinsfile
