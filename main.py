import firebase_admin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from firebase_admin import credentials
from firebase_admin import firestore
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD

torch.set_default_device('cpu')

# Initialize Firebase
cred = credentials.Certificate('adminkey.json')  # Replace with your Firebase credentials
firebase_admin.initialize_app(cred)
db = firestore.client()


