### docker build
docker build -t flask-controller:v1 .

docker login

docker tag flask-controller:v1 hoainamtran204/flask-controller:v1

docker push hoainamtran204/flask-controller:v1

docker run -td flask-controller:v1

docker exec -it containerid sh


docker tag docker-new-build:latest dockerhub-username/name-of-repo:latest
docker push image-name:version-name
docker run -td imageid

### key create
openssl genrsa -out dev-nam.key 2048
openssl req -new -key dev-nam.key -out dev-nam.csr -subj "/CN=nam"

create dev-nam-csr.yaml file 
https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

request is the base64 encoded value of the CSR file content. You can get the content using this command:
cat dev-nam.csr | base64 | tr -d "\n"

kubectl apply -f dev-nam-csr.yaml

kubectl get csr

kubectl certificate approve dev-nam

kubectl get csr dev-nam -o yaml

kubectl get csr dev-nam -o jsonpath='{.status.certificate}'| base64 -d > dev-nam.crt

echo ‘’ | base64 — decode > dev-nam.crt


### kubernetes
kubectl apply -f controller_deployment.yaml
kubectl apply -f controller_service.yaml
kubectl apply -f mutating_admission_webhook.yaml

kubectl delete -f controller_deployment.yaml
kubectl delete -f controller_service.yaml
kubectl delete -f mutating_admission_webhook.yaml


### git 
git init
git add .
git commit -m "Window runner check"
git branch -M main
git remote add origin https://github.com/namtranvn/flask-controller.git
git push -u origin main

git push --set-upstream origin master

ngrok http 443 

if [ -f requirements.txt ]; then pip install -r requirements.txt; fi