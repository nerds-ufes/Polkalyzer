from lib.polka import modified_create_list_irrpoly_mod2
import hashlib
import json
import toml

cache_file = 'lib/.polkalyzer_cache.json'
hash_file = 'hashes.toml'

def is_cached(keys: list):
    if not compare_hash(keys):
        print('Cache hit')
        return False
    print('Cache miss')
    return True

def is_file_cached(keys: list, filename: str):
    hash = calculate_file_hash(filename)
    if not is_cached(keys):
        save_hash_to_file(keys, hash)
        print(f'Cache saved for {keys} with hash {hash}')
        return False # Not already saved
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
    for key in keys:
        current_dict = current_dict[key]
    return current_dict

def get_nodesID_CRC16():
    cache = load_cache_from_file(cache_file)
    keys = ['nodesID', 'crc16']

    if not is_cached(keys):
        nodesID_CRC16 = modified_create_list_irrpoly_mod2(16)
        save_cache_to_file(keys, nodesID_CRC16)
        save_hash_to_file(keys, calculate_dict_hash(nodesID_CRC16))
        return nodesID_CRC16
    
    return get_keys_value(keys, cache)

def calculate_file_hash(filename):
    with open(filename, 'r') as f:
        return calculate_dict_hash(json.load(f))

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

# Given a array of keys (keys and subkeys and subsubkeys ...) and a value, save it into a toml file called hashes.toml
def save_hash_to_file(keys: list, val):
    hashes = load_hashes_from_file(hash_file)


    current_dict = hashes
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    current_dict[keys[-1]] = val

    with open(hash_file, 'w') as f:
        toml.dump(hashes, f)

    # save_hashes_to_file(hash_file, field, hashes)

# def save_hashes_to_file(filename, field, values):
#     data = {field: values}
#     with open(filename, 'w') as f:
#         toml.dump(data, f)

# Given a array of keys (keys and subkeys and subsubkeys ...) and a value, save it into a toml file called hashes.toml
def save_cache_to_file(keys: list, val):
    caches = load_cache_from_file(cache_file)

    current_dict = caches
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    current_dict[keys[-1]] = val

    with open(cache_file, 'w') as f:
        json.dump(caches, f)

    # save_caches_to_file(cache_file, caches)

def save_caches_to_file(filename, field, values):
    data = {field: values}
    with open(filename, 'w') as f:
        json.dump(data, f)

# # Given a key and a value, save it into a json file called .polkalyzer_cache.json
# def save_cache_to_file(key, value):
#     cache = load_cache_from_file(cache_file)
#     cache[key] = value
#     with open(cache_file, 'w') as f:
#         json.dump(cache, f)

# Given key, compare the value from the .polkalyzer_cache.json file, calculate its hash and compare it with hash on hashes.toml to this key

def compare_hash(keys: list):
    current_hash = calculate_dict_hash(get_keys_value(keys, load_cache_from_file(cache_file)))

    hash_dict = load_hashes_from_file(hash_file)
    json_dict = load_cache_from_file(cache_file)
    for key in keys[:-1]:
        hash_dict = hash_dict.setdefault(key, {})
        json_dict = json_dict.setdefault(key, {})
    
    # return hash_dict[keys[-1]] == json_dict[keys[-1]]
    if keys[-1] in hash_dict and hash_dict[keys[-1]] == current_hash:
        return True
    return False

    # if key in hashes and hashes[key] == current_hash:
    #     return True
    # return False
