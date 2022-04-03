import os
from werkzeug.utils import secure_filename
from email.policy import default
from wsgiref.validate import validator
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cv2
import numpy as np
from keras.preprocessing import image
from keras.applications.resnet import preprocess_input
import tensorflow as tf
from keras.models import load_model