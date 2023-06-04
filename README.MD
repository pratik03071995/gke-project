
https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image#python

step - 1 -
gcloud artifacts repositories create health-repo \
    --project=meta-spirit-382121 \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository"

step - 2 -
gcloud builds submit \
  --tag us-central1-docker.pkg.dev/meta-spirit-382121/health-repo/my_flask_app .

step - 3 -
kubectl apply -f deployment.yaml

step - 4 -
kubectl get deployments

step - 5 -
kubectl get pods

step - 6 -
kubectl apply -f service.yaml

step - 7 -
kubectl get services


