import hashlib

def crack_sha1_hash(hash, use_salts = False):

    with open('top-10000-passwords.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if use_salts:
                with open('known-salts.txt', 'r') as salts:
                    for salt in salts:
                        salt = salt.strip()
                        line_with_salt_1 = f'{salt}{line}'
                        line_with_salt_2 = f'{line}{salt}'
                        is_current_true_1 = is_pass_hash(line_with_salt_1, hash)
                        is_current_true_2 = is_pass_hash(line_with_salt_2, hash)
                        if is_current_true_1 or is_current_true_2:
                            return line
            else:
                is_current_true = is_pass_hash(line, hash)
                if is_current_true:
                    return line
    return 'PASSWORD NOT IN DATABASE'

def is_pass_hash(current_pass, hash):
    m = hashlib.sha1()
    m.update(current_pass.encode('utf-8'))
    current_hash = m.hexdigest()
    if current_hash == hash:
        return True
    else:
        return False
