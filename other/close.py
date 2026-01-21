#!/usr/bin/env python
from hashlib import blake2b
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from json import loads as json_loads, dumps as json_dumps, JSONDecodeError

def fetch_and_parse_json(url):
    try:
        # Send GET request using urllib
        with urlopen(url, timeout=10) as response:
            # Read the response body
            data = response.read().decode('utf-8')

            # Parse JSON
            parsed_data = json_loads(data)

            # Print or process the data
            print("✅ Successfully fetched and parsed JSON:")
            print(parsed_data)

            return parsed_data

    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    except JSONDecodeError as e:
        print(f"Invalid JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def hash_traits(key, traits):
    """
    Hashes each trait using BLAKE2b with the given key.
    Returns a JSON array of 128-character lowercase hex digests.

    Args:
        key (str): The key to use for hashing (UTF-8 encoded).
        traits (list of str): List of traits to hash.

    Returns:
        str: JSON-formatted array of hex digests.
    """
    key_bytes = key.encode('utf-8')
    hashes = []

    for trait in traits:
        hasher = blake2b(digest_size=64, key=key_bytes)
        hasher.update(trait.encode('utf-8'))
        digest_hex = hasher.hexdigest().lower()
        hashes.append(digest_hex)

    #return hashes
    return json_dumps(hashes, separators=(',', ':'))

def post_traits_to_close_api_urllib(url, traits, api_key=None):
    """
    POSTs a JSON array of traits to the Close API using urllib.

    Args:
        url (str): The API endpoint URL (e.g., "https://api.close.com/buildwithus/").
        traits (list of str): List of traits to send (e.g., ['a', 'b']).
        api_key (str, optional): If required by the API, provide your API key here.

    Returns:
        dict: Response JSON if successful, otherwise raises an exception.
    """
    # Prepare the JSON payload
    payload = json_dumps(traits, separators=(',', ':')).encode('utf-8')

    # Build headers
    headers = {
        "Content-Type": "application/json",
    }

    # Optional: Add API key if required
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    # Create request
    print(traits)
    req = Request(url, data=traits.encode('utf-8'), method="POST")

    # Add headers to the request
    for key, value in headers.items():
        req.add_header(key, value)

    try:
        with urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print(response_data)
            return json_loads(response_data)
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        print(f"Response body: {e.read().decode('utf-8')}")
        raise
    except JSONDecodeError as e:
        print(f"json decoding error {url}: {e}")
    except Exception as e:
        print(f"Error posting to {url}: {e}")
        raise

if __name__ == '__main__':
    url = "https://api.close.com/buildwithus/"
    #data = fetch_and_parse_json(url)
    data = {'traits': ['Craftsman', 'Pragmatic', 'Curious', 'Methodical', 'Driven', 'Collaborator'], 'key': 'Close-0901c1ad', 'meta': {'description': 'Enclosed are some traits that [Joe](https://www.linkedin.com/in/jkemp101/) believes great engineers exhibit. Using the included UTF-8 `key`, construct a JSON array using the lowercase hex digest of the blake2b hash for each trait (digest size=64). POST this bare array back to this endpoint. Example array: ["1f9ec19c7...57fd27e5", "79c72b47088...bf13026c", ...] If the hashes are correct you will get a Verification ID you should include in your application. 400 responses indicate a problem with the hashes in your array. Note, the key rotates each day around midnight EST.'}}
    result = hash_traits(data['key'], data['traits'])
    fin = post_traits_to_close_api_urllib(url, result)

