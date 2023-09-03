import pathlib

BASEDIR = pathlib.Path(__file__).parent

MODULES_FOLDER = BASEDIR / 'modules'
HOME_MODULES = pathlib.Path().home() / ".daudit" / 'modules'

ENABLED_MODULES = list()
LOADED_MODULES = list()