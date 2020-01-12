pipeline{
        agent any
        
        stages{
		stage('--Build Docker--'){
			steps{
				sh '''. ~/.bashrc
				      docker-compose build
				      docker-compose push
				      '''
			}
		}
                stage('--Deploy Docker--'){
                        steps{
				sh '''ssh myapp  << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      docker service update --replicas "3" --image jenkins:5000/service1:build-${BUILD_NUMBER} project_service1
				      docker service update --replicas "3" --image jenkins:5000/cards:build-${BUILD_NUMBER} project_cards
				      docker service update --replicas "3" --image jenkins:5000/crystals:build-${BUILD_NUMBER} project_crystals
				      docker service update --replicas "3" --image jenkins:5000/readings:build-${BUILD_NUMBER} project_readings
                                      '''
                        }
                }
        }
}
