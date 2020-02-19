# Getting Started on Okteto with Stacks

This example shows how to leverage [Okteto](https://github.com/okteto/okteto) to deploys the Voting App in Kubernetes using Okteto Stacks. 

<!-- This is the application used for the [How to Develop and Debug PHP Applications in Kubernetes](https://okteto.com/blog/how-to-develop-php-apps-in-kubernetes/) blog post. -->

The Voting App is a simple distributed application running across multiple containers. Containers are implemented using Python, Node.js and Java, with Redis for messaging and Postgres for storage.

![Architecture diagram](architecture.png)

* A front-end web app in [Python](/vote) which lets you vote between two options.
* A [Redis](https://hub.docker.com/_/redis/) queue which collects new votes.
* A [Java](/worker/src/main) worker which consumes votes and stores them in...
* A [Postgres](https://hub.docker.com/_/postgres/) database backed by a volume.
* A [Node.js](/result) webapp which shows the results of the voting in real time.


## Deploy the Voting App

```
okteto stack deploy
```

## Deploy the Voting App rebuilding containers

```
okteto stack deploy --build
```

## Destroy the Voting App

```
okteto stack destroy
```
