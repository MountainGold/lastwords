from sslib import shamir

if __name__ == '__main__':
    distributed_shares = int(input("Please tell me how many shares you want to generate: "))
    required_shares = int(input("Please tell me the minimum number of shares required to recover the secret: "))
    secret = input("Please tell me the secret: ")

    print(shamir.to_base64(shamir.split_secret(secret.encode('ascii'), required_shares, distributed_shares)))
