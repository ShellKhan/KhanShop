{% extends 'base.html' %}

{% block title %}Catalog root{% endblock %}

{% block content %}
	<h1>Catalog root</h1>
	{% for cat in catlist %}
		<p>
			<a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a>
		</p>
	{% endfor %}
{% endblock %}