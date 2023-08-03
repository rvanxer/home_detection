import sys
sys.path.insert(0, '/home/umni2/a/umnilab/users/verma99/mk/mobilkit')
from mobilkit.umni import *

P = Project('..')

class Region:
    """ A simple class for handling study regions (mostly MSAs). """
    def __init__(self, name: str, state: str, counties: list, 
                 geocode=None, root=P.root / 'regions'):
        self.name = name
        self.state = state
        self.root = root
        self.counties = sorted(counties)
        self.key = name.replace(' ', '_').lower()
        self.geocode = geocode or f'{name}, {state}'
        self.data = U.mkdir(root / self.key)
        self.datasets = set()
        P.params.set({'regions': {self.key: {
            'name': name, 'state': state, 'counties': self.counties}}})

    def __repr__(self):
        return f'Region({self.name})'
    
    def __hash__(self):
        return hash(self.geocode)
    
    def __eq__(self, other):
        return self.geocode == other.geocode
    
    @staticmethod
    def load(key):
        key = key.replace(' ', '_').lower()
        x = P.params.get(f'regions.{key}')
        rgn = Region(x['name'], x['state'], x['counties'])
        rgn.bbox = P.params.get(f'regions.{rgn.key}.bbox')
        return rgn


class Dataset:
    """ A container of a combination of region and analysis period. """
    def __init__(self, key, region, start_date, end_date,
                 root=P.root / 'datasets'):
        self.key = key
        if isinstance(region, str):
            region = Region.load(region)
        self.region = region
        self.start = U.to_date(start_date)
        self.end = U.to_date(end_date)
        self.dates = U.dates(self.start, self.end)
        self.data = U.mkdir(root / key)
        region.datasets.add(self)
        P.params.set({'datasets': {key: {
            'region': region.key, 'start': str(self.start),
            'end': str(self.end)}}})
        
    def fmt_dates(self, sep=' - ', fmt='%Y-%m-%d'):
        return sep.join([d.strftime(fmt) for d in [self.start, self.end]])
        
    def __repr__(self):
        return f'Dataset {self.key}({self.region.name}: {self.fmt_dates()})'

    def math(self, bold=False):
        label = '%s_%s' % (self.key[0], self.key[1])
        return r'$\mathbf{%s}$' % label if bold else r'$%s$' % label
    
    @staticmethod
    def load(key, region=None):
        x = P.params.get(f'datasets.{key}')
        rgn = region or Region.load(x['region'])
        return Dataset(key, rgn, x['start'], x['end'])
    
    
class HDA:
    def __init__(self, key, name=None, color=None, marker=None):
        self.key = key
        self.name = name
        self.color = color
        self.marker = marker
        P.params.set({'algorithms': {key: {
            'name': name, 'color': color, 'marker': marker}}})

    def __repr__(self):
        return self.key
    
    def math(self, bold=False):
        label = '%s_%s' % (self.key[0], self.key[1])
        return r'$\mathbf{%s}$' % label if bold else r'$%s$' % label

    @staticmethod
    def load(key):
        x = P.params.get(f'algorithms.{key}')
        return HDA(key, **x)
