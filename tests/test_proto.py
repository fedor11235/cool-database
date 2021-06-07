from modules import ProtoHelper
import pytest

@pytest.mark.parametrize("in_str, out_len", [("fr r", 10),
                                        (66653355353539, 10),
                                        (("r r", "55", 6), 10),
                                        ({"rr":9, 5:"55"}, 10)])

def test_type_BuildProtoString(in_str, out_len):
    assert type(ProtoHelper.BuildProtoString(in_str, out_len))==type(bytearray(b''))

