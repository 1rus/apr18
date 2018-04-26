node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
        sh '''
        sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose &&
        sudo chmod +x /usr/local/bin/docker-compose &&
        echo "Docker environment:" &&
        docker --version &&
        docker-compose --version &&
        COMPOSE_FILE_LOC="docker-compose.test.yml" &&
        TEST_CONTAINER_NAME="apr18" &&
        COMPOSE_PROJECT_NAME_ORIGINAL="jenkinsbuild_${BUILD_TAG}" &&
        COMPOSE_PROJECT_NAME=$(echo $COMPOSE_PROJECT_NAME_ORIGINAL | awk '{print tolower($0)}' | sed 's/[^a-z0-9]*//g') &&
        TEST_CONTAINER_REF="${COMPOSE_PROJECT_NAME}_${TEST_CONTAINER_NAME}_1"
        '''
    }
    stage('build docker image'){
        sh '''docker-compose -f $COMPOSE_FILE_LOC \
                   -p $COMPOSE_PROJECT_NAME \
                   down --remove-orphans &&
                   docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk '{print $1}' | xargs --no-run-if-empty docker stop &&
                    docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk '{print $1}' | xargs --no-run-if-empty docker rm
            '''

    }
    stage('test'){
        
    	sh '''ls -la'''
        
    }
    stage('collect test results'){
    	sh '''ls -la'''

    }
}
