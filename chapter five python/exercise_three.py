def slicing (alphabet):
    result_a = alphabet[0:14:1]
    result_b = alphabet[:14]
    result_c = alphabet[13:27:1]
    result_d = alphabet[13::1]
    result_e = alphabet[26::1]
    result_f = alphabet[:27:2]
    result_g = alphabet[26::-3]

    return result_a, result_b, result_c, result_d, result_e, result_f, result_g

alphbet = 'abcdefghijklmnopqrstuwxyz'

print(slicing(alphbet))
