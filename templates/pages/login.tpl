{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
	<h1>{{ title }}</h1>
	<form action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <div class="mb-3">
            <label for="id_username" class="form-label">Логин</label>
            <input type="text" class="form-control{% if login_form.non_field_errors or login_form.username.errors %} is-invalid{% endif %}" name="username" id="id_username">
            {% if login_form.username.errors %}
                {% for err in login_form.username.errors %}
                    <div class="invalid-feedback">{{ err }}</div>
                {% endfor %}
            {% endif %}
        </div>
        <div class="mb-3">
            <label for="id_password" class="form-label">Пароль</label>
            <input type="password" class="form-control{% if login_form.non_field_errors or login_form.password.errors %} is-invalid{% endif %}" name="password" id="id_password">
            {% if login_form.password.errors %}
                {% for err in login_form.password.errors %}
                    <div class="invalid-feedback">{{ err }}</div>
                {% endfor %}
            {% endif %}
        </div>
        {% if login_form.non_field_errors %}
            <div class="mb-3">
                {% for err in login_form.non_field_errors %}
                    <div class="text-danger">{{ err }}</div>
                {% endfor %}
            </div>
        {% endif %}
        <button type="submit" class="btn btn-primary">Войти</button>
    </form>
{% endblock %}
