from configparser import ConfigParser, NoSectionError

def config(filename='./env.ini', section='raw_data'):
    parser = ConfigParser()
    parser.read(filename)
    if not parser.has_section(section):
        raise NoSectionError('Section {0} not found in the {1} file'.format(section, filename))

    params = parser.items(section)
    return {param[0]: param[1] for param in params}