import os

from onedns.logger import log


def get_fqdn(name, domain):
    if not name.endswith(domain):
        if name.endswith('.'):
            return name + domain
        else:
            return '.'.join([name, domain])
    return name


def get_kwargs_from_dict(d, prefix, lower=False):
    tups_list = []
    for i in d:
        if i.startswith(prefix):
            arg = i.replace(prefix, '')
            if lower:
                arg = arg.lower()
            tups_list.append((arg, d[i]))
    return dict(tups_list)


def get_kwargs_from_env(prefix, lower=False):
    return get_kwargs_from_dict(os.environ, prefix, lower=lower)


def shell(local_ns={}):
    try:
        from IPython import embed
        return embed(user_ns=local_ns)
    except ImportError as e:
        log.error("Unable to load IPython:\n\n%s\n" % e)
        log.error("Please check that IPython is installed and working.")
