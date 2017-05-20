#plots sample crime data on a map with GeoJSON
#Charles Ritter 2017

import geojson

import parse as p

def create_map(data_file)
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com Just copy the output file and
    paste into a new Gist, then crate either a public or
    private gist. GitHub will automatically render the GeoJSON
    file as a map.
    """
def create_map(data_file):
    # Define type of GeoJSON we're creating

    # Define empty list to collect each point to graph

    # Iterate over our data to create GeoJSON document.
    # We're using enumerate() so we get the line, as well
    # the index, which is the line number.

        # Skip any zero coordinates as this will throw off
        # our map.

        # Setup a new dictionary for each iteration.

        # Assign line items to appropriate GeoJSON fields.

        # Add data dictionary to our item_list

    # For each point in our item_list, we add the point to our
    # dictionary.  setdefault creates a key called 'features' that
    # has a value type of an empty list.  With each iteration, we
    # are appending our point to that list.

    # Now that all data is parsed in GeoJSON write to a file so we
    # can upload it to gist.github.com
