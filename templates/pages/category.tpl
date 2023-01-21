{% extends 'base.html' %}

{% block title %}{{ category.name }}{% endblock %}

{% block content %}
	<nav aria-label="breadcrumb">
		<ol class="breadcrumb">
			<li class="breadcrumb-item"><a href="/catalog/">Каталог</a></li>
			{% if breadcrumbs %}
				{% for cat in breadcrumbs %}
					<li class="breadcrumb-item"><a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a></li>
				{% endfor %}
			{% endif %}
			<li class="breadcrumb-item active" aria-current="page">{{ category.name }}</li>
		</ol>
	</nav>
	<h1>{{ category.name }}</h1>
	<p>{{ category.description }}</p>
	{% if subcats %}
		<h2>Подкатегории:</h2>
		<ul>
			{% for cat in subcats %}
				<li>
					<a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a>
				</li>
			{% endfor %}
		</ul>
	{% endif %}
	{% if goods %}
		<h2>Товары в категории {{ category.name }}</h2>
		<div class="gridrow row">
			{% for item in goods %}
				<div class="col-sm-6 col-md-4 col-lg-3 col-xxl-2">
					<div class="card">
						<div class="card-header text-end">
							{{ item.category }}
						</div>
						<div class="card-body">
							<h5 class="card-title">{{ item.name }}</h5>
							<div class="card-image">
								<img src="" alt="{{ item.name }}">
							</div>
							<p class="card-text">{{ item.description }}</p>
							<a class="card-link" href="{% url 'products:product' item.category.pk item.pk %}">На страницу товара</a>
							<br>
							<a class="btn btn-primary" href="{% url 'basket:add' item.pk %}">КУПИТЬ</a>
						</div>
					</div>
				</div>
			{% endfor %}
		</div>
	{% endif %}
{% endblock %}