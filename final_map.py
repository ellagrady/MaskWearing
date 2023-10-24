# format based on answer to a question on stackoverflow
# https://stackoverflow.com/questions/55598249/showing-alaska-and-hawaii-in-cartopy-map

import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

import shapely.geometry as sgeom


class Map:
    
    
    # A function that draws inset map, ++
    # ===================================
    def add_insetmap(self,axes_extent, map_extent, state_name, facecolor, edgecolor, geometry):
    # create new axes, set its projection
        use_projection = ccrs.Mercator()     # preserve shape well
        #use_projection = ccrs.PlateCarree()   # large distortion in E-W for Alaska
        geodetic = ccrs.Geodetic(globe=ccrs.Globe(datum='WGS84'))
        sub_ax = plt.axes( self.axes_extent, projection=use_projection)  # normal units
        sub_ax.set_extent( self.map_extent, geodetic)  # map extents

        # add basic land, coastlines of the map
        # you may comment out if you don't need them
        sub_ax.add_feature(cartopy.feature.LAND)
        sub_ax.coastlines()

        sub_ax.set_title( state_name)

        # add map `geometry` here
        sub_ax.add_geometries([geometry], ccrs.PlateCarree(), \
                                facecolor=self.facecolor, edgecolor=self.edgecolor)
        # +++ more features can be added here +++

        # plot box around the map
        extent_box = sgeom.box( self.map_extent[0],  self.map_extent[2],  self.map_extent[1],  self.map_extent[3])
        sub_ax.add_geometries([extent_box], ccrs.PlateCarree(), color='none', linewidth=0.05)

    def makemap(self):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())

        ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

        shapename = 'admin_1_states_provinces_lakes_shp'
        states_shp = shpreader.natural_earth(resolution='110m',
                                                category='cultural', name=shapename)


        ax.background_patch.set_visible(False)
        ax.outline_patch.set_visible(False)

        ax.set_title('Map of Winners')

        winners = { #1 for biden, 0 for trump
            'New Jersey':  1,
            'Rhode Island':   1,
            'Massachusetts':   1,
            'Connecticut':    1,
            'Maryland':   1,
            'New York':    1,
            'Delaware':    1,
            'Florida':     0,
            'Ohio':  0,
            'Pennsylvania':  1,
            'Illinois':    1,
            'California':  1,
            'Virginia':    1,
            'Michigan':    1,
            'Indiana':    0,
            'North Carolina':  0,
            'Georgia':     1,
            'Tennessee':   0,
            'New Hampshire':   1,
            'South Carolina':  0,
            'Louisiana':   0,
            'Kentucky':   0,
            'Wisconsin':  1,
            'Washington':  1,
            'Alabama':     0,
            'Missouri':    0,
            'Texas':   0,
            'West Virginia':  0,
            'Vermont':     1,
            'Minnesota':  1,
            'Mississippi':   0,
            'Iowa':  0,
            'Arkansas':    0,
            'Oklahoma':    0,
            'Arizona':     1,
            'Colorado':    1,
            'Maine':  1,
            'Oregon':  1,
            'Kansas':  0,
            'Utah':  0,
            'Nebraska':    0,
            'Nevada':  1,
            'Idaho':   0,
            'New Mexico':  1,
            'South Dakota':  0,
            'North Dakota':  0,
            'Montana':     0,
            'Wyoming':      0,
            'Hawaii': 1,
            'Alaska': 0,
            'District of Columbia': 1}

        for state in shpreader.Reader(states_shp).records():


            self.edgecolor = 'black'
                
            state_name = winners[ state.attributes['name'] ]
        

            # simple scheme to assign color to each state
            if state_name == 0:
                self.facecolor = "pink"
                
            else:
                self.facecolor = "lightblue"

                # special handling for the 2 states
                # ---------------------------------
            if state.attributes['name'] in ("Alaska", "Hawaii"):
                    # print("state.attributes['name']:", state.attributes['name'])

                state_name = state.attributes['name']

                    # prep map settings
                    # experiment with the numbers in both `_extents` for your best results
                if state_name == "Alaska":
                        # (1) Alaska
                    self.map_extent = (-178, -135, 46, 73)    # degrees: (lonmin,lonmax,latmin,latmax)
                    self.axes_extent = (0.04, 0.06, 0.29, 0.275) # axes units: 0 to 1, (LLx,LLy,width,height)

                if state_name == "Hawaii":
                    # (2) Hawii
                    self.map_extent = (-162, -152, 15, 25)
                    self.axes_extent = (0.27, 0.06, 0.15, 0.15)

                    # add inset maps
                self.add_insetmap(self.axes_extent, self.map_extent, state_name, \
                                self.facecolor, \
                                self.edgecolor, \
                                state.geometry)

                # the other (conterminous) states go here
            else:
                    # `state.geometry` is the polygon to plot
                ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                                    facecolor=self.facecolor, edgecolor=self.edgecolor)

        plt.show()