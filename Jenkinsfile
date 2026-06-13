pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'storage-cc-data'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
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
                    ${VENV_DIR}/bin/python -m pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -e .
                    ${VENV_DIR}/bin/pip install dvc
                    '''
                }
            }
        }

        stage('DVC Pull'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC pull....'
                        sh '''
                        export GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS
                        ${VENV_DIR}/bin/python -m pip install dvc
                        ${VENV_DIR}/bin/dvc pull
                        '''
                    }
                }
            }
        }


        stage('Building and Pushing Image to GCP'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Image to GCP...'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker us-central1-docker.pkg.dev --quiet
                        docker build -t us-central1-docker.pkg.dev/${GCP_PROJECT}/ml-project/ml-project:latest .
                        docker push us-central1-docker.pkg.dev/${GCP_PROJECT}/ml-project/ml-project:latest
                        '''
                    }
                }
            }
        }

        stage('Deployment to Kubernates'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Deployment to Kubernates...'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}:${KUBERCTL_AUTH_PLUGIN}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud container clusters get-credentials ml-app-cluster --region us-central1
                        kubectl apply -f deployment.yaml
                        '''
                    }
                }
            }
        }

    }
}