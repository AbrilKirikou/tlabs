# Tlabs

## Hiveplot

### Colores de Egos y Alters

 - Academia: azul
 - Gobierno: verde
 - Otros: morado
 - Privado: morado
 - Sociedad_Civil: amarillo

Cuadros rojos son acciones, van ordenadas hacia afuera por in_degree.

### Vínculos

Los ejes 1 y 2 se conectan por curvas del color de los nodos del eje
2, el grosor representa la distancia.

Los ejes 2 y 3 se unen por vínculos color azul claro cuando el
in_degree de la acción es 1, y dark cyan cuando es mayor.

<img src="fobject/agency.png" >

<table>
<thead>
<tr>
<td>
Gobierno
</td>
<td>
Academia
</td>
<td>
Otros.png
</td>
<td>
Privado
</td>
<td>
Sociedad Civil
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
<img src="fobject/Gobierno.png">
</td>
<td>
<img src="fobject/Academia.png">
</td>
<td>
<img src="fobject/Otros.png">
</td>
<td>
<img src="fobject/Privado.png">
</td>
<td>
<img src="fobject/Sociedad_Civil.png">
</td>
</tr>
</tbody>
</table>


## Clusterizados por sus alters

<img src="fobject/dendrogram.png">

Hay un índice jaccard de semejanza entre los conjuntos de alters de dos egos.

## Clusterizados por sus acciones

<img src="fobject/dendrogram_actions.png">

Hay un índice jaccard de semejanza entre los conjuntos de acciones, a
través de los alters, de dos egos.

## Alters clusterizados por distancias a Egos
<img src="fobject/dendrogram_distances.png">
