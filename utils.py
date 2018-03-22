import hashlib


def is_power_of_two(n):
    """Check whether `n` is an exponent of two

    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(3)
    False
    >>> if_power_of_two(16)
    True
    """
    return n != 0 and ((n & (n - 1)) == 0)

def hash_data(data, hash_function='sha256'):
    """One-way function, takes various standard algorithm names as
    `hash_function` input and uses it to hash string `data`. The default
    algorithm is 'sha256'. Even small changes in `data` input cause
    significant changes to the output

    >>> example = 'hello'
    >>> hash_data(example)
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    >>> hash_data(example, 'sha1')
    'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    >>> example = 'hello!'
    >>> hash_data(example)
    'ce06092fb948d9ffac7d1a376e404b26b7575bcc11ee05a4615fef4fec3a308b'
    """
    hash_function = getattr(hashlib, hash_function)
    data = data.encode('utf-8')
    return hash_function(data).hexdigest()

def concat_and_hash_list(lst, hash_function='sha256'):
    """Helper function for quickly concatenate pairs of values and hash them.
    The process is repeated until one value is returned: the final hash.
    Assumes that the length of the `lst` is an exponent of two

    >>> concat_and_hash_list(['a', 'b'])
    'fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603'
    """
    assert len(lst) >= 2, "No transactions to be hashed"
    while len(lst) > 1:
        a = lst.pop(0)
        b = lst.pop(0)
        lst.append(hash_data(a + b, hash_function))
    return lst[0]
