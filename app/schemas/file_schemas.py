import re
from marshmallow import Schema, fields, validate, pre_load

class CompressFileSchema(Schema):
  file_path = fields.Str(required=True, validate=validate.Regexp(r'^.*\.(jpg|jpeg|png|gif|bmp|tiff|webp|pdf)$', flags=re.IGNORECASE))

class SubPDFSchema(Schema):
  pdf_path = fields.Str(required=True, validate=validate.Regexp(r'^.*\.pdf$'))
  max_size = fields.Int(required=True, validate=validate.Range(min=1))
  size_unit = fields.Str(validate=validate.Regexp(r'^(kb|mb|gb)$', flags=re.IGNORECASE), missing='kb')
  @pre_load
  def preprocess_data(self, data, **kwargs):
    if 'size_unit' not in data or not data['size_unit']:
      data['size_unit'] = 'kb'
    size_factors = {'kb': 1024, 'mb': 1024**2, 'gb': 1024**3}
    data['max_size'] *= size_factors[data['size_unit'].lower()]
    return data