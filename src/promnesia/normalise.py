from typing import List, Any
from re import compile as R
from kython.canonify import canonify


# TODO make sure we are consistent with these rules??
STRIP_RULES: List[List[Any]] = [
    [R('.*')                     , R('^\\w+://'         )],
    [R('.*')                     , R('(www|ww|amp)\\.'  )],
    [R('.*')                     , R('[&#].*$'          )],
    [
        [R('^(youtube|urbandictionary|tesco|scottaaronson|answers.yahoo.com|code.google.com)') , None],
        [R('.*'), R('[\\?].*$')],
    ],
    [R('.*')                     , R('/$'               )],
]


def normalise_url(url):
    return canonify(url)
    cur = url
    for thing in STRIP_RULES:
        first = thing[0]
        rules: List
        if isinstance(first, list):
            rules = thing
        else:
            rules = [thing]

        for target, reg in rules:
            if target.search(cur):
                if reg is not None:
                    cur = reg.sub('', cur)
                break


    return cur


# use [] instead of () so it's easy to copy regexes to js
# TODO eh, None vs null..

# TODO fine tune, start with reddit?
# TODO ok, if first elemnent is a rule, apply it
# if only one, bail
# if it's a list, they are mutually exclusive?