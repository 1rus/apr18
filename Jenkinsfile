node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
       
    }
    stage('docker-compose up'){
        sh '''
            docker-compose -d up
           '''

    }
    stage('test'){
        
    	sh '''ls -la'''
        
    }
    stage('docker-compose down'){
    	sh '''
        docker-compose down
        '''

    }
}