import os

BASE = r"D:\MaxWay\templates"
os.makedirs(BASE, exist_ok=True)

# 1. SIDEBAR qayta yozish
sidebar = """
<aside class="menu-sidebar d-none d-lg-block">
    <div class="logo">
        <a href="{% url 'home_page' %}">
            <h2 class="text-primary"><i class="fas fa-hamburger pt-1"></i> MaxWay</h2>
        </a>
    </div>
    <div class="menu-sidebar__content js-scrollbar1">
        <nav class="navbar-sidebar">
            <ul class="list-unstyled navbar__list">
                <li><a href="{% url 'home_page' %}"><i class="fas fa-tachometer-alt"></i>Dashboard</a></li>
                <li><a href="{% url 'order_list' %}"><i class="fas fa-shopping-cart"></i>Buyurtmalar</a></li>
                <li><a href="{% url 'category_list' %}"><i class="fas fa-th-list"></i>Kategoriyalar</a></li>
                <li><a href="{% url 'branch_list' %}"><i class="fas fa-map-marker-alt"></i>Filiallar</a></li>
                <li><a href="{% url 'menuitem_list' %}"><i class="fas fa-utensils"></i>Menyu</a></li>
                <li><a href="{% url 'table_list' %}"><i class="fas fa-chair"></i>Stollar</a></li>
                <li><a href="{% url 'employee_list' %}"><i class="fas fa-users"></i>Xodimlar</a></li>
                <li><a href="{% url 'profile' %}"><i class="fas fa-user-circle"></i>Profil</a></li>
                <li><a href="{% url 'logout_page' %}"><i class="fas fa-sign-out-alt"></i>Chiqish</a></li>
            </ul>
        </nav>
    </div>
</aside>
"""
with open(os.path.join(BASE, "sidebar.html"), "w", encoding="utf-8") as f:
    f.write(sidebar)

