#!/usr/bin/python3
"""Creates and load the Storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
