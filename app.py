from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import sqlite3
import random
from difflib import SequenceMatcher
from typing import Dict, List
import re
# from pydentic import BaseModel

app = FastAPI(title="English Trainer")

#Подключаем статику и шаблоны
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
  """Главная страница"""
  return templates.TemplateResponse("index.html", {"request": request})