pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{

        stage("Cloning from Github.."){
            steps{
                script{
                    echo 'Cloning from Github..'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-id-1', url: 'https://github.com/abhichris63/MLOPS_project.git']])
                }
            }
        }

        stage("Creating a Virtual Environment...."){
            steps{
                script{
                    echo 'Creating a Virtual Environment....'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -e .
                    pip install dvc
                    '''
                }
            }
        }
    // stage('Debug'){
    //     steps{
    //         sh '''
    //         pwd
    //         ls -la
    //         find . -maxdepth 2 -name ".dvc"
    //         '''
    //     }
    // }
        stage('DVC Pull'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC pull....'
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }
            }
        }
    }
}