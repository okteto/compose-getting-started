# Getting Started with Okteto Stacks

This example shows how to leverage [Okteto](https://github.com/okteto/okteto) to develop an application using [Stacks](hhttps://okteto.com/docs/cloud/stacks#manifest-reference). Stacks are designed for developers that don't want to deal with the complexities of Kubernetes manifests.

## Prerequisites

- Install the Okteto CLI. Follow this [guide](https://okteto.com/docs/getting-started/installation) if you haven't done it yet.
- Access to a Kubernetes Cluster. You can also give [Okteto Cloud](https://okteto.com/) a try. Okteto Cloud is a development platform for Kubernetes applications. Free developer accounts come with 4GB of RAM, 2 CPUs, and 5GB Disk space.

## Deploy the Sample App

Get a local version of the Sample App by executing the following commands in your local terminal:

```console
$ git clone https://github.com/okteto/stacks-getting-started
$ cd stacks-getting-started
```

The Sample App is a simple web application implemented using Python, with Redis for storage. 
The `okteto-stack.yml` file contains the [Stack manifest](https://okteto.com/docs/cloud/stacks#manifest-reference) of the Sample App.
Deploy the Sample App by executing:


```console
$ okteto stack deploy --wait
```

```console
✓  Successfully deployed stack 'voting-app'
```

Check that all pods are ready by executing the command below:

```console
$ kubectl get pod
```

```console
NAME                           READY   STATUS    RESTARTS   AGE
redis-0                        1/1     Running   0          34s
vote-6f4b7f5756-4dr72          1/1     Running   0          35s
vote-6f4b7f5756-x6k7d          1/1     Running   0          35s
```

## Activate your development environment

Use `okteto up` to synchronize your local changes with your application by executing the following command:

```console
$ okteto up -f vote/okteto.yml
```

```console
✓  Development environment activated
✓  Files synchronized
   Namespace: pchico83
   Name:      vote
   Forward:   8080 -> 8080

* Serving Flask app "app" (lazy loading)
* Environment: development
* Debug mode: on
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 279-349-987
```

From this moment, every change you do from your local IDE will be immediately hot reloaded by your application running on Kubernetes:

```console
* Detected change in '/src/app.py', reloading
* Restarting with stat
* Debugger is active!
* Debugger PIN: 167-523-127
```

## Redeploy the Voting App

When you are done with your code changes, you can rebuild and redeploy your application by executing the following command:

```console
$ okteto stack deploy --build
```

```console
i  Running your build in Okteto Cloud...
i  Building image for service 'vote'...
[+] Building 4.2s (13/13) FINISHED                                                                                                                              
=> importing cache manifest from registry.cloud.okteto.net/pchico83/   vote:okteto                                      1.0s
=> [internal] load build definition from buildkit-630371997                                                             0.4s
=> => transferring dockerfile: 524B                                                                                     0.4s
=> [internal] load .dockerignore                                                                                        0.3s
=> => transferring context: 2B                                                                                          0.3s
=> [internal] load metadata for docker.io/library/python:3-slim                                                         0.7s
=> [internal] load build context                                                                                        0.6s
=> => transferring context: 6.04kB                                                                                      0.6s
=> [1/6] FROM docker.io/library/python:3-slim@sha256:c0281d8fe99edff517fcc748f088bc51822ae660bac9e4aba76a81fa987fe9e8   0.0s
=> => resolve docker.io/library/python:3-slim@sha256:c0281d8fe99edff517fcc748f088bc51822ae660bac9e4aba76a81fa987fe9e8   0.0s
=> CACHED [2/6] WORKDIR /src                                                                                            0.0s
=> CACHED [3/6] RUN pip install --upgrade pip                                                                           0.0s
=> CACHED [4/6] ADD requirements.txt requirements.txt                                                                   0.0s
=> CACHED [5/6] RUN pip install -r requirements.txt                                                                     0.0s
=> CACHED [6/6] ADD . /src                                                                                              0.0s
=> exporting to image                                                                                                   1.8s
=> => exporting layers                                                                                                  0.0s
=> => exporting manifest sha256:23567b4fef520ef1fb356cacad163e019c06c5942a991fc76f12f0cbab7b3b3a                        0.0s
=> => exporting config sha256:a424f508b9602ec44193c2c6408107d4d4c8f7f7eb71828c884a2c6feb574ea6                          0.0s
=> => pushing layers                                                                                                    1.1s
=> => pushing manifest for registry.cloud.okteto.net/pchico83/vote:okteto                                               0.6s
=> exporting cache                                                                                                      0.2s
=> => preparing build cache for export                                                                                  0.2s
✓  Image for service 'vote' successfully pushed
✓  Successfully deployed stack 'voting-app'
```

## Destroy the Voting App

Execute the command below to destroy the application from your Kubernetes cluster:

```console
$ okteto stack destroy
```

```console
✓ Successfully destroyed stack 'voting-app'
```
