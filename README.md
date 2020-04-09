# Getting Started on Okteto Cloud with Stacks

This example shows how to leverage [Okteto](https://github.com/okteto/okteto) to deploys the Voting App on Okteto Cloud using [Stacks](https://okteto.com/docs/cloud/stacks). 

The Voting App is a simple web application implemented using Python, with Redis for storage.

## Deploy the Voting App

```console
$ okteto stack deploy
```

## Deploy the Voting App rebuilding containers

```console
$ okteto stack deploy --build
```

## Destroy the Voting App

```console
$ okteto stack destroy
```
