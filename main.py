import sys
import logging
import emoji
from custom_short_names import custom_short_names

# Setup logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

ahk_header = b"""#Requires AutoHotkey v2.0

#Hotstring EndChars :
#Hotstring O

"""

if __name__ == '__main__':
    underscore_only = '--underscore-only' in sys.argv
    if underscore_only:
        logger.info(f'Writing only underscore shortcodes')
    
    skip_update = '--skip-update' in sys.argv
    if not skip_update:
        emoji.update_if_not_latest(logger)

    emoji_data = emoji.get_emoji_data()
    emoji_short_names = dict((data[0], data) for data in emoji_data)

    # Add custom short codes
    for old, new in custom_short_names.items():
        emoji_short_names[new] = emoji_short_names[old]

    output = 'emoji.ahk'
    logger.info(f'📝 Writing to {output}')
    with open(output, 'wb') as f:
        f.write(ahk_header)
        for code, (_, emoji_string, name) in emoji_short_names.items():
            f.write(f"; {name or code.replace('_', ' ').upper()}\n".encode('utf-8'))  # Some emoji have no name field
            code = code[:39] # AHK hotstring limit is 40 chars
            f.write(f":::{code}::{emoji_string}\n".encode('utf-8')) 
            if '-' in code:
                code = code.replace('-', '_')
                f.write(f":::{code}::{emoji_string}\n".encode('utf-8')) 
            if '_' in code and not underscore_only:
                f.write(f":::{code.replace('_', ' ')}::{emoji_string}\n".encode('utf-8'))

    logger.info(f'✅ Done, {output} ready to use')
