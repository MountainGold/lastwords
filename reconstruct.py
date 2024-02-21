from sslib import shamir

if __name__ == '__main__':
    required_shares = int(input("Please tell me the number of shares required to recover the secret: "))
    shares = []
    prime_mod = input("Please tell me the prime modulus: ")
    for i in range(required_shares):
        shares.append(input(f"Please tell me share {i+1}: "))
    data = {'required_shares': required_shares, 'prime_mod': prime_mod, 'shares': shares}
    print(shamir.recover_secret(shamir.from_base64(data)).decode('ascii'))
