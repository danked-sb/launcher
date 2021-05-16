import requests, time

print('Welcome to Danked launcher.')
print('''Which mode would you like to use? Type safe or fast.''')
mode = input('> ')
if mode == 'fast':
    print('This is the fast version, so expect a ban/blacklist after a few hours.')
    print('Downloading the latest version from Github...')
    fastCode = requests.get('https://raw.githubusercontent.com/danked-sb/danked/main/fast.py').text
    fast_changelog = requests.get('https://github.com/danked-sb/danked/raw/main/fast_changelog.txt').text
    print('\n')
    print(f'''CHANGELOG: \n{fast_changelog}''')
    time.sleep(1)
    exec(fastCode)
elif mode == 'safe':
    print('Bans may still occur but it is much more stealthy.')
    print('Downloading the latest version from Github...')
    saferCode = requests.get('https://raw.githubusercontent.com/danked-sb/danked/main/safe.py').text
    safe_changelog = requests.get('https://github.com/danked-sb/danked/raw/main/safe_changelog.txt').text
    print('\n')
    print(f'''CHANGELOG: \n{safe_changelog}''')
    time.sleep(1)
    exec(saferCode)

