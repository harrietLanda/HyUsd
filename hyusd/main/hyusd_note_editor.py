import logging
import json
import os

import sys
sys.path.append(r"C:/Users/harriet/workspace/deploy")

from Qt import *

from qtpy import QtWidgets

import qtpynodeeditor
from qtpynodeeditor import (NodeData, NodeDataModel, NodeDataType, PortType,
                            StyleCollection)

# current_path = os.path.abspath(__file__)
_CONFIG = r"C:/Users/harriet/workspace/hyusd/hyusd/config.json"

logging.basicConfig(level='INFO')

with open(_CONFIG) as f:
  style_json = json.load(f)

class MyNodeData(NodeData):
    data_type = NodeDataType(id='MyNodeData', name='MyNodeData')


class Object_node(NodeDataModel):
    name = 'usd_object'
    caption = 'USD Object'
    caption_visible = True
    num_ports = {PortType.input: 0,
                 PortType.output: 1,
                 }
    port_caption_visible = True
    data_type = MyNodeData.data_type
    port_caption = {'output': {0: 'Output'}}

class Output_node(NodeDataModel):
    name = 'output_node'
    caption = 'Output Node'
    caption_visible = True
    num_ports = {PortType.input: 1,
                 PortType.output: 0,
                 }
    port_caption_visible = True
    data_type = MyNodeData.data_type
    port_caption = {'input': {0: 'Object'}}

    def out_data(self, port):
        return MyNodeData()

    def set_in_data(self, node_data, port):
        ...

    def embedded_widget(self):
        return None

def main(app):
    style = StyleCollection.from_json(style_json)

    registry = qtpynodeeditor.DataModelRegistry()
    registry.register_model(Object_node, category='Objects Nodes', style=style)
    registry.register_model(Output_node, category='Output Nodes', style=style)
    scene = qtpynodeeditor.FlowScene(style=style, registry=registry)

    view = qtpynodeeditor.FlowView(scene)


    return scene, view
