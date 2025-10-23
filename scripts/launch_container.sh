source $( dirname ${BASH_SOURCE[0]} )/credentials.sh

docker run \
  -d \
  --shm-size=10g \
  --memory=120g \
  --cpus=16 \
  --user ${DOCKER_USER_ID}:${DOCKER_GROUP_ID} \
  --name ${CONTAINER_NAME} \
  --rm -it --init \
  -p 7860:7860 \
  ${DOCKER_NAME} 