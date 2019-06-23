#!/usr/bin/env python
# Hack to get around https://github.com/elastic/logstash/issues/10879
import collections
from yaml import load, FullLoader


class FilterModule(object):
    def flatten(self, d, parent_key, sep):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(self.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def flatten_keys(self, d, parent_key='', sep='.'):
        lines = []
        results = self.flatten(d, parent_key='', sep=sep)
        for item in results:
            lines.append(item + ': ' + results[item])

        return load("\n".join(lines), Loader=FullLoader)


    def filters(self):
        return {
            'flatten_keys': self.flatten_keys,
        }
