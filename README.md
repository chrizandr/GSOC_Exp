# HydraExp

A small repo for understanding the Hydra to PSQL connection and how Python objects can be stored and deleted in it.

## How to build and run the docker nginx server

1. Build the docker container using `docker build -t hydraexp .`

2. Run the docker container using `docker run -v <app folder full path>:/app -p <port>:80 hydraexp`

  ### Sample command `docker run -v ~/workspace/gsoc/hydraenv/HydraExp/app:/app -p <port>:80 hydraexp`

3. The server should be up and running at `http://127.0.0.1:<port>`.

4. Now you can simple edit the contents of `app/` and the all you need to do is restart the server using #2

## Api entrypoint

`/api`
