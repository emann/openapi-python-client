{% macro construct(property, source) %}
{% if property.required %}
{{ property.python_name }} = isoparse({{ source }}).date()
{% else %}
{{ property.python_name }} = None
if {{ source }} is not None:
    {{ property.python_name }} = isoparse(cast(str, {{ source }})).date()
{% endif %}
{% endmacro %}

{% macro transform(property, source, destination) %}
{% if property.required %}
{% if property.nullable %}
{{ destination }} = {{ source }}.isoformat() if {{ source }} else None
{% else %}
{{ destination }} = {{ source }}.isoformat()
{% endif %}
{% else %}
if {{ source }} is UNSET:
    {{ destination }} = UNSET
{% if property.nullable %}
else:
    {{ destination }} = {{ source }}.isoformat() if {{ source }} else None
{% else %}
else:
    {{ destination }} = {{ source }}.isoformat()
{% endif %}
{% endif %}
{% endmacro %}
