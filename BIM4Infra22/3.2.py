# pip install otlmow_converter

from otlmow_converter.AssetFactory import AssetFactory

if __name__ == '__main__':
    asset = AssetFactory.dynamic_create_instance_from_ns_and_name(namespace='onderdeel',
                                                                  class_name='Wegkantkast')
    print(asset)
