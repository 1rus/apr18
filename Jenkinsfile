node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
       
    }
    stage('docker-compose up'){
        sh """
        #!/bin/bash -e
        printenv 
        echo $PATH 
        docker-compose --version
        """

    }
    stage('test'){
        
    	sh """
        ls -la
        """
        
    }
    stage('docker-compose down'){
    	sh """
        docker-compose down
        """


    }
}