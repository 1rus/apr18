node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
        pythonImage = docker.build('apr18:test')
    }
    stage('test'){
        pythonImage.inside {
    	sh '''. /tmp/venv/bin/activate && python -m pytest tests --junitxml=results.xml'''
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}
