try:
    a = models.Alter.objects.get(name="Huella chinampera")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Taller 13")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Chinamperos")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Yolcan")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Sociedad Mexicana del Paisaje")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="GREENPEACE")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Michmani (PRD)")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Grillos Priistas Xochimilco")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Delegacion Xochimilco (Del Avelino)")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="SEDEMA-CONANP")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Juanita Gob Local (pista de canotaje)")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Agencia Francesa de Cooperacion")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Tec de Monterrey")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="UAM-CIBAC Xochimilco")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="UNAM-PUMA")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Tecnicos por proyectos")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Estudiantes Lic-Doct")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="Otros academicos")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="SACMEX")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="AFD")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="AEP")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="100RC")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="RBD")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="TNC")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="UAM")
    a.delete()
except:
    pass

try:
    a = models.Alter.objects.get(name="ANP")
    a.delete()
except:
    pass

try:
    s = models.Alter.objects.get(name="Central de abastos")
    t = models.Alter.objects.get(name="TL007")
    e = models.EgoEdge(source=s, target=t, distance=2, interaction="SP")
    e.save()
except:
    pass


try:
    s = models.Alter.objects.get(name="UNAM-Facultad de arquitectura (paisaje)")
    t = models.Alter.objects.get(name="TL012")
    e = models.EgoEdge(source=s, target=t, distance=2, interaction="SP")
    e.save()
except:
    pass
