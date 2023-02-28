#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infra.stack import EchoServiceStack


app = cdk.App()
EchoServiceStack(app, "EchoServiceStack")

app.synth()
