# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import networkx as nx

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name


class Alter(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, null=True)
    sector = models.ForeignKey(Sector, null=True)
    desc = models.TextField(blank=True)

    degree = models.IntegerField(default=0)

    def mental_model(self):
        g = nx.Graph()

        for e in self.mentaledge_set.all():
            g.add_edge(e.source.name,
                       e.target.name)
        return json.dumps(nx.node_link_data(g), indent=2)

    def __unicode__(self):
        return u"%s" % self.name


class EgoEdge(models.Model):
    source = models.ForeignKey(Alter, related_name='ego_net')
    target = models.ForeignKey(Alter, related_name='alter_for')

    distance = models.IntegerField()
    interaction = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s<-%s->%s" % (self.source, self.distance, self.target)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"%s" % self.name


class Action(models.Model):
    action = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True)

    in_degree = models.IntegerField(default=0)

    def update_in_degree(self):
        self.in_degree = self.actor_set.count()

    def __unicode__(self):
        return u"%s" % self.action


class Agency(models.Model):
    alter = models.ForeignKey(Alter,
                              related_name='action_set',
                              null=True)
    action = models.ForeignKey(Action,
                               related_name='actor_set',
                               null=True)

    class Meta:
        verbose_name_plural = "Agencies"

    def __unicode__(self):
        return u"%s->%s" % (self.alter, self.action)


class MentalType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    mental_type = models.ForeignKey(MentalType, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class MentalEdge(models.Model):
    ego = models.ForeignKey(Alter, null=True)
    source = models.ForeignKey(Item,
                               related_name='leads_to',
                               null=True)
    target = models.ForeignKey(Item,
                               related_name='caused_by',
                               null=True)

    def __unicode__(self):
        return u"(%s)->(%s)" % (self.source, self.target)


class Networks:
    def __init__(self):

        self.alter = nx.Graph()

        for e in EgoEdge.objects.all():
            self.alter.add_edge(e.source, e.target,
                                distance=e.distance,
                                interaction=e.interaction)

    def update_alter_metrics(self):
        degrees = list(self.alter.degree())
        for node in degrees:
            node[0].degree = node[1]
            node[0].save()

    def update_action_metrics(self):
        for a in Action.objects.all():
            a.update_in_degree()
            a.save()
