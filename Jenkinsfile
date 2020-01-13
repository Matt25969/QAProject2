pipeline{
        agent any
        
        stages{
		stage('--Build Docker--'){
			steps{
				sh '''. ~/.bashrc
				      docker-compose build
				      '''
			}
		}
                stage('--Deploy Docker--'){
                        steps{
				sh '''ssh 10.154.0.4 << EOF
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      docker service update --replicas "3" --image jenkins:5000/service1:build-${BUILD_NUMBER} qaproject2_service1_1
				      docker service update --replicas "3" --image jenkins:5000/cards:build-${BUILD_NUMBER} qaproject2_cards_1
				      docker service update --replicas "3" --image jenkins:5000/crystals:build-${BUILD_NUMBER} qaproject2_crystals_1
				      docker service update --replicas "3" --image jenkins:5000/readings:build-${BUILD_NUMBER} qaproject2_readings_1
                                      '''
                        }
                }
        }
}
