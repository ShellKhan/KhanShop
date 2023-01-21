{% extends 'base.html' %}

{% block title %}Catalog root{% endblock %}

{% block content %}
	<h1>Каталог</h1>
	{% for cat in catlist %}
		<p>
			{{ cat.1|safe }}<a href="/catalog/{{ cat.0.urlname }}">{{ cat.0.name }}</a>
		</p>
	{% endfor %}
{% endblock %}