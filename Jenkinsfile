node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
        sh '''echo "Docker environment:" &&
        docker --version &&
        docker-compose --version'''
    }
    def COMPOSE_FILE_LOC="docker-compose.test.yml"
    def TEST_CONTAINER_NAME="apr18"
    defCOMPOSE_PROJECT_NAME_ORIGINAL="jenkinsbuild_${BUILD_TAG}"
    def COMPOSE_PROJECT_NAME=$(echo $COMPOSE_PROJECT_NAME_ORIGINAL | awk '{print tolower($0)}' | sed 's/[^a-z0-9]*//g')
    def TEST_CONTAINER_REF="${COMPOSE_PROJECT_NAME}_${TEST_CONTAINER_NAME}_1"

    stage('build docker image'){
        sh '''docker-compose -f $COMPOSE_FILE_LOC \
                   -p $COMPOSE_PROJECT_NAME \
                   down --remove-orphans &&
                   docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk '{print $1}' | xargs --no-run-if-empty docker stop &&
                    docker ps -a --no-trunc  | grep $COMPOSE_PROJECT_NAME \
                    | awk '{print $1}' | xargs --no-run-if-empty docker rm

    }
    stage('test'){
        
    	sh '''ls -la'''
        
    }
    stage('collect test results'){
    	sh '''ls -la'''

    }
}
