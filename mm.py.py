import streamlit as st
import streamlit.components.v1 as components

# Streamlit sahifa sozlamalari
st.set_page_config(
    page_title="SportMax — Sport Do'koni",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Alohida HTML fayl shart emas - barcha mantiq, dizayn va kalkulyator shu yerda:
html_content = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SportMax — Sport Do'koni</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    /* ===== CSS VARIABLES ===== */
    :root {
      --green: #22c55e;
      --green-dark: #16a34a;
      --green-light: #dcfce7;
      --green-mid: #86efac;
      --black: #0a0a0a;
      --gray-900: #111827;
      --gray-800: #1f2937;
      --gray-700: #374151;
      --gray-500: #6b7280;
      --gray-300: #d1d5db;
      --gray-200: #e5e7eb;
      --gray-100: #f3f4f6;
      --gray-50:  #f9fafb;
      --white: #ffffff;
      --red: #ef4444;
      --radius: 10px;
      --shadow-green: 0 8px 28px rgba(34,197,94,0.15);
      --font-display: 'Barlow Condensed', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    /* ===== RESET ===== */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { font-family: var(--font-body); background: var(--gray-50); color: var(--gray-900); line-height: 1.6; }
    .container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }

    /* ===== HEADER ===== */
    header { background: var(--black); position: sticky; top: 0; z-index: 200; border-bottom: 2px solid var(--green); }
    .header__inner { display: flex; align-items: center; justify-content: space-between; height: 62px; gap: 16px; }
    .logo { font-family: var(--font-display); font-size: 26px; font-weight: 900; color: var(--white); letter-spacing: 0.02em; display: flex; align-items: center; gap: 8px; text-decoration: none; }
    .logo em { color: var(--green); font-style: normal; }
    nav { display: flex; align-items: center; gap: 4px; }
    nav a { padding: 6px 13px; border-radius: 6px; font-size: 14px; font-weight: 500; color: #9ca3af; text-decoration: none; transition: all 0.15s; }
    nav a:hover { color: var(--white); background: rgba(255,255,255,0.07); }
    .cart-btn { background: var(--green) !important; color: var(--black) !important; font-weight: 700 !important; border-radius: 8px !important; padding: 8px 16px !important; display: flex; align-items: center; gap: 7px; cursor: pointer; border: none; }
    .cart-btn:hover { background: var(--green-dark) !important; }
    .cart-badge { background: var(--black); color: var(--green); border-radius: 999px; font-size: 11px; font-weight: 700; padding: 1px 7px; min-width: 20px; text-align: center; }

    /* ===== HERO ===== */
    .hero { background: var(--black); padding: 72px 0 64px; position: relative; overflow: hidden; }
    .hero__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 56px; align-items: center; position: relative; z-index: 1; }
    .hero__eyebrow { display: inline-flex; align-items: center; gap: 7px; background: rgba(34,197,94,0.12); border: 1px solid rgba(34,197,94,0.3); color: var(--green); border-radius: 999px; padding: 5px 15px; font-size: 13px; font-weight: 600; margin-bottom: 20px; width: fit-content; }
    .hero__title { font-family: var(--font-display); font-size: 58px; font-weight: 900; color: var(--white); line-height: 1.05; margin-bottom: 18px; text-transform: uppercase; }
    .hero__title em { color: var(--green); font-style: normal; display: block; }
    .hero__sub { font-size: 16px; color: #9ca3af; max-width: 440px; margin-bottom: 34px; }
    .hero__actions { display: flex; gap: 12px; flex-wrap: wrap; }
    
    .btn { display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; font-size: 15px; font-weight: 600; border-radius: 8px; cursor: pointer; border: none; transition: all 0.18s; text-decoration: none; }
    .btn--primary { background: var(--green); color: var(--black); }
    .btn--primary:hover { background: var(--green-dark); transform: translateY(-1px); }
    .btn--ghost { background: transparent; color: var(--white); border: 2px solid rgba(255,255,255,0.2); }
    .btn--ghost:hover { border-color: var(--green); color: var(--green); }
    .btn--full { width: 100%; justify-content: center; margin-top: 10px; }

    .hero__stats { display: flex; gap: 32px; margin-top: 36px; padding-top: 32px; border-top: 1px solid rgba(255,255,255,0.08); }
    .hero__stat strong { display: block; font-family: var(--font-display); font-size: 32px; font-weight: 800; color: var(--green); }
    .hero__stat span { font-size: 13px; color: #6b7280; }
    .hero__img-wrap { border-radius: 16px; overflow: hidden; aspect-ratio: 4/3; background: var(--gray-800); }
    .hero__img-wrap img { width: 100%; height: 100%; object-fit: cover; }

    /* ===== CATALOG ===== */
    section { padding: 72px 0; }
    .section-head { text-align: center; margin-bottom: 48px; }
    .section-eyebrow { display: inline-block; font-size: 13px; font-weight: 600; color: var(--green); text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 10px; }
    .section-title { font-family: var(--font-display); font-size: 38px; font-weight: 800; color: var(--gray-900); text-transform: uppercase; }
    .section-sub { font-size: 15px; color: var(--gray-500); max-width: 480px; margin: 0 auto; }
    
    .cat-tabs { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px; }
    .cat-tab { display: flex; align-items: center; gap: 8px; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; border: 2px solid var(--gray-200); background: var(--white); color: var(--gray-700); transition: all 0.16s; }
    .cat-tab:hover { border-color: var(--green); color: var(--green); }
    .cat-tab.active { background: var(--green); border-color: var(--green); color: var(--black); font-weight: 700; box-shadow: 0 4px 14px rgba(34,197,94,0.25); }

    .products-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; }
    .prod-card { background: var(--white); border-radius: var(--radius); border: 1.5px solid var(--gray-100); overflow: hidden; transition: all 0.2s; display: flex; flex-direction: column; }
    .prod-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-green); border-color: var(--green-mid); }
    .prod-card__img { width: 100%; aspect-ratio: 4/3; object-fit: cover; background: var(--gray-100); font-size: 50px; display: flex; align-items: center; justify-content: center; }
    .prod-card__body { padding: 16px; display: flex; flex-direction: column; flex: 1; }
    .prod-card__badge { display: inline-block; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; background: var(--green-light); color: var(--green-dark); margin-bottom: 8px; align-self: flex-start; }
    .prod-card__badge.hot { background: #fee2e2; color: #b91c1c; }
    .prod-card__badge.new { background: #dbeafe; color: #1d4ed8; }
    .prod-card__name { font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gray-900); margin-bottom: 5px; text-transform: uppercase; }
    .prod-card__desc { font-size: 13px; color: var(--gray-500); margin-bottom: 10px; flex: 1; }
    .prod-card__footer { display: flex; align-items: center; justify-content: space-between; margin-top: auto; }
    .prod-card__price { font-family: var(--font-display); font-size: 20px; font-weight: 800; color: var(--gray-900); }
    .prod-card__price span { font-size: 12px; font-weight: 400; color: var(--gray-500); }

    /* ===== CALCULATOR ===== */
    #calculator { background: var(--white); }
    .calc-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; max-width: 960px; margin: 0 auto; }
    .calc-info h3 { font-family: var(--font-display); font-size: 26px; font-weight: 800; margin-bottom: 14px; text-transform: uppercase; }
    .calc-info p { color: var(--gray-500); margin-bottom: 20px; font-size: 14px; }
    .calc-box { background: var(--gray-50); padding: 28px; border-radius: 14px; border: 1.5px solid var(--gray-100); }
    .field { margin-bottom: 14px; }
    .field label { display: block; font-size: 13px; font-weight: 600; color: var(--gray-700); margin-bottom: 5px; }
    .field input, .field select { width: 100%; padding: 10px 14px; border: 1.5px solid var(--gray-200); border-radius: 7px; font-size: 15px; background: var(--white); color: var(--gray-900); }
    .calc-results-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 16px; }
    .calc-res-card { background: var(--green-light); border: 1.5px solid #a7f3d0; border-radius: 8px; padding: 12px 14px; text-align: center; }
    .calc-res-card p { font-size: 12px; color: var(--green-dark); font-weight: 600; margin-bottom: 3px; }
    .calc-res-card strong { font-family: var(--font-display); font-size: 22px; font-weight: 800; color: #065f46; }

    /* ===== ORDER & SAVAT SECTION ===== */
    #order-section { background: var(--gray-900); color: white; }
    #order-section .section-title { color: white; }
    .order-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; }
    .cart-panel { background: rgba(255,255,255,0.04); border: 1.5px solid rgba(34,197,94,0.3); border-radius: 14px; overflow: hidden; }
    .cart-panel__head { background: var(--green); padding: 16px 20px; display: flex; align-items: center; justify-content: space-between; color: var(--black); }
    .cart-panel__head h3 { font-family: var(--font-display); font-size: 18px; font-weight: 800; text-transform: uppercase; }
    .cart-items { max-height: 340px; overflow-y: auto; padding: 10px; }
    .cart-item { display: flex; align-items: center; justify-content: space-between; padding: 12px 10px; border-bottom: 1px solid rgba(255,255,255,0.08); gap: 10px; }
    .cart-item__name { font-size: 14px; font-weight: 600; color: var(--white); }
    .cart-item__price { color: var(--green); font-weight: 700; font-family: var(--font-display); }
    .cart-item__del { background: none; border: none; color: var(--red); cursor: pointer; font-size: 16px; }
    .cart-empty { text-align: center; padding: 40px; color: var(--gray-500); }
    .cart-footer { padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); }
    .cart-row { display: flex; justify-content: space-between; font-size: 16px; margin-bottom: 15px; }
    .cart-row strong { color: var(--green); font-size: 20px; font-family: var(--font-display); }

    /* ===== MODAL ===== */
    .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 500; align-items: center; justify-content: center; padding: 20px; }
    .modal-overlay.open { display: flex; }
    .modal { background: var(--white); color: var(--black); border-radius: 14px; padding: 32px; max-width: 440px; width: 100%; }
    .modal h3 { font-family: var(--font-display); font-size: 24px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; }
    .modal p { color: var(--gray-500); font-size: 14px; margin-bottom: 20px; }

    /* ===== SERVICES ===== */
    #services { background: var(--gray-100); }
    .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 22px; }
    .svc-card { background: var(--white); border-radius: var(--radius); padding: 28px 24px; text-align: center; border: 1px solid var(--gray-200); }
    .svc-icon { font-size: 40px; margin-bottom: 10px; }

    footer { background: #0d1117; color: #6b7280; padding: 30px 0; text-align: center; font-size: 14px; border-top: 1px solid rgba(255,255,255,0.05); }
    
    @media (max-width: 900px) { .hero__grid, .order-grid, .calc-wrap { grid-template-columns: 1fr; } .hero__img-wrap { display: none; } }
  </style>
</head>
<body>

  <!-- ===== HEADER ===== -->
  <header>
    <div class="container header__inner">
      <a href="#" class="logo">⚡ Sport<em>Max</em></a>
      <nav>
        <a href="#catalog">Katalog</a>
        <a href="#calculator">Kalkulyator</a>
        <a href="#services">Xizmatlar</a>
        <a href="#order-section" class="cart-btn">🛒 Savat <span class="cart-badge" id="cartCountBadge">0</span></a>
      </nav>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section class="hero">
    <div class="container">
      <div class="hero__grid">
        <div>
          <div class="hero__eyebrow">🏆 O'zbekistoning №1 Sport Do'koni</div>
          <h1 class="hero__title">Sport — <em>hayot tarzi!</em></h1>
          <p class="hero__sub">Trenajorlar, sport kiyimi, aksessuarlar va sport oziq-ovqatlari ulgurji narxlarda.</p>
          <div class="hero__actions">
            <a href="#catalog" class="btn btn--primary">💪 Katalogni ko'rish</a>
            <a href="#calculator" class="btn btn--ghost">🧮 Porsiya hisobi</a>
          </div>
        </div>
        <div class="hero__img-wrap">
          <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&auto=format&fit=crop" alt="Sport" />
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CATALOG (6 TA TO'LIQ KATEGORIYA) ===== -->
  <section id="catalog">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Katalog</span>
        <h2 class="section-title">Kategoriyalar bo'yicha mahsulotlar</h2>
      </div>

      <div class="cat-tabs">
        <button class="cat-tab active" onclick="filterCategory('trenajor', this)">🏋️ Trenajorlar</button>
        <button class="cat-tab" onclick="filterCategory('kiyim', this)">👕 Sport Kiyim</button>
        <button class="cat-tab" onclick="filterCategory('aksessuar', this)">🎽 Aksessuarlar</button>
        <button class="cat-tab" onclick="filterCategory('ovqat', this)">🥤 Sport Ovqat</button>
        <button class="cat-tab" onclick="filterCategory('futbol', this)">⚽ Futbol</button>
        <button class="cat-tab" onclick="filterCategory('tennis', this)">🎾 Tennis</button>
      </div>

      <div class="products-grid" id="productsGrid">
        <!-- JavaScript dinamik to'ldiradi -->
      </div>
    </div>
  </section>

  <!-- ===== FITNES & PORSIYA KALKULYATORI ===== -->
  <section id="calculator">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Oziqlanish</span>
        <h2 class="section-title">Kaloriya va Porsiya hisoblagichi</h2>
      </div>
      <div class="calc-wrap">
        <div class="calc-info">
          <h3>Kunlik normani aniqlang</h3>
          <p>Maqsadingiz va jismoniy holatingizga qarab organizmingizga kerakli kaloriya va oqsil (protein) miqdorini aniq hisoblang.</p>
        </div>
        <div class="calc-box">
          <div class="field">
            <label>Vazningiz (kg)</label>
            <input type="number" id="calcWeight" value="70" oninput="calculateFitness()" />
          </div>
          <div class="field">
            <label>Maqsad</label>
            <select id="calcGoal" onchange="calculateFitness()">
              <option value="gain">Mushak yig'ish (Vazn olish)</option>
              <option value="lose">Ozish (Yog' eritish)</option>
              <option value="maintain">Formani saqlash</option>
            </select>
          </div>
          <div class="calc-results-grid">
            <div class="calc-res-card">
              <p>Tavsiya etilgan kaloriya</p>
              <strong id="resCalories">2400 kkal</strong>
            </div>
            <div class="calc-res-card">
              <p>Kerakli Protein (Oqsil)</p>
              <strong id="resProtein">140 gr</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== XIZMATLAR ===== -->
  <section id="services">
    <div class="container">
      <div class="services-grid">
        <div class="svc-card"><div class="svc-icon">🚚</div><h3>Tez Yetkazish</h3><p>O'zbekiston bo'ylab 1 kunda yetkazib berish.</p></div>
        <div class="svc-card"><div class="svc-icon">🛠️</div><h3>O'rnatib berish</h3><p>Katta trenajorlarni bepul yig'ish xizmati.</p></div>
        <div class="svc-card"><div class="svc-icon">🛡️</div><h3>Kafolat</h3><p>Barcha mahsulotlarga 1 yilgacha rasmiy kafolat.</p></div>
      </div>
    </div>
  </section>

  <!-- ===== BUYURTMA VA SAVATCHA PANEL ===== -->
  <section id="order-section">
    <div class="container">
      <div class="order-grid">
        <div>
          <h2 class="section-title">Sizning Savatchangiz</h2>
          <p style="color: #9ca3af; margin-bottom: 20px;">Tanlangan mahsulotlarni tekshiring va buyurtmani rasmiylashtiring.</p>
        </div>
        <div class="cart-panel">
          <div class="cart-panel__head"><h3>Savat</h3></div>
          <div class="cart-items" id="cartItemsList">
            <div class="cart-empty">Savatchangiz bo'sh</div>
          </div>
          <div class="cart-footer">
            <div class="cart-row"><span>Jami summa:</span><strong id="cartTotalPrice">0 so'm</strong></div>
            <button class="order-btn" id="checkoutBtn" onclick="openModal()" disabled>Buyurtma berish</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== BUYURTMA MODAL OYNASI ===== -->
  <div class="modal-overlay" id="orderModal">
    <div class="modal">
      <h3>Xaridni tasdiqlash</h3>
      <p>Ma'lumotlaringizni qoldiring, operatorimiz tez orada aloqaga chiqadi.</p>
      <div class="field"><label>Ismingiz</label><input type="text" id="custName" placeholder="Ism familiya" /></div>
      <div class="field"><label>Telefon raqamingiz</label><input type="tel" id="custPhone" value="+998" /></div>
      <div class="modal-actions">
        <button class="btn btn--primary" onclick="submitOrder()">Tasdiqlash</button>
        <button class="btn btn--outline-dark" onclick="closeModal()">Yopish</button>
      </div>
    </div>
  </div>

  <footer>
    <p>&copy; 2026 SportMax do'koni. Barcha huquqlar himoyalangan.</p>
  </footer>

  <script>
    // MAHSULOTLAR BAZASI (Barcha 6 ta kategoriya qamrab olingan)
    const database = [
      { id: 1, cat: 'trenajor', name: 'Shtanga To\'plami 100 kg', price: 2850000, desc: 'Professional sifatli temir shtanga va disklar.', badge: 'HOT', bType: 'hot' },
      { id: 2, cat: 'trenajor', name: 'Yugurish Yo\'lagi Pro', price: 8900000, desc: '15 tezlik darajasi, LED sensorli ekran.', badge: 'YANGI', bType: 'new' },
      { id: 3, cat: 'kiyim', name: 'Kompression Futbolka DryFit', price: 185000, desc: 'Namlikni tez o\'tkazuvchi professional mato.', badge: 'TOP', bType: 'hot' },
      { id: 4, cat: 'kiyim', name: 'Sport Shimi Nike Tech', price: 320000, desc: 'Kundalik va mashqlar uchun juda qulay.', badge: 'AKSIYA', bType: 'sale' },
      { id: 5, cat: 'aksessuar', name: 'Fitnes Rezinalari To\'plami', price: 95000, desc: '5 xil yuklama darajasiga ega rezinalar.', badge: 'OMBORDA', bType: '' },
      { id: 6, cat: 'ovqat', name: 'Whey Protein 2.2 kg', price: 650000, desc: 'Mushak o\'sishi uchun yuqori sifatli oqsil.', badge: 'TOP', bType: 'hot' },
      { id: 7, cat: 'futbol', name: 'Futbol To\'pi Adidas UEFA', price: 450000, desc: 'Chidamlilik va mukammal nazorat uchun.', badge: 'ORIGINAL', bType: 'new' },
      { id: 8, cat: 'tennis', name: 'Tennis Raketkasi Wilson', price: 780000, desc: 'Professional tennischilar tanlovi.', badge: 'PREMIUM', bType: 'hot' }
    ];

    let cart = [];

    // KATEGORIYA FILTRLASH
    function filterCategory(category, element) {
      document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
      if(element) element.classList.add('active');

      const grid = document.getElementById('productsGrid');
      grid.innerHTML = '';

      const filtered = database.filter(p => p.cat === category);
      
      filtered.forEach(p => {
        grid.innerHTML += `
          <div class="prod-card">
            <div class="prod-card__img">📦</div>
            <div class="prod-card__body">
              \${p.badge ? `<span class="prod-card__badge \${p.bType}">\${p.badge}</span>` : ''}
              <div class="prod-card__name">\${p.name}</div>
              <div class="prod-card__desc">\${p.desc}</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">\${p.price.toLocaleString()} <span>so'm</span></div>
                <button class="btn btn--primary" style="padding: 6px 12px; font-size: 13px;" onclick="addToCart(\${p.id})">+ Savat</button>
              </div>
            </div>
          </div>
        `;
      });
    }

    // SAVAT LOGIKASI
    function addToCart(id) {
      const item = database.find(p => p.id === id);
      cart.push(item);
      renderCart();
    }

    function removeFromCart(index) {
      cart.splice(index, 1);
      renderCart();
    }

    function renderCart() {
      document.getElementById('cartCountBadge').innerText = cart.length;
      const list = document.getElementById('cartItemsList');
      const checkoutBtn = document.getElementById('checkoutBtn');
      
      if(cart.length === 0) {
        list.innerHTML = '<div class="cart-empty">Savatchangiz bo\'sh</div>';
        document.getElementById('cartTotalPrice').innerText = "0 so'm";
        checkoutBtn.disabled = true;
        return;
      }

      checkoutBtn.disabled = false;
      list.innerHTML = '';
      let total = 0;

      cart.forEach((item, index) => {
        total += item.price;
        list.innerHTML += `
          <div class="cart-item">
            <span class="cart-item__name">\${item.name}</span>
            <span class="cart-item__price">\${item.price.toLocaleString()} so'm</span>
            <button class="cart-item__del" onclick="removeFromCart(\${index})">✕</button>
          </div>
        `;
      });

      document.getElementById('cartTotalPrice').innerText = total.toLocaleString() + " so'm";
    }

    // INTERFAYS & MODAL
    function openModal() { document.getElementById('orderModal').classList.add('open'); }
    function closeModal() { document.getElementById('orderModal').classList.remove('open'); }
    function submitOrder() {
      const name = document.getElementById('custName').value;
      if(!name.trim() || name === "Ism familiya") { alert("Iltimos ismingizni kiriting!"); return; }
      alert("Rahmat, " + name + "! Buyurtmangiz muvaffaqiyatli qabul qilindi.");
      cart = [];
      renderCart();
      closeModal();
    }

    // FITNES KALKULYATORI
    function calculateFitness() {
      const weight = parseFloat(document.getElementById('calcWeight').value) || 70;
      const goal = document.getElementById('calcGoal').value;
      let calories = 2000;
      let protein = weight * 1.5;

      if(goal === 'gain') { calories = Math.round(weight * 35 + 400); protein = weight * 2; }
      else if(goal === 'lose') { calories = Math.round(weight * 30 - 300); protein = weight * 1.8; }
      else { calories = Math.round(weight * 32); protein = weight * 1.6; }

      document.getElementById('resCalories').innerText = calories + " kkal";
      document.getElementById('resProtein').innerText = Math.round(protein) + " gr";
    }

    // Boshlang'ich yuklanish
    window.onload = function() {
      filterCategory('trenajor', null);
      calculateFitness();
    };
  </script>
</body>
</html>
"""

# Streamlitga xavfsiz uzatish
components.html(html_content, height=1800, scrolling=True)
