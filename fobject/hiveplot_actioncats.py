# coding: utf-8

import os
import sys
import argparse
import svgwrite


parser = argparse.ArgumentParser(
    description="create tlabs hiveplot")

parser.add_argument('sector',
                    default='all',
                    help='plot which sector')

args = parser.parse_args()

if __name__ == '__main__':
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fobject.settings")

    # Setup django
    import django
    django.setup()


from mm.models import Alter, Action, Sector, Agency, Networks

n = Networks()
n.update_alter_metrics()
n.update_action_metrics()

from math import sin, cos, radians
from scale import Scale
from pyveplot import Hiveplot, Node, Axis


if args.sector == "all":
    h = Hiveplot('agency_actioncats.svg')
else:
    h = Hiveplot('%s_actioncats.svg' % args.sector)


def rotate(radius, angle, origin=(0, 0)):
    """ Returns a tuple of destination coordinates
        given a radius, angle and origin tuple """
    return (origin[0] + round((radius * cos(radians(angle))), 2),
            origin[1] + round((radius * sin(radians(angle))), 2))


sector_color = {'Academia': 'blue',
                'Gobierno': 'green',
                None: 'orange',
                'Otros': 'purple',
                'Privado': 'purple',
                'Sociedad_Civil': 'yellow'}


offcenter = 80
center = (500, 400)
rotation = -180

############
# Ego axis #
############
ego_count = Alter.objects.filter(name__contains='TL0').count()
ego_scale = Scale(domain=[Alter.objects.order_by('degree')[0].degree,
                          Alter.objects.order_by('-degree')[0].degree],
                  range=[2, 40])
ego_axis_len = sum([ego_scale.linear(e.degree) * 2.0
                    for e in Alter.objects.filter(name__contains='TL0').all()])

ego_axis_origin = rotate(offcenter + 100,
                         angle=rotation,
                         origin=center)
axis_egos = Axis(ego_axis_origin,
                 rotate(offcenter + ego_axis_len,
                        angle=rotation,
                        origin=ego_axis_origin),
                 stroke="purple",
                 stroke_opacity="1", stroke_width=2)

# place ego nodes on ego axis
j = 0.0
for e in Alter.objects.filter(name__contains='TL0').order_by('degree').all():
    delta = ego_scale.linear(e.degree) / ego_axis_len
    j += delta * 2.0
    n = Node(e)
    axis_egos.add_node(n, j)

    if e.sector:
        sector = e.sector.name
    else:
        sector = None

    n.dwg.add(n.dwg.circle(center=(n.x, n.y),
                           r=ego_scale.linear(e.degree),
                           stroke_width=0,
                           fill=sector_color[sector],
                           fill_opacity=0.8))
    g = svgwrite.container.Group(transform='rotate(-90, %s, %s)' % (n.x, n.y),
                                 style='font-size:28')
    g.add(n.dwg.text(e.name,
                     insert=(n.x - 111, n.y)))
    n.dwg.add(g)



alter_scale = Scale(
    domain=[Alter.objects.exclude(name__contains='TL0').
            order_by('degree')[0].degree,
            Alter.objects.exclude(name__contains='TL0').
            order_by('-degree')[0].degree],
    range=[5, 20])


def alter_axis_len(sector_name):
    return sum([alter_scale.linear(a.degree)
                for a in Alter.objects.filter(
                        sector__name=sector_name).exclude(
                            name__contains='TL0')])


##############
# Alter axes #
##############
starts = []


def alter_axis(name, start):

    axis_len = alter_axis_len(name)
    axis_end = rotate(axis_len,
                      angle=rotation + 135,
                      origin=start)
    fake_end = rotate(axis_len + 60,
                      angle=rotation + 135,
                      origin=start)

    starts.append(fake_end)
    axis = Axis(start,
                axis_end,
                stroke=sector_color[name],
                stroke_opacity="1", stroke_width=2)

    # place alter nodes on alter axis
    j = 0.0
    for alter in Alter.objects.filter(
            sector__name=name).exclude(
                name__contains='TL0').order_by('degree').all():
        delta = alter_scale.linear(alter.degree) / axis_len
        j += delta
        n = Node(alter)
        axis.add_node(n, j)

        n.dwg = n.dwg.circle(center=(n.x, n.y),
                             r=alter_scale.linear(alter.degree) / 2.0,
                             stroke_width=0,
                             fill=sector_color[name],
                             fill_opacity=0.87)

    return axis


action_count = Action.objects.count()
action_scale = Scale(
    domain=[Action.objects.order_by('in_degree')[0].in_degree,
            Action.objects.order_by('-in_degree')[0].in_degree],
    range=[5, 40])

action_axis_len = sum([action_scale.linear(a.in_degree)
                       for a in Action.objects.all()])

action_axis_origin = rotate(offcenter,
                            angle=rotation + 180 + 60,
                            origin=center)
axis_actions = Axis(action_axis_origin,
                    rotate(offcenter + action_axis_len,
                           angle=rotation + 180 + 60,
                           origin=action_axis_origin),
                    stroke_width=0)


action_cat_color = {
    'Research': 'darkcyan',
    'Training': 'firebrick',
    'Agricultural/ecological training': 'orange',
    'Outreach': 'green',
    'Market': 'blue',
    'Education': 'teal',
    'Funding': 'grey',
    'Collaboration': 'red',
    'Financial/commercial training': 'yellow',
    'Social organization': 'cornflowerblue',
    'Tourism': 'forestgreen',
    'Management': 'dodgerblue',
    'Networking': 'goldenrod',
    'Production': 'midnightblue',
    'Construction': 'darkgreen',
    'Culture': 'cyan',
    'Consultancy': 'hotpink',
    'Ecological conservation': 'lightcoral',
    'Citizen assistance': 'indigo',
    'Legal training': 'brown',
}

# place action nodes on action axis
j = 0.0
for action in Action.objects.order_by('category', 'in_degree'):
    delta = 0.6 * action_scale.linear(action.in_degree) / action_axis_len
    j += delta

    n = Node(action)
    axis_actions.add_node(n, j)
    j += delta

    size = action_scale.linear(action.in_degree)
    fill = action_cat_color[action.category.name]
    n.dwg.add(n.dwg.rect(insert=(n.x - size/2.0,
                                 n.y - size/2.0),
                         size=(size, size),
                         fill=fill,
                         fill_opacity=0.8,
                         stroke_width=0.5))
    if action.in_degree > 3:
        g = svgwrite.container.Group(style='font-size:35;')
        g.add(n.dwg.text("%s: %s" % (action.category.name, action.action),
                         insert=(n.x - 20, n.y + 5),
                         text_anchor='end'))
        n.dwg.add(g)


ego_color = {1: 'forestgreen',
             2: 'greenyellow',
             3: 'goldenrod',
             4: 'gold'}


axis_origin = rotate(offcenter,
                     angle=rotation + 135,
                     origin=center)
alter_axes = [alter_axis("Gobierno", axis_origin),
              alter_axis("Academia", starts.pop()),
              alter_axis("Otros", starts.pop()),
              alter_axis("Privado", starts.pop()),
              alter_axis("Sociedad_Civil", starts.pop())]

h.axes = [axis_egos, ] + alter_axes + [axis_actions, ]


# link egos
for ego in Alter.objects.filter(name__contains='TL0').all():
    # grab their ego net
    for edge in ego.ego_net.all():
        alter = edge.target
        for alter_axis in alter_axes:
            if alter in alter_axis.nodes \
               and (args.sector == 'all'
                    or alter.sector.name == args.sector):
                h.connect(axis_egos, ego,
                          45,
                          alter_axis, alter,
                          -1,
                          stroke_width=edge.distance * 2.0,
                          stroke_opacity=0.33,
                          stroke=sector_color[alter.sector.name],)


# create links for agencies
for a in Agency.objects.all():
    for alter_axis in alter_axes:
        if a.alter in alter_axis.nodes and a.action in axis_actions.nodes\
           and (args.sector == "all" or a.alter.sector.name == args.sector):
            if a.action.in_degree < 2:
                color = "lightsteelblue"
                opacity = 0.77
            else:
                color = "darkcyan"
                opacity = 0.8
            h.connect(alter_axis, a.alter,
                      1,
                      axis_actions, a.action,
                      -40,
                      stroke_width=1.5,
                      stroke_opacity=opacity,
                      stroke=color)


h.save()
