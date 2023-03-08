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
	{% if category.image %}
		<img class="rounded" src="/media/{{ category.image.get_catalog_image }}" alt="{{ category.image.short_desc }}">
	{% endif %}
	{% if subcats %}
		<h2>Подкатегории</h2>
		<ul>
			{% for cat in subcats %}
				<li>
					<a href="/catalog/{{ cat.urlname }}">{{ cat.name }}</a>
				</li>
			{% endfor %}
		</ul>
	{% endif %}
	{% if products %}
		<h2>Товары в категории {{ category.name }}</h2>
		<div class="gridrow row">
			{% for item in products %}
				<div class="col-sm-6 col-md-4 col-lg-3 col-xxl-2">
					<div class="card">
						<div class="card-header text-center">
							{{ item.category.name }}
						</div>
						<div class="card-body">
							<h5 class="card-title">{{ item.name }}</h5>
							{% if item.main_image %}
								<div class="card-image">
									<img src="/media/{{ item.main_image.get_catalog_image }}" alt="{{ item.main_image.short_desc }}">
								</div>
							{% endif %}
							<p class="card-text">{{ item.short_desc }}</p>
							<a class="card-link" href="/products/{{ item.pk }}">На страницу товара</a>
							<h3 class="text-center text-danger">{{ item.price }} &#x20bd;</h3>
							<a class="btn btn-primary" href="#">КУПИТЬ</a>
						</div>
						<div class="card-footer text-center">
							{{ item.get_status }}
						</div>
					</div>
				</div>
			{% endfor %}
		</div>
	{% endif %}
	{% if not subcats and not products %}
		<p>Это пустая категория</p>
	{% endif %}
{% endblock %}