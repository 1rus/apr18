node ('master') {
 withEnv(['DOCKER_COMPOSE=/usr/local/bin']){
    cleanWs()
    stage('checkout scm'){
        checkout scm
        sh 'echo "Docker environment:"'
        sh 'docker --version'
        sh '$DOCKER_COMPOSE/docker-compose --version'
        sh'''
            COMPOSE_FILE_LOC="docker-compose.test.yml"
            TEST_CONTAINER_NAME="apr18"
            COMPOSE_PROJECT_NAME_ORIGINAL="jenkinsbuild_${BUILD_TAG}"
            COMPOSE_PROJECT_NAME=$(echo $COMPOSE_PROJECT_NAME_ORIGINAL | awk '{print tolower($0)}' | sed 's/[^a-z0-9]*//g')
            TEST_CONTAINER_REF="${COMPOSE_PROJECT_NAME}_${TEST_CONTAINER_NAME}_1"
            '''
    }
    stage('build docker image'){
        sh '''
            $DOCKER_COMPOSE/docker-compose -f $COMPOSE_FILE_LOC \
                   -p $COMPOSE_PROJECT_NAME \
                   down --remove-orphans &&
                   docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk "{print $1}" | xargs --no-run-if-empty docker stop &&
                    docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk "{print $1}" | xargs --no-run-if-empty docker rm
            '''

    }
    stage('test'){
        
    	sh '''ls -la'''
        
    }
    stage('collect test results'){
    	sh '''ls -la'''

    }
    }
}