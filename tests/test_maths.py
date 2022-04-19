from scratches.maths import Point, Ellipse


def test_is_point_inside():
    # Point
    point_in_ellipse = Point(-1, 0)
    point_outof_ellipse = Point(0, 2.1)

    # Ellipse
    ellipse_centre_point = Point(0, 0)
    ellipse_radius_x = 1
    ellipse_radius_y = 2
    ellipse = Ellipse(ellipse_centre_point, ellipse_radius_x, ellipse_radius_y)

    assert ellipse.is_point_inside(point_in_ellipse)
    assert not ellipse.is_point_inside(point_outof_ellipse)


