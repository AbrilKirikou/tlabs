var ego_id = document.currentScript.getAttribute('ego_id');

$.getJSON(`/ego_json/${ego_id}`, function (data) {
    console.log(data);
    var cy = cytoscape({
	container: document.getElementById('cy'),
	elements: data,

	style: cytoscape.stylesheet()
	    .selector('node')
	    .css({
		'shape': 'data(shape)',
		// 'width': 'mapData(weight, 40, 80, 20, 60)',
		'content': 'data(name)',
		'text-valign': 'center',
		'text-outline-width': 2,
		'text-outline-color': 'data(scolor)',
		'background-color': 'data(scolor)',
		'color': '#fff'
	    })
	    .selector(':selected')
	    .css({
		'border-width': 3,
		'border-color': '#333'
	    })
	    .selector('edge')
	    .css({
		'curve-style': 'bezier',
		'opacity': 0.666,
		'width': 'mapData(strength, 70, 100, 2, 6)',
		'target-arrow-shape': 'triangle',
		'source-arrow-shape': 'circle',
//		'line-color': 'data(faveColor)',
//		'source-arrow-color': 'data(faveColor)',
//		'target-arrow-color': 'data(faveColor)'
	    })
	    .selector('edge.questionable')
	    .css({
		'line-style': 'dotted',
		'target-arrow-shape': 'diamond'
	    })
	    .selector('.faded')
	    .css({
		'opacity': 0.25,
		'text-opacity': 0
	    }),

	layout: {
	    name: 'circle'
	}
    });
});