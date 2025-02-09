# Emoji to AHK

**This is a fork!**: This is a fork of [alexmick's emoji-to-ahk](https://github.com/alexmick/emoji-to-ahk/) that generates an autohotkey v2 script instead!

This is an Autohotkey script to automatically replace your emoji from their shortnames.
Like in Slack but anywhere on your windows machine.

You type `:smiley:` anywhere and it gets replaced by 😃 without you noticing !

The full list of supported emoji can be found here : https://projects.iamcal.com/emoji-data/table.htm

**Note**: All emoji with underscores like `:raised_hands:` are also available with spaces
as `:raised hands:` for easier typing.

## ⏬ Download

The emoji `.ahk` script as well as an `.exe` version can be found in the [releases](https://github.com/ITR13/emoji-to-ahk-v2/releases)
section.

## 👷 Build

The python tool creates a [Autohotkey](https://autohotkey.com)
script with a hotstring for every emoji with a short name.

### 🗜 Installing

This tools uses only builtin libraries from python 3.3+, so no additional installation needed.

### 🔧 Customising

If you edit the `custom_short_names.py` list in the format `'old_name':'new_name'`
you can add any number of custom short name aliases to your generated script.
Feel free to submit a PR if you want to share your custom aliases.

### 🏃 Running

Run :
```
python main.py
```

You can add `--underscore-only` to skip generation of `:raised hands:`
expansion (space instead of underscore). Without this flag, both with and without will be generated.

You can add `--skip-update` to not not automatically update emoji.json when a new version has been released.

Your generated file should be `emoji.ahk` :tada:

###### Thanks to [iamcal](https://github.com/iamcal/emoji-data) for the complete emoji data.