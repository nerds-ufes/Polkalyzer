from lib.polka import modified_create_list_irrpoly_mod2
import hashlib
import json
import toml
from pathlib import Path
from lib.utils import installBehavioralModel

def load_hashes_from_file(path):
    try:
        with open(path, 'r') as f:
            return toml.load(f)
    except (FileNotFoundError, toml.TomlDecodeError):
        return {}

def load_cache_from_file(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

cache_file = Path('lib/.polkalyzer_cache.json')
hash_file = 'hashes.toml'

hashes = load_hashes_from_file(hash_file)
caches = load_cache_from_file(cache_file)

installBehavioralModel() # If not installed, install behavioral model

def is_cached(keys: list):
    if not compare_hash(keys):
        return False # Cache not saved
    return True # Already on cache

# If not cached yet, save the hash of the file in hashes.toml
def is_file_cached(keys: list, path: Path):
    # A partir do path, crie um objeto Path
    if path.exists() and not compare_file_hash(keys,path): #Path exist and hash not saved
        hash = calculate_file_hash(path)
        file_save_hash_to_file(keys, hash)
        print(f'Cache saved for {keys} with hash {hash}')
        return False # Not already saved
    elif not path.exists(): # Path not exist
        return False
    else:
        return True # Already saved


def save_if_not_cached(keys: list, value):
    if not is_cached(keys):
        save_cache_to_file(keys, value)
        hash = calculate_dict_hash(value)
        save_hash_to_file(keys, hash)
        print(f'Cache saved for {keys} with hash {hash}')
        return True # Saved
    return False # Not saved

# Given a keys, return the value from the last key on list
def get_keys_value(keys: list, dictionary: dict):
    current_dict = dictionary
    if(current_dict != {}): #Verify if the dictionary is empty
        for key in keys:
            try:
                current_dict = current_dict[key]
            except KeyError:
                print(f'Key {key} not found on cache')
                return {}
    return current_dict

def get_nodesID_CRC16():
    cache = caches
    keys = ['nodesID', 'crc16']

    if not is_cached(keys):
        nodesID_CRC16 = modified_create_list_irrpoly_mod2(15)
        save_cache_to_file(keys, nodesID_CRC16)
        save_hash_to_file(keys, calculate_dict_hash(nodesID_CRC16))
        return nodesID_CRC16
    
    return get_keys_value(keys, cache)

# def calculate_file_hash(path: Path):
#     with open(path, 'rb') as f:
#         image = f.read()
#         return hashlib.md5(image).hexdigest()

def calculate_file_hash(path: Path):
    hash_md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def calculate_dict_hash(data):
    json_data = json.dumps(data, sort_keys=True)
    hash_value = hashlib.md5(json_data.encode()).hexdigest()
    return hash_value

# Given a array of keys (keys and subkeys and subsubkeys ...) and a value, save it into a toml file called hashes.toml
def save_hash_to_file(keys: list, val):
    global hashes
    current_dict = hashes
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    current_dict[keys[-1]] = val

def file_save_hash_to_file(keys: list, val):
    global hashes
    current_dict = hashes
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    # If key doesn't exist, create it with a empty list
    if keys[-1] not in current_dict:
        current_dict[keys[-1]] = []
    current_dict[keys[-1]].append(val)

def save_cache_to_file(keys: list, val):
    global caches
    current_dict = caches
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    current_dict[keys[-1]] = val

# Given key, compare the value from the .polkalyzer_cache.json file, calculate its hash and compare it with hash on hashes.toml to this key
def compare_hash(keys: list):
    global hashes, caches
    hash_dict = hashes
    json_dict = caches

    if(json_dict == {}): #Verify if the dictionary is empty
        return False

    current_hash = calculate_dict_hash(get_keys_value(keys, json_dict))

    for key in keys[:-1]:
        hash_dict = hash_dict.setdefault(key, {})
        json_dict = json_dict.setdefault(key, {})
    
    if keys[-1] in hash_dict and hash_dict[keys[-1]] == current_hash:
        return True
    return False

def compare_file_hash(keys: list, path: Path):
    global hashes
    hash_dict = hashes
    file_hash = calculate_file_hash(path)

    for key in keys[:-1]:
        hash_dict = hash_dict.setdefault(key, {})
    
    if keys[-1] in hash_dict and file_hash in hash_dict[keys[-1]]:
        # print('Hash already saved')
        return True
    return False

def export_cache():
    global hashes, caches

    with open(hash_file, 'w') as f:
        toml.dump(hashes, f)
    with open(cache_file, 'w') as f:
        json.dump(caches, f)
