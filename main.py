#!/usr/bin/env python
# coding: utf-8
import os
import warnings
import numerapi
import pandas as pd
import functions_framework
from numerapi import NumerAPI

numerai_public_id = os.environ["numerai_public_id"]
numerai_secret_key = os.environ["numerai_secret_key"]

@functions_framework.http
def main(request):
    # Download predictions
    os.system("mkdir -p ./nishi_crypto2")
    os.system("kaggle kernels output nishimoto/numerai-crypto-main-beta-prv -p ./nishi_crypto2")

    # Upload predictions
    napi = numerapi.CryptoAPI(numerai_public_id, numerai_secret_key)
    model_id = napi.get_models()["nishi_crypto1"]
    napi.upload_predictions("./nishi_crypto2/submission.csv", model_id=model_id)

    model_id = napi.get_models()["nishi_crypto2"]
    napi.upload_predictions("./nishi_crypto2/submission.csv", model_id=model_id)

    return "OK"
