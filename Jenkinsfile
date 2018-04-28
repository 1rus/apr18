node ('master') {
    cleanWs()
    withEnv(['$DOCKER_COMPOSE=/usr/local']){
    stage('checkout scm'){
        checkout scm
       
    }
    stage('docker-compose up'){
        sh """
        #!/bin/bash -l
        printenv 
        echo $PATH 
        $DOCKER_COMPOSE/docker-compose --version
        """

    }
    stage('test'){
        
    	sh """
        ls -la
        """
        
    }
    stage('docker-compose down'){
    	sh """
        $DOCKER_COMPOSE/docker-compose down
        """

    }
    }
}