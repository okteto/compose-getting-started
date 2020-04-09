.PHONY: push
push:
	okteto build -t okteto/vote:stacks vote
