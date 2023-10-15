#!/usr/bin/python3
"""Module for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review representation"""
    place_id = ""
    user_id = ""
    text = ""
