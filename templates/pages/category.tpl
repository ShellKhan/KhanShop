{% extends 'base.html' %}

{% block title %}{{ category.name }}{% endblock %}

{% block content %}
	<h1>{{ category.name }}</h1>
	<p>{{ category.description }}</p>
	{% if subcats %}
		{% for cat in subcats %}
			<p>
				<a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a>
			</p>
		{% endfor %}
	{% endif %}
	{% if breadcrumbs %}
		<hr>
		{% for cat in breadcrumbs %}
			<p>
				<a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a>
			</p>
		{% endfor %}
	{% endif %}
{% endblock %}