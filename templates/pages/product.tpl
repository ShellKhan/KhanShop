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
	<div class="gridrow row">
		{% if product.main_image %}
			<div class="col-lg-8 col-xxl-6">
				<img class="rounded" src="/media/{{ product.main_image.get_catalog_image }}" alt="{{ product.main_image.short_desc }}">
				<h2>Галерея</h2>
				<div class="gridrow row">
					{% for item in gallery %}
						<div class="col-4">
							<div class="card">
								<img class="card-img-top" src="/media/{{ item.get_gallery_image }}" alt="{{ item.short_desc }}">
								<p class="card-text">{{ item.short_desc }}</p>
								<a href="/media/{{ item.get_main_image }}" class="btn btn-primary" target="_blank">Размер побольше</a>
								<a href="/media/{{ item.get_big_image }}" class="btn btn-secondary" target="_blank">Совсем большой размер</a>
							</div>
						</div>
					{% endfor %}
				</div>
			</div>
			<div class="col-lg-4 col-xxl-6">
		{% else %}
			<div class="col-lg-12 col-xxl-12">
		{% endif %}
			<p>{{ product.description }}</p>
			<h2 class="text-danger">{{ product.price }} рублёв <span class="badge bg-danger">{{ product.get_status }}</span></h2>
		</div>
	</div>
{% endblock %}