"""
    the functions for analysis docs
"""
from collections import defaultdict

def get_num_words(file_contents: str):
    num_words = len(file_contents.split())
    return num_words

def get_character_number(text: str):
    text = text.lower()
    character_num = defaultdict(int)
    for chr in text:
        character_num[chr] += 1
    return dict(character_num)

def sort_dict_by_wordnumber(d: dict):
    def sort_on(item):
        return item["num"]
    result = [{"char": key, "num": value} for key, value in d.items()]
    result.sort(reverse=True, key=sort_on)
    return result
    
    