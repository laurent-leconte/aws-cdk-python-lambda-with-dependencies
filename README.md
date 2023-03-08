# Deploying a Python Lambda with dependencies using AWS CDK

This is a template illustrating how to write and deploy a Lambda function which relies on external libraries.

## Requirements

In order to use this code, you must have Docker installed.

## How to use

### Set up CDK

In the root folder, create a virtual environment, activate it and install the infra dependencies.

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

### Write your code

Your application code should go in the `src` folder. You should treat this as the root folder for your code: in particular, this is where you should set up your project dependencies, using Poetry or pipenv.

### Update the infra stack

The infra configuration in `app.py` (and `infra/stack.py`) defines a simple Lambda function exposed through API Gateway. You probably will want to update this depending on your exact infrastructure configuration.

### Build and deploy

From the root folder, using the virtualenv you created in the first step, run:

```
$ cdk synth
$ cdk deploy
```

Voilà! Your Python Lambda and its dependencies are now deployed.
