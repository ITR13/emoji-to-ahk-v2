import urllib.request
import re
import os.path
import json


def update_if_not_latest(logger):
    emoji_version_path = 'emoji.json.version'
    emoji_path = 'emoji.json'

    current_version = ''
    if os.path.isfile(emoji_version_path) and os.path.isfile(emoji_path):
        with open(emoji_version_path) as f:
            current_version = f.read().strip()
    
    latest = get_greatest_version()

    if latest != current_version:
        update_to(logger, latest)
    else:
        logger.info(f'Using cached emoji-data {latest}')

def get_greatest_version():
    url = 'https://github.com/iamcal/emoji-data/tags'
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
    
    # Look for the tag titles
    tags = re.findall(r'class="Link--primary Link">(v(\d+)\.(\d+)\.(\d+))</a>', html)
    max_tag = max(tags, key=lambda tag: tuple(map(int, tag[1:])))
    return max_tag[0].strip()

def update_to(logger, tag):
    url = f'https://raw.githubusercontent.com/iamcal/emoji-data/refs/tags/{tag}/emoji.json'
    logger.info(f'📝 Downloading emoji-data {tag}')

    with urllib.request.urlopen(url) as response:
        if response.getcode() != 200:
            logger.error(f'❌ Failed to download emoji.json')
            return

        with open('emoji.json', 'wb') as f:
            f.write(response.read())
        with open('emoji.json.version', 'w') as f:
            f.write(tag)
        
        logger.info(f'✅ Finished downloading emoji.json')

def convert_unified_to_emoji(unified):
    characters = [chr(int(hex, 16)) for hex in unified.split('-')]
    return ''.join(characters)

def get_emoji_data():
    with open('emoji.json', encoding='utf-8') as f:
        emojis = json.load(f)

    return (
        (
            short_name,
            convert_unified_to_emoji(emoji['unified']),
            emoji.get('name', '')
        )
        for emoji in emojis
        for short_name in emoji['short_names']
    )

def validate_emoji_data():
    with open('emoji.json', encoding='utf-8') as f:
        emojis = json.load(f)

    any_failed = False
    for emoji in emojis:
        short_name = emoji['short_name']
        if short_name not in emoji['short_names']:
            name = emoji['name']
            print(f'Emoji {name} is missing short code {short_name}')
            any_failed = True

    if not any_failed:
        print("Successfully validated emoji.json")

if __name__ == '__main__':
    validate_emoji_data()