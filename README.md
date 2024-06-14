### docker build
docker build -t flask-controller100:v1 .
docker login
docker tag flask-controller100:v1 hoainamtran204/flask-controller100:v1
docker push hoainamtran204/flask-controller100:v1

docker run -td flask-controller:v1
docker exec -it containerid sh


docker tag docker-new-build:latest dockerhub-username/name-of-repo:latest
docker push image-name:version-name
docker run -td imageid

### git 
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/namtranvn/gitlab-ci-test.git
git push --set-upstream origin master