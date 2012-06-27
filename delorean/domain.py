# coding: utf-8
import urllib2
import json
import string

class Transformer(object):
    """
    """
    def __init__(self, template):
        self._template = string.Template(template)

    def transform(self, data):
        if not isinstance(data, dict):
            raise TypeError('data must be dict')

        try:
            return self._template.substitute(data)
        except KeyError, exc:
            raise ValueError("there are some data missing: {}".format(exc))

    def transform_list(self, data_list):
        if not isinstance(data_list, list) and not isinstance(data_list, tuple):
            raise TypeError('data must be list or tuple')

        res = []
        for data in data_list:
            res.append(self.transform(data))
        return '\n'.join(res)

class DataCollector(object):
    """
    Responsible for collecting data from RESTful interfaces,
    and making them available as Python datastructures.
    """
    def __init__(self, resource_url, url_lib=urllib2):
        self._resource_url = resource_url
        self._url_lib = url_lib

        try:
            self._data = self._url_lib.urlopen(self._resource_url)
        except url_lib.URLError:
            raise ValueError("invalid resource url: '%s'".format(
                self._resource_url))

    def get_data(self):
        """
        Get data from the specified resource and returns
        it as Python native datastructures.
        """
        return json.loads(self._data.read())

class DeLorean(object):
    """
    Represents a time machine, generating databases
    compatible with SciELO legacy apps (ISIS dbs)
    from RESTFul data sources.
    """
    def generate_title(self):
        return u'http://localhost:6543/files/title_2012-06-26_13:25:24.008242.zip'
