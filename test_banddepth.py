
from banddepth import inside

import pytest

flat_lb = [0.0, 0.0, 0.0, 0.0]
flat_ub = [1.0, 1.0, 1.0, 1.0]

inc_lb = [0.0, 0.4, 0.8, 1.0]
dec_ub = [1.1, 0.9, 0.5, -1.0]

r1 = [0.5, 0.5, 0.5, 0.5]
r2 = [1.5, 1.5, 1.5, 1.5]
r3 = [-1.0, -1.0, -1.0, -1.0]
r4 = [0.5, 0.5, 1.5, 1.8]
r5 = [0.5, 1.5, 0.5, 1.8]

class TestIntersections:

  @pytest.mark.skip(reason="pending")
  def test_unequal_len_curves(self):
    """curves of differing lengths should generate an error"""
    pass

  def test_fully_inside(self):
    """curve is fully inside surrounding curves"""
    assert inside(r1, flat_lb, flat_ub)

  def test_fully_outside(self):
    """curve is fully outside surrounding curves"""
    assert not inside(r2, flat_lb, flat_ub)
    assert not inside(r3, flat_lb, flat_ub)

  def test_half_inside(self):
    """curve is inside and then goes outside"""
    assert not inside(r4, flat_lb, flat_ub)

  def test_inout_varying(self):
    """curve varies from inside to outside and back again"""
    assert not inside(r5, flat_lb, flat_ub)

  def test_bounds_cross(self):
    """curve varies but bounding curves cross"""
    assert inside(r1, inc_lb, dec_ub)

