import argparse
import hashlib

def get_endpoint_secret_hash(endpoint_id, endpoint_secret, salt):
    # Calculates endpoint secret hash as SHA256(endpoint.secret, SHA256(endpoint.id_hex + salt))
    # salt is random string of length >= 1
    
    endpoint_id_hex = endpoint_id.encode('utf-8').hex()
    salted_endpoint_id = (endpoint_id_hex + salt).encode('utf-8')
    endpoint_id_hash = hashlib.sha256(salted_endpoint_id).hexdigest()
    salted_enpoint_secret = (endpoint_secret + endpoint_id_hash).encode('utf-8')
    
    return hashlib.sha256(salted_enpoint_secret).hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate endpoint secret hash')
    parser.add_argument('endpoint_id', type=str, help='ID of endpoint')
    parser.add_argument('endpoint_secret', type=str, help='Secret of endpoint')
    parser.add_argument('salt', type=str, help='Salt to use')
    args = parser.parse_args()

    endpoint_secret_hash = get_endpoint_secret_hash(args.endpoint_id, args.endpoint_secret, args.salt)
    print(endpoint_secret_hash)

