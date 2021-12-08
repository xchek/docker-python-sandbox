### Docker python example usage:

Drop into python3 interpreter running in container:
`docker run -it python:3`

Builds images from `Dockerfile` in $CWD:
`docker build -t IMAGE_NAME .`

Run IMAGE_NAME in container CONTAINER_NAME. [(Clean-up --rm)](https://docs.docker.com/engine/reference/run/#clean-up---rm)
`docker run -it --rm --name CONTAINER_NAME IMAGE_NAME`

Run python script in interactive mode (drops into interpreter):
`docker run -it IMAGE_NAME python -i ./main.py`

Run command `python` in running container:
`docker exec -it CONTAINER_NAME/CONTAINER_ID python`

List all containers:
`docker ps -a`

Inspect container metadata:
`docker container inspect CONTAINER_NAME`

(Could be dangerous) Removes all containers (-f force, -v delete volumes, -q quiet-print ids only):
docker rm -fv $(docker ps -aq)

### Useful links:
https://docs.docker.com/engine/reference/build/
https://docs.docker.com/engine/reference/exec/
https://docs.docker.com/engine/reference/run/


### Random free APIs:
https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
