# Rap Lyrics Generator Kivy App!

This is a simple Kivy app that takes input from the user: starting word, temperature & number of characters and generates unique rap lyrics.

Kudos to kbd-overlord for helping us set up the project dependecies using poetry!

# Setting up the project - Mac OS

### Install pyenv build dependencies.

#### Xcode Command Line Tools
```xcode-select --install```

#### Other dependencies

```brew install openssl readline sqlite3 xz zlib```

#### Install pyenv with Homebrew.

```brew update ```

```brew install pyenv```

#### Install Python 3.7.6

```pyenv install 3.7.6```

#### Clone the repository.

```cd [directory of the project]```

```git clone [this repository clone link]```

```cd rap-generator-app```

### Set a local version for Python (for current directory only).

#### Set version
```pyenv local 3.7.6```

#### Check version
```pyenv version```

### Install poetry via curl.

#### Install
```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

#### Verify
```poetry --version```


##### Install a pre-existing poetry project with dependencies.

### Go to project folder
```cd rap-generator-app```

#### Install poetry project
```poetry install```

#### If you get an error that python versions are not compatible, run this command

```poetry env use ~/.pyenv/shims/python3.7```

#### and then

```poetry update```

### Run main.py script to verify that setup is complete.

#### Run a poetry shell
```poetry shell```

#### Inside the shell now type
```poetry run python main.py```

You can now type starting word, temperature, number of characters and generate your own rap lyrics!

