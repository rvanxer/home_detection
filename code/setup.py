import sys
sys.path.insert(0, '/home/umni2/a/umnilab/users/verma99/mk/mobilkit')
from mobilkit.umni import *

P = Project('..')

class Region:
    """ A simple class for handling study regions (mostly MSAs). """

    def __init__(self, name: str, state: str, counties: list[str]):
        self.name = name
        self.label = name.replace(' ', '_').lower()
        self.state = state
        self.counties = sorted(counties)
        # folder containing this region's data
        self.data = P.data / str(self)
        # folder containing this region's geometry data
        self.geom = self.data / 'geometry'
        # add its details to the params file
        P.params.set({'regions': {str(self): {
            'state': state, 'counties': self.counties}}})

    def __repr__(self):
        return f'Region({self.name})'
    
    def __str__(self):
        return self.label
    
    @staticmethod
    def load(name, state=None):
        rgn = Region(name, state, counties=[])
        rgn.cnty = gpd.read_file(rgn.geom / 'counties.gpkg')
        rgn.counties = sorted(list(rgn.cnty['name']))
        rgn.bbox = list(rgn.cnty.geometry.unary_union.bounds)
        P.params.set({'regions': {str(rgn): {
            'counties': rgn.counties, 'bbox': rgn.bbox}}})
        return rgn
