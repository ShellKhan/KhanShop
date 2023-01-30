{% extends 'base.html' %}

{% block title %}{{ product.name }}{% endblock %}

{% block content %}
	<nav aria-label="breadcrumb">
		<ol class="breadcrumb">
			<li class="breadcrumb-item"><a href="/products/">Каталог</a></li>
			{% if breadcrumbs %}
				{% for cat in breadcrumbs %}
					<li class="breadcrumb-item"><a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a></li>
				{% endfor %}
			{% endif %}
			<li class="breadcrumb-item active" aria-current="page">{{ product.name }}</li>
		</ol>
	</nav>
	<h1>{{ product.name }}</h1>
	<p>{{ product.description }}</p>
{% endblock %}