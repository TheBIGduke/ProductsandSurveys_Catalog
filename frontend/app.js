const API = "http://localhost:9999/api";

async function init() {
    const [cats, prods] = await Promise.all([
        fetch(`${API}/categories`).then(r => r.json()),
        fetch(`${API}/products`).then(r => r.json())
    ]);
    renderFilters(cats);
    renderProducts(prods);
}

function renderFilters(cats) {
    const bar = document.getElementById('filter-bar');
    bar.innerHTML = '<button class="btn filter-btn active" onclick="filter(null, this)">All</button>';
    cats.forEach(c => {
        bar.innerHTML += `<button class="btn filter-btn" onclick="filter(${c.id}, this)">${c.name}</button>`;
    });
}

async function filter(id, el) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
    const url = id ? `${API}/products?category_id=${id}` : `${API}/products`;
    const res = await fetch(url);
    renderProducts(await res.json());
}

function renderProducts(prods) {
    const grid = document.getElementById('catalog-grid');
    grid.innerHTML = prods.map(p => `
        <div class="col">
            <div class="card h-100 shadow-sm">
                <img src="${p.primary_image || ''}" class="card-img-top product-img" onerror="this.src='https://via.placeholder.com/300?text=No+Asset'">
                <div class="card-body">
                    <h5 class="card-title fw-bold">${p.name}</h5>
                    <p class="card-text text-muted small">${p.description}</p>
                    <div class="d-flex justify-content-between align-items-center mt-3">
                        <span class="fw-bold text-primary h5 mb-0">$${p.price.toLocaleString()}</span>
                        <div class="tags">${p.categories.map(c => `<span class="badge bg-light text-dark border me-1">${c}</span>`).join('')}</div>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

init();