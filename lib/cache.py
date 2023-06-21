from lib.polka import modified_create_list_irrpoly_mod2
import hashlib
import json
import toml

def get_nodesID_CRC16():
    cache_file = 'lib/.polkalyzer_cache.json'
    cache = load_cache_from_file(cache_file)
    key = 'nodesID_CRC16'

    if key not in cache or not compare_hash(key):
        nodesID_CRC16 = modified_create_list_irrpoly_mod2(16)
        cache[key] = nodesID_CRC16
        save_cache_to_file(key, nodesID_CRC16)
        save_hash_to_file(key, calculate_dict_hash(nodesID_CRC16))

    return cache[key]

def calculate_hash(value):
    return hashlib.md5(value.encode()).hexdigest()

def calculate_dict_hash(data):
    json_data = json.dumps(data, sort_keys=True)
    hash_value = hashlib.md5(json_data.encode()).hexdigest()
    return hash_value

def load_hashes_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return toml.load(f)
    except (FileNotFoundError, toml.TomlDecodeError):
        return {}

def load_cache_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Given a key name and a value, save it into a toml file called hashes.toml
def save_hash_to_file(key, value):
    hash_file = 'hashes.toml'
    hashes = load_hashes_from_file(hash_file)
    hashes[key] = value
    with open(hash_file, 'w') as f:
        toml.dump(hashes, f)

# Given a key and a value, save it into a json file called .polkalyzer_cache.json
def save_cache_to_file(key, value):
    cache_file = 'lib/.polkalyzer_cache.json'
    cache = load_cache_from_file(cache_file)
    cache[key] = value
    with open(cache_file, 'w') as f:
        json.dump(cache, f)

# Given key, compare the value from the .polkalyzer_cache.json file, calculate its hash and compare it with hash on hashes.toml to this key
def compare_hash(key):
    hash_file = 'hashes.toml'
    cache_file = 'lib/.polkalyzer_cache.json'
    current_hash = calculate_dict_hash(load_cache_from_file(cache_file)[key])
    hashes = load_hashes_from_file(hash_file)
    if key in hashes and hashes[key] == current_hash:
        return True
    return False
