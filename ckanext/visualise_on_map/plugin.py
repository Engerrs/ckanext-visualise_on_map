'''A plugin to add a Visualise on Map button to Datasets page.
   Iterates through dataset resources looking for one with the
   edp web map format then uses its URL for its hyperlink.

   Created by Aiden Price Informed Solutions GIS Technology Specialist
   7/6/2016.'''

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def has_web_map_layer(package_dict):
    '''Returns a boolean indicating whether the dataset has a layer in Geocortex'''
    if package_dict['resources'] is not None:
        for resource in package_dict['resources']:
            strFormat = resource['format'].lower().replace(' ', '')
            if strFormat == 'edpwebmap' or strFormat == 'seedwebmap':
                return True
    else:
        return False


def get_web_map_layer_url(package_dict):
    '''Returns the URL to show the dataset's layer on Geocortex.'''
    if package_dict['resources'] is not None:
        for resource in package_dict['resources']:
            strFormat = resource['format'].lower().replace(' ', '')
            if strFormat == 'edpwebmap' or strFormat == 'seedwebmap':
                return resource['url']
    else:
        return ''


class Visualise_On_MapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'visualise_on_map')

    def get_helpers(self):
        return {'visualise_on_map_has_web_map_layer': has_web_map_layer, 'visualise_on_map_get_web_map_layer_url': get_web_map_layer_url}
