## PyDeck
from IPython.display import clear_output
from google.colab import output
output.enable_custom_widget_manager()
# output.disable_custom_widget_manager()
import os
os.system('pip install pydeck')
clear_output()
import pandas as pd
import numpy as np
import pydeck as pdk
from pydeck.types import String as pdk_string
def create_pdk_text_layer(data, text, position = 'coordinates', size = 12, color = [0,0,0], angle = 0, text_anchor = 'middle', alignment_baseline = 'center', pickable = True):
  return pdk.Layer(
      'TextLayer',
      data,
      get_text = text,
      get_position = position,
      # Text styling and positioning
      get_size = size,
      get_color = color,
      get_angle = angle,
      get_text_anchor = pdk_string(text_anchor),
      get_alignment_baseline = pdk_string(alignment_baseline),
      # Interactivity
      pickable = pickable
  )

def create_pdk_polygon_layer(data, polygon, filled = True, fill_color = [255, 255, 255], opacity = 0.1, stroked = False, line_color = [255, 255, 255], line_width = 1, extruded = False, elevation = 0, wireframe = False, auto_highlight = True, pickable = True):
  return pdk.Layer(
      'PolygonLayer',
      data,
      get_polygon = polygon,
      # Fill
      filled = filled,
      get_fill_color = fill_color,
      opacity = opacity,
      # Border
      stroked = stroked,
      get_line_color = line_color,
      get_line_width = line_width,
      # Height
      extruded = extruded,
      get_elevation = elevation,
      # Surface
      wireframe = wireframe,
      # Interactivity
      auto_highlight = auto_highlight,
      pickable = pickable,
  )

def show_deck(layers, view, tooltip = True, iframe_height = 500, html_filepath = '/content/map.html'):
    r = pdk.Deck( layers, initial_view_state=view, map_style=pdk.map_styles.DARK, tooltip = tooltip) # tooltip={'html': '<br>'.join(['<b>'+c+':</b> {'+c+'}' for c in tooltip_columns])}
    _ = r.to_html(html_filepath, iframe_height = iframe_height)