{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
	<h1>{{ title }}</h1>
	<p><a href="/catalog/">Каталог</a></p>
	<p><a href="/pages/">Другие страницы</a></p>
{% endblock %}