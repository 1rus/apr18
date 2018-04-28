node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
       
    }
    stage('docker-compose up'){
        sh """
        docker-compose --version
        docker-compose -p APR18 up --build
        """

    }
    stage('test'){
        
    	sh """
        docker-compose run apr18 . /tmp/venv/bin/activate
        docker-compose run apr18 python -m pytest frame-test --junitxml=results.xml
        """
        
    }
    stage('docker-compose down'){
    	sh """
        junit 'results.xml'
        docker-compose down
        """

    }
}