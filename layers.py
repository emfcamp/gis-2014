mapfile = 'emf2014.dxf'

#
# The configuration below describes an ordered list of layers visible on the map server.
# The order is the order in which the layers appear in the layer selection settings on
# the map server, as well as the rendering order; layers containing transparent areas,
# like Fields, should be at the beginning to avoid overlaying an area on top of other data.
#
# Each map-visible layer is a dictionary containing the following fields:
# - title:     The name of the layer as visible in the layer picker box.
# - aliases:   Alternative names for this layer that are also accepted by the
#              Semantic Maps wiki extension. To ensure compatibility with existing
#              wiki maps, if a layer title is changed, the old name should be added
#              as an alias.
# - input:     A list of input layers, described below, in increasing z-order.
# - enabled:   If set to False, the layer is disabled by default. Defaults to True.
#
# An input source consists of an input file (currently only .dxf files are supported,
# but this can be changed if we're going to add data from NOC and Power) along with a
# set of layers defined in that file, together with layout data describing how to render
# the data in this layer. The following fields are defined for an input source:
#
# - file:           The source filename. No full path is necessary, search paths are
#                   defined elsewhere.
# - layers:         The selected layers from the source file, specified as a set of
#                   regular expressions of which a source layer needs to match one.
# - color, width:   The color and width used to render LINE data in this data source.
#                   Width is measured in pixels, color is specified as 'rrggbb' or 'rrggbbaa'.
# - fill:           The color used to render AREA data in this data source.
# - text, fontSize: The color and font size used to render text labels in the data source.
#                   Font sizes are in a scale roughly compatible with those specified in QCad.
#                   If the font size is not specified, the size from the map file is used.
#

layers = [
    {'title': 'Fields',
        'input': [
        {'file': mapfile,
            'layers': ['Event Fields \(Hatch\)'],
            'fill': '00B503',
        },
        {'file': mapfile,
            'layers': ['Fields \(Hatch\)'],
            'fill': 'CFB617',
        }
        ]
    },
    {'title': 'Trees',
        'input': [
        {'file': mapfile,
            'layers': ['Trees'],
            'fill': '3E7830',
        }
        ]
    },

    {
        'title': 'Waterways',
        'input': [
        {
            'file': mapfile,
            'layers': ['Rivers'],
            'color': '000099',
            'width_units': 'meters',
            'width': '2',
        },
        {
            'file': mapfile,
            'layers': ['Water - Surface'],
            'color': '000099',
            'fill': '000099',
            'width': '1',
        },

    ]},
    {
        'title': 'Paths',
        'input': [
        {
            'file': mapfile,
            'layers': ['Paths - Gravel Track'],
            'color': '999999',
            'width_units': 'meters',
            'width': '4',
        },
        {
            'file': mapfile,
            'layers': ['Paths - Trackway'],
            'color': '999999',
            'width_units': 'meters',
            'width': '2',
        },

    ]},

    {
        'title': 'Perimeter',
        'input': [
        {
            'file': mapfile,
            'layers': ['Perimeter'],
            'color': 'ff0000',
            'width_units': 'meters',
            'width': '1',
        },
    ]},
    {
        'title': 'Power',
        'input': [
        {
            'file': mapfile,
            'layers': ['Power - Generator'],
            'color': 'ff00ff',
            'width': '2',
        }]
    },
    {
        'title': 'Tents',
        'input': [
        {
            'file': mapfile,
            'layers': ['Tents'],
            'color': '000000',
            'width': '1',
            'text': '000000',
        },

    ]},
    {'title': 'Labels',
        'input': [
        {'file': mapfile,
            'layers': ['Labels'],
            'text': '000000',
        }]
    },
    {'title': 'Toilets',
        'input': [
        {'file': mapfile,
            'layers': ['Toilets'],
            'color': 'ff00ff',
            'width': 1
        }]
    },
    {'title': 'NOC',
        'enabled': False,
        'input': [
        {'file': mapfile,
            'layers': ['NOC-DK'],
            'color': '009900',
            'width': '1',
        },
        {'file': mapfile,
            'layers': ['NOC-DK-Label'],
            'color': '009900',
            'width': '1',
            'text': '000000'
        },
    ]},
    {'title': 'Water',
        'enabled': False,
        'input': [
        {'file': mapfile,
            'layers': ['Water infrastructure'],
            'color': '0000FF',
            'width': '1',
        }
    ]},
]