# 2. INDEX / Dashboard qayta yozish
index = """
{% extends 'base.html' %}
{% block content %}
<div class="page-container">
    <div class="main-content">
        <div class="section__content section__content--p30">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12">
                        <div class="overview-wrap"><h2 class="title-1">Restoran Statistikasi</h2></div>
                    </div>
                </div>
                <!-- Box infos -->
                <div class="row m-t-25">
                    <div class="col-sm-6 col-lg-3">
                        <div class="overview-item overview-item--c1">
                            <div class="overview__inner">
                                <div class="overview-box clearfix">
                                    <div class="icon"><i class="zmdi zmdi-shopping-cart"></i></div>
                                    <div class="text"><h2>{{ counts.orders }}</h2><span>Buyurtmalar</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <div class="overview-item overview-item--c2">
                            <div class="overview__inner">
                                <div class="overview-box clearfix">
                                    <div class="icon"><i class="zmdi zmdi-money"></i></div>
                                    <div class="text"><h2>{{ counts.menu_items }}</h2><span>Menyu</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <div class="overview-item overview-item--c3">
                            <div class="overview__inner">
                                <div class="overview-box clearfix">
                                    <div class="icon"><i class="zmdi zmdi-pin"></i></div>
                                    <div class="text"><h2>{{ counts.branches }}</h2><span>Filiallar</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <div class="overview-item overview-item--c4">
                            <div class="overview__inner">
                                <div class="overview-box clearfix">
                                    <div class="icon"><i class="zmdi zmdi-account-o"></i></div>
                                    <div class="text"><h2>{{ counts.employees }}</h2><span>Xodimlar</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(index)

# Entities Data
entities = {
    "category": {"title": "Kategoriyalar", "url": "category", "ctx": "categories", "cols": ["Id", "Nomi", "Icon"], "tds": ["id", "name", "icon"]},
    "branch": {"title": "Filiallar", "url": "branch", "ctx": "branches", "cols": ["Id", "Filial Nomi", "Manzil", "Telefon"], "tds": ["id", "name", "address", "phone"]},
    "menuitem": {"title": "Menyu", "url": "menuitem", "ctx": "menu_items", "cols": ["Id", "TaomNomi", "Narxi", "Kategoriyasi"], "tds": ["id", "name", "price", "category_name"]},
    "employee": {"title": "Xodimlar", "url": "employee", "ctx": "employees", "cols": ["Id", "Ism", "Familiya", "Yosh", "Lavozim", "Filiali", "Mutaxassis"], "tds": ["id", "first_name", "last_name", "age", "role", "branch_name", "menu_item_name"]},
    "table": {"title": "Stollar", "url": "table", "ctx": "tables", "cols": ["Id", "Stol", "Sig'im", "Filial"], "tds": ["id", "name", "capacity", "branch_name"]},
    "order": {"title": "Buyurtmalar", "url": "order", "ctx": "orders", "cols": ["Rasm", "Ism", "Familiya", "Tel", "Stol", "Taom", "Miqdor", "Xolat", "Narxi", "Vaqt"], "tds": ["image", "first_name", "last_name", "phone", "table_name", "menu_item_name", "quantity", "status", "price", "created_at"]}
}

for folder, meta in entities.items():
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    
    # LIST HTML
    th_html = "".join([f"<th>{t}</th>" for t in meta['cols']])
    td_html = ""
    for td in meta['tds']:
        if td == "image":
             td_html += f"<td>{{% if item.{td} %}}<img src='/media/{{{{ item.{td} }}}}' width='50'>{{% else %}}-{{% endif %}}</td>"
        else:
             td_html += f"<td>{{{{ item.{td} }}}}</td>"
             
    lhtml = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<div class="page-container">
    <div class="main-content">
        <div class="section__content section__content--p30">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12">
                        <div class="overview-wrap">
                            <h2 class="title-1">{meta['title']}</h2>
                            <a href="{{% url '{meta['url']}_create' %}}" class="au-btn au-btn-icon au-btn--blue">
                                <i class="zmdi zmdi-plus"></i>Qo'shish</a>
                        </div>
                    </div>
                </div>
                <div class="row m-t-30">
                    <div class="col-md-12">
                        <div class="table-responsive m-b-40">
                            <table class="table table-borderless table-data3">
                                <thead>
                                    <tr>
                                        {th_html}
                                        <th>Harakatlar</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {{% for item in {meta['ctx']} %}}
                                    <tr>
                                        {td_html}
                                        <td>
                                            <a href="{{% url '{meta['url']}_edit' item.id %}}" class="btn btn-warning btn-sm">Tahrirlash</a>
                                            <a href="{{% url '{meta['url']}_delete' item.id %}}" class="btn btn-danger btn-sm">O'chirish</a>
                                        </td>
                                    </tr>
                                    {{% endfor %}}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}"""
    with open(os.path.join(d, "list.html"), "w", encoding="utf-8") as f:
        f.write(lhtml)

    # FORM HTML
    fhtml = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<div class="page-container">
    <div class="main-content">
        <div class="section__content section__content--p30">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-8 mx-auto">
                        <div class="card">
                            <div class="card-header"><strong>{meta['title']}</strong></div>
                            <div class="card-body card-block">
                                <form action="" method="post" enctype="multipart/form-data" class="form-horizontal">
                                    {{% csrf_token %}}
                                    {{{{ form.as_p }}}}
                                    <div class="card-footer text-right">
                                        <button type="submit" class="btn btn-primary btn-sm"><i class="fa fa-dot-circle-o"></i> Saqlash</button>
                                        <a href="{{% url '{meta['url']}_list' %}}" class="btn btn-danger btn-sm">Bekor qilish</a>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}"""
    with open(os.path.join(d, "form.html"), "w", encoding="utf-8") as f:
        f.write(fhtml)

print("ALL TEMPLATES GENERATED")
