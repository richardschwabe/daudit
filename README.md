<div align="center">
    <h1>daudit</h1>
    <span>Modular Docker Audit Tool</span>
</div>

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Installation](#installation)
  - [Via PIPX](#via-pipx)
  - [Manual](#manual)
  - [For Development](#for-development)
- [Usage](#usage)
  - [Adding functionality](#adding-functionality)
- [License](#license)
- [Contributing](#contributing)

# Overview

# Installation

## Via PIPX
```
pipx install daudit
```

## Manual

## For Development
```
git clone ...
pip install virtualenv
virtualenv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

# Usage

```bash
# Localhost Check
python -m daudit

# Remote Host Check
python -m daudit --remote 10.10.10.10
```

## Adding functionality
Add in your home directory `~/.daudit/modules` a new file with the following contents:
```python
...
```


# License
MIT

# Contributing


