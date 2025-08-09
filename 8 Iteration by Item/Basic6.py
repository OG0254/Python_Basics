# Real world usage of iterations

emails = ['john@example.com', 'ken@example.com', 'mary@gmail.com']
for email in emails:
    if email.endswith('@gmail.com'):
        print(f'Sending offer to: {email}')
