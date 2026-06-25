import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="QurilishMart — Qurilish Mollari",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu { visibility: hidden; }
    header[data-testid="stHeader"] { display: none; }
    footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>QurilishMart — Qurilish Mollari</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    /* ===== CSS VARIABLES ===== */
    :root {
      --orange: #f97316;
      --orange-dark: #ea580c;
      --orange-light: #fff7ed;
      --orange-mid: #fed7aa;
      --gray-900: #111827;
      --gray-700: #374151;
      --gray-500: #6b7280;
      --gray-300: #d1d5db;
      --gray-100: #f3f4f6;
      --gray-50: #f9fafb;
      --white: #ffffff;
      --green: #059669;
      --green-light: #ecfdf5;
      --radius: 10px;
      --shadow: 0 4px 16px rgba(0,0,0,0.08);
      --shadow-hover: 0 8px 28px rgba(249,115,22,0.18);
      --font-display: 'Space Grotesk', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    /* ===== RESET ===== */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--font-body);
      background: var(--gray-50);
      color: var(--gray-900);
      line-height: 1.6;
    }
    img { max-width: 100%; display: block; }
    a { text-decoration: none; }

    /* ===== LAYOUT ===== */
    .container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* ===== HEADER ===== */
    header {
      background: var(--white);
      border-bottom: 1.5px solid var(--gray-100);
      position: sticky;
      top: 0;
      z-index: 200;
      padding: 14px 0;
    }
    .header__inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }
    .logo {
      font-family: var(--font-display);
      font-size: 22px;
      font-weight: 700;
      color: var(--gray-900);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .logo span { color: var(--orange); }
    nav { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
    nav a {
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 500;
      color: var(--gray-700);
      transition: background 0.18s, color 0.18s;
    }
    nav a:hover { background: var(--orange-light); color: var(--orange-dark); }
    .cart-btn {
      background: var(--orange);
      color: var(--white) !important;
      border-radius: 8px;
      padding: 8px 16px !important;
      font-weight: 600 !important;
      display: flex;
      align-items: center;
      gap: 6px;
      position: relative;
    }
    .cart-btn:hover { background: var(--orange-dark) !important; }
    .cart-count {
      background: var(--gray-900);
      color: var(--white);
      border-radius: 999px;
      font-size: 11px;
      padding: 1px 7px;
      font-weight: 700;
      min-width: 20px;
      text-align: center;
    }

    /* ===== HERO ===== */
    .hero {
      padding: 72px 0 64px;
      background: linear-gradient(135deg, #fff7ed 0%, #fef3c7 60%, #fff 100%);
      position: relative;
      overflow: hidden;
    }
    .hero::after {
      content: '';
      position: absolute;
      right: -80px; top: -80px;
      width: 420px; height: 420px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(249,115,22,0.12), transparent 70%);
      pointer-events: none;
    }
    .hero__grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 48px;
      align-items: center;
    }
    .hero__badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--orange-mid);
      color: var(--orange-dark);
      border-radius: 999px;
      padding: 4px 14px;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 18px;
    }
    .hero__title {
      font-family: var(--font-display);
      font-size: 48px;
      font-weight: 700;
      line-height: 1.15;
      margin-bottom: 18px;
      color: var(--gray-900);
    }
    .hero__title em { color: var(--orange); font-style: normal; }
    .hero__sub {
      font-size: 17px;
      color: var(--gray-500);
      max-width: 480px;
      margin-bottom: 32px;
    }
    .hero__actions { display: flex; gap: 12px; flex-wrap: wrap; }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 24px;
      font-size: 15px;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      border: none;
      transition: all 0.18s;
      font-family: var(--font-body);
    }
    .btn--primary { background: var(--orange); color: var(--white); }
    .btn--primary:hover { background: var(--orange-dark); transform: translateY(-1px); box-shadow: var(--shadow-hover); }
    .btn--outline { background: transparent; color: var(--gray-700); border: 2px solid var(--gray-300); }
    .btn--outline:hover { border-color: var(--orange); color: var(--orange); }
    .hero__stats {
      display: flex;
      gap: 28px;
      margin-top: 32px;
    }
    .hero__stat { text-align: left; }
    .hero__stat strong {
      display: block;
      font-family: var(--font-display);
      font-size: 28px;
      font-weight: 700;
      color: var(--orange);
    }
    .hero__stat span { font-size: 13px; color: var(--gray-500); }
    .hero__img-wrap {
      border-radius: 16px;
      overflow: hidden;
      box-shadow: var(--shadow);
      aspect-ratio: 4/3;
      background: var(--gray-100);
    }
    .hero__img-wrap img { width: 100%; height: 100%; object-fit: cover; }

    /* ===== SECTION COMMON ===== */
    section { padding: 72px 0; }
    .section-head {
      text-align: center;
      margin-bottom: 48px;
    }
    .section-eyebrow {
      display: inline-block;
      font-size: 13px;
      font-weight: 600;
      color: var(--orange);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 10px;
    }
    .section-title {
      font-family: var(--font-display);
      font-size: 34px;
      font-weight: 700;
      color: var(--gray-900);
      margin-bottom: 10px;
    }
    .section-sub {
      font-size: 16px;
      color: var(--gray-500);
      max-width: 500px;
      margin: 0 auto;
    }

    /* ===== CATEGORIES ===== */
    #catalog { background: var(--white); }
    .cat-tabs {
      display: flex;
      gap: 10px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 40px;
    }
    .cat-tab {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      border: 2px solid var(--gray-200, #e5e7eb);
      background: var(--white);
      color: var(--gray-700);
      transition: all 0.18s;
    }
    .cat-tab:hover { border-color: var(--orange); color: var(--orange); }
    .cat-tab.active {
      background: var(--orange);
      border-color: var(--orange);
      color: var(--white);
      box-shadow: 0 4px 12px rgba(249,115,22,0.3);
    }
    .cat-tab .tab-icon { font-size: 18px; }

    .products-panel { display: none; }
    .products-panel.active { display: block; }
    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 22px;
    }

    /* ===== PRODUCT CARD ===== */
    .prod-card {
      background: var(--white);
      border-radius: var(--radius);
      border: 1.5px solid var(--gray-100);
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
      display: flex;
      flex-direction: column;
    }
    .prod-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-hover);
      border-color: var(--orange-mid);
    }
    .prod-card__img {
      width: 100%;
      aspect-ratio: 4/3;
      object-fit: cover;
      background: var(--gray-100);
    }
    .prod-card__body {
      padding: 16px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .prod-card__badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--orange-light);
      color: var(--orange-dark);
      margin-bottom: 8px;
      align-self: flex-start;
    }
    .prod-card__name {
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 600;
      color: var(--gray-900);
      margin-bottom: 6px;
      line-height: 1.35;
    }
    .prod-card__desc {
      font-size: 13px;
      color: var(--gray-500);
      margin-bottom: 14px;
      flex: 1;
    }
    .prod-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
    }
    .prod-card__price {
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 700;
      color: var(--gray-900);
    }
    .prod-card__price span {
      font-size: 12px;
      font-weight: 400;
      color: var(--gray-500);
    }
    .add-btn {
      background: var(--orange);
      color: var(--white);
      border: none;
      border-radius: 7px;
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.16s, transform 0.12s;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .add-btn:hover { background: var(--orange-dark); transform: scale(1.04); }
    .add-btn.added { background: var(--green); }

    /* ===== RECOMMENDED ===== */
    #recommended { background: var(--gray-50); }
    .rec-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
    }
    .rec-card {
      background: var(--white);
      border-radius: var(--radius);
      border: 1.5px solid var(--gray-100);
      overflow: hidden;
      transition: transform 0.18s, box-shadow 0.18s;
      cursor: pointer;
    }
    .rec-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-hover); }
    .rec-card__img {
      width: 100%;
      aspect-ratio: 1;
      object-fit: cover;
      background: var(--gray-100);
    }
    .rec-card__body { padding: 14px; }
    .rec-rank {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px; height: 22px;
      border-radius: 50%;
      background: var(--orange);
      color: var(--white);
      font-size: 11px;
      font-weight: 700;
      margin-bottom: 6px;
    }
    .rec-card__name {
      font-size: 14px;
      font-weight: 600;
      color: var(--gray-900);
      margin-bottom: 4px;
      line-height: 1.3;
    }
    .rec-card__cat {
      font-size: 12px;
      color: var(--orange);
      font-weight: 500;
      margin-bottom: 8px;
    }
    .rec-card__price {
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      color: var(--gray-900);
    }
    .rec-card__price small { font-size: 11px; font-weight: 400; color: var(--gray-500); }
    .rec-add-btn {
      display: block;
      width: 100%;
      margin-top: 10px;
      padding: 7px;
      border: none;
      border-radius: 6px;
      background: var(--orange-light);
      color: var(--orange-dark);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.16s;
    }
    .rec-add-btn:hover { background: var(--orange); color: var(--white); }

    /* ===== CALCULATOR ===== */
    #calculator { background: var(--white); }
    .calc-wrap {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: start;
      max-width: 900px;
      margin: 0 auto;
    }
    .calc-info h3 {
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 14px;
    }
    .calc-info p { color: var(--gray-500); margin-bottom: 20px; }
    .calc-tips { list-style: none; }
    .calc-tips li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 14px;
      color: var(--gray-700);
      margin-bottom: 12px;
    }
    .calc-tips li span { color: var(--orange); font-size: 18px; }
    .calc-box {
      background: var(--gray-50);
      padding: 30px;
      border-radius: 14px;
      border: 1.5px solid var(--gray-100);
    }
    .calc-tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
    }
    .calc-tab-btn {
      flex: 1;
      padding: 8px;
      border: 2px solid var(--gray-200, #e5e7eb);
      border-radius: 7px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      background: var(--white);
      color: var(--gray-700);
      transition: all 0.16s;
    }
    .calc-tab-btn.active {
      background: var(--orange);
      border-color: var(--orange);
      color: var(--white);
    }
    .calc-panel { display: none; }
    .calc-panel.active { display: block; }
    .field { margin-bottom: 16px; }
    .field label { display: block; font-size: 13px; font-weight: 600; color: var(--gray-700); margin-bottom: 6px; }
    .field input, .field select {
      width: 100%;
      padding: 10px 14px;
      border: 1.5px solid var(--gray-200, #e5e7eb);
      border-radius: 7px;
      font-size: 15px;
      font-family: var(--font-body);
      background: var(--white);
      color: var(--gray-900);
      transition: border-color 0.16s;
    }
    .field input:focus, .field select:focus { outline: none; border-color: var(--orange); }
    .calc-result {
      background: var(--green-light);
      border-radius: 8px;
      padding: 16px;
      text-align: center;
      margin-top: 18px;
      border: 1.5px solid #a7f3d0;
    }
    .calc-result p { font-size: 13px; color: var(--green); font-weight: 500; margin-bottom: 4px; }
    .calc-result strong {
      font-family: var(--font-display);
      font-size: 26px;
      font-weight: 700;
      color: #065f46;
    }

    /* ===== DELIVERY ===== */
    #delivery { background: var(--gray-50); }
    .delivery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 22px;
    }
    .del-card {
      background: var(--white);
      border-radius: var(--radius);
      padding: 28px 24px;
      border: 1.5px solid var(--gray-100);
      text-align: center;
      transition: box-shadow 0.18s;
    }
    .del-card:hover { box-shadow: var(--shadow); }
    .del-icon {
      font-size: 42px;
      margin-bottom: 14px;
    }
    .del-card h3 {
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .del-card p { font-size: 14px; color: var(--gray-500); line-height: 1.55; }

    /* ===== B2B ===== */
    #b2b { background: var(--gray-900); }
    #b2b .section-title { color: var(--white); }
    #b2b .section-eyebrow { color: var(--orange); }
    #b2b .section-sub { color: #9ca3af; }
    .b2b-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 48px;
      align-items: start;
    }
    .b2b-perks { display: flex; flex-direction: column; gap: 18px; }
    .b2b-perk {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      padding: 18px;
      background: rgba(255,255,255,0.05);
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.08);
    }
    .b2b-perk__icon {
      font-size: 28px;
      flex-shrink: 0;
    }
    .b2b-perk h4 { color: var(--white); font-weight: 600; font-size: 15px; margin-bottom: 4px; }
    .b2b-perk p { color: #9ca3af; font-size: 13px; }

    /* ===== CART / ORDER SUMMARY ===== */
    .b2b-order {
      background: rgba(255,255,255,0.05);
      border: 1.5px solid rgba(249,115,22,0.3);
      border-radius: 14px;
      overflow: hidden;
    }
    .b2b-order__head {
      background: var(--orange);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .b2b-order__head h3 { color: var(--white); font-family: var(--font-display); font-size: 16px; font-weight: 700; }
    .b2b-order__head span { color: rgba(255,255,255,0.75); font-size: 13px; }
    .b2b-order__body { padding: 0; }
    .cart-items { max-height: 340px; overflow-y: auto; }
    .cart-items::-webkit-scrollbar { width: 4px; }
    .cart-items::-webkit-scrollbar-thumb { background: rgba(249,115,22,0.3); border-radius: 2px; }
    .cart-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 20px;
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }
    .cart-item__img {
      width: 52px;
      height: 52px;
      border-radius: 6px;
      object-fit: cover;
      background: rgba(255,255,255,0.1);
      flex-shrink: 0;
    }
    .cart-item__info { flex: 1; min-width: 0; }
    .cart-item__name { color: var(--white); font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .cart-item__cat { color: #9ca3af; font-size: 11px; }
    .cart-item__qty {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .qty-btn {
      width: 26px; height: 26px;
      border-radius: 5px;
      border: 1px solid rgba(255,255,255,0.15);
      background: rgba(255,255,255,0.07);
      color: var(--white);
      font-size: 16px;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: background 0.15s;
      font-family: var(--font-body);
    }
    .qty-btn:hover { background: var(--orange); border-color: var(--orange); }
    .qty-val { color: var(--white); font-size: 14px; font-weight: 600; min-width: 24px; text-align: center; }
    .cart-item__price { color: var(--orange); font-family: var(--font-display); font-size: 14px; font-weight: 700; min-width: 90px; text-align: right; }
    .cart-item__del {
      color: #6b7280;
      background: none;
      border: none;
      cursor: pointer;
      font-size: 16px;
      padding: 4px;
      transition: color 0.15s;
    }
    .cart-item__del:hover { color: #f87171; }

    .cart-empty {
      text-align: center;
      padding: 40px 20px;
      color: #6b7280;
    }
    .cart-empty .empty-icon { font-size: 48px; margin-bottom: 12px; }
    .cart-empty p { font-size: 14px; }

    .cart-footer {
      padding: 18px 20px;
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    .cart-totals { margin-bottom: 16px; }
    .cart-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 14px;
      color: #9ca3af;
    }
    .cart-row.total {
      font-size: 17px;
      font-weight: 700;
      color: var(--white);
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 10px;
      margin-top: 8px;
    }
    .cart-row.total span { color: var(--orange); font-family: var(--font-display); }
    .order-btn {
      display: block;
      width: 100%;
      padding: 13px;
      background: var(--orange);
      color: var(--white);
      border: none;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.16s, transform 0.12s;
      font-family: var(--font-display);
      letter-spacing: 0.02em;
    }
    .order-btn:hover { background: var(--orange-dark); transform: translateY(-1px); }
    .order-btn:disabled { background: #374151; cursor: not-allowed; transform: none; }

    /* ===== TOAST ===== */
    .toast {
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: var(--gray-900);
      color: var(--white);
      padding: 12px 20px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 500;
      z-index: 9999;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
      border-left: 4px solid var(--orange);
      display: flex;
      align-items: center;
      gap: 10px;
      transform: translateX(120%);
      transition: transform 0.3s cubic-bezier(.34,1.56,.64,1);
    }
    .toast.show { transform: translateX(0); }

    /* ===== FOOTER ===== */
    footer {
      background: #0d1117;
      color: #6b7280;
      padding: 48px 0 28px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 40px;
    }
    .footer-brand .logo { margin-bottom: 12px; }
    .footer-brand p { font-size: 14px; line-height: 1.6; margin-bottom: 16px; }
    .footer-col h4 { color: var(--white); font-size: 15px; font-weight: 600; margin-bottom: 14px; }
    .footer-col a { display: block; color: #6b7280; font-size: 14px; margin-bottom: 9px; transition: color 0.15s; }
    .footer-col a:hover { color: var(--orange); }
    .footer-bottom {
      border-top: 1px solid rgba(255,255,255,0.07);
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
    }
    .footer-bottom a { color: #6b7280; }
    .footer-bottom a:hover { color: var(--orange); }

    /* ===== MODAL ===== */
    .modal-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.55);
      z-index: 500;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-overlay.open { display: flex; }
    .modal {
      background: var(--white);
      border-radius: 14px;
      padding: 32px;
      max-width: 440px;
      width: 100%;
      animation: popIn 0.25s ease;
    }
    @keyframes popIn { from { transform: scale(0.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    .modal h3 { font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 8px; }
    .modal p { color: var(--gray-500); font-size: 14px; margin-bottom: 22px; }
    .modal-actions { display: flex; gap: 10px; }
    .modal-actions .btn { flex: 1; justify-content: center; }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 900px) {
      .hero__grid { grid-template-columns: 1fr; }
      .hero__img-wrap { display: none; }
      .hero__title { font-size: 36px; }
      .b2b-grid { grid-template-columns: 1fr; }
      .calc-wrap { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 600px) {
      .hero__title { font-size: 28px; }
      .section-title { font-size: 26px; }
      nav a:not(.cart-btn) { display: none; }
      .footer-grid { grid-template-columns: 1fr; }
      .products-grid { grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); }
    }
  </style>
</head>
<body>

  <!-- ===== HEADER ===== -->
  <header>
    <div class="container header__inner">
      <a href="#" class="logo">⚙ Qurilish<span>Mart</span></a>
      <nav>
        <a href="#catalog">Katalog</a>
        <a href="#recommended">Tavsiyalar</a>
        <a href="#calculator">Kalkulyator</a>
        <a href="#delivery">Xizmatlar</a>
        <a href="#b2b">B2B</a>
        <a href="#b2b" class="cart-btn">🛒 Savat <span class="cart-count" id="cartCountBadge">0</span></a>
      </nav>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section class="hero">
    <div class="container">
      <div class="hero__grid">
        <div>
          <div class="hero__badge">⚡ Toshkent bo'yicha kuni yetkazib beramiz</div>
          <h1 class="hero__title">Qurilish mollari —<br><em>tez, arzon, ishonchli</em></h1>
          <p class="hero__sub">Sement, kafel, bo'yoq, laminat va yana 500+ mahsulot. Prorablar va uy egalari uchun eng yaxshi narxlar.</p>
          <div class="hero__actions">
            <a href="#catalog" class="btn btn--primary">🏗 Katalogni ko'rish</a>
            <a href="#b2b" class="btn btn--outline">💼 B2B Hamkorlik</a>
          </div>
          <div class="hero__stats">
            <div class="hero__stat"><strong>500+</strong><span>Mahsulot turi</span></div>
            <div class="hero__stat"><strong>2,400+</strong><span>Mijozlar</span></div>
            <div class="hero__stat"><strong>1 kun</strong><span>Yetkazib berish</span></div>
          </div>
        </div>
        <div class="hero__img-wrap">
          <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&auto=format&fit=crop" alt="Qurilish mollari ombori" />
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CATEGORIES ===== -->
  <section id="catalog">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Katalog</span>
        <h2 class="section-title">Kategoriyalar bo'yicha mahsulotlar</h2>
        <p class="section-sub">Har bir kategoriya uchun sifatli mahsulotlarni tanlang</p>
      </div>

      <div class="cat-tabs">
        <button class="cat-tab active" onclick="switchCat('sement')" id="tab-sement">
          <span class="tab-icon">🪣</span> Sement va Qurilish
        </button>
        <button class="cat-tab" onclick="switchCat('kafel')" id="tab-kafel">
          <span class="tab-icon">🪟</span> Kafel va Plitka
        </button>
        <button class="cat-tab" onclick="switchCat('boyoq')" id="tab-boyoq">
          <span class="tab-icon">🎨</span> Bo'yoq va Lak
        </button>
        <button class="cat-tab" onclick="switchCat('laminat')" id="tab-laminat">
          <span class="tab-icon">🪵</span> Laminat va Parket
        </button>
      </div>

      <!-- SEMENT PANEL -->
      <div class="products-panel active" id="panel-sement">
        <div class="products-grid">
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&auto=format&fit=crop" alt="Portland Sement M400" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Portland Sement M400 (50 kg)</div>
              <div class="prod-card__desc">Poydevor va konstruksiyalar uchun. Yuqori mustahkamlik, tez qotish.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">78 000 <span>so'm/qop</span></div>
                <button class="add-btn" onclick="addToCart(this,'Portland Sement M400','sement','https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=100','78000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=400&auto=format&fit=crop" alt="Sement M500" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Portland Sement M500 (50 kg)</div>
              <div class="prod-card__desc">Eng mustahkam turdagi sement. Ko'p qavatli binolar uchun.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">92 000 <span>so'm/qop</span></div>
                <button class="add-btn" onclick="addToCart(this,'Portland Sement M500','sement','https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=100','92000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=400&auto=format&fit=crop" alt="Qum" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Qurilish Qumi (1 tonna)</div>
              <div class="prod-card__desc">Tozalangan, quritilgan qurilish qumi. Eritma tayyorlash uchun.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">320 000 <span>so'm/t</span></div>
                <button class="add-btn" onclick="addToCart(this,'Qurilish Qumi','sement','https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=100','320000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=400&auto=format&fit=crop" alt="Shagal" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Mavjud</span>
              <div class="prod-card__name">Shag'al (1 tonna)</div>
              <div class="prod-card__desc">Beton aralashmasi uchun. O'lchami 5–20 mm.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">280 000 <span>so'm/t</span></div>
                <button class="add-btn" onclick="addToCart(this,'Shag\'al','sement','https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=100','280000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1590593162201-f67611a18b87?w=400&auto=format&fit=crop" alt="Armatura" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Ko'p sotiladi</span>
              <div class="prod-card__name">Armatura d=12 mm (1 m)</div>
              <div class="prod-card__desc">Temir-beton konstruksiyalar uchun. GOST standartida.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">18 500 <span>so'm/m</span></div>
                <button class="add-btn" onclick="addToCart(this,'Armatura d=12mm','sement','https://images.unsplash.com/photo-1590593162201-f67611a18b87?w=100','18500')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1597173791720-87ec8a2a9bef?w=400&auto=format&fit=crop" alt="G'isht" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Qurilish G'ishti (1 dona)</div>
              <div class="prod-card__desc">Standart o'lcham 250×120×65 mm. Devor qurilishi uchun.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">1 200 <span>so'm/dona</span></div>
                <button class="add-btn" onclick="addToCart(this,'Qurilish G\'ishti','sement','https://images.unsplash.com/photo-1597173791720-87ec8a2a9bef?w=100','1200')">+ Savat</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- KAFEL PANEL -->
      <div class="products-panel" id="panel-kafel">
        <div class="products-grid">
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400&auto=format&fit=crop" alt="Oshxona kafel" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Ko'p sotiladi</span>
              <div class="prod-card__name">Oshxona Kafel "Marbella" 30×60</div>
              <div class="prod-card__desc">Suv o'tkazmaydigan, chiroyli naqsh. Oshxona va hammom uchun.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">85 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Kafel Marbella 30×60','kafel','https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=100','85000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&auto=format&fit=crop" alt="Pol kafel" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Pol Plitka "Granito" 60×60</div>
              <div class="prod-card__desc">Granit effekti. Ko'cha va ichki makonlar uchun bardoshli.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">120 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Pol Plitka Granito 60×60','kafel','https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=100','120000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1574362848149-11496d93a7c7?w=400&auto=format&fit=crop" alt="Hammom kafel" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Yangi</span>
              <div class="prod-card__name">Hammom Kafel "Aqua" 20×40</div>
              <div class="prod-card__desc">Namga chidamli. Hammom va WC uchun maxsus seriya.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">65 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Hammom Kafel Aqua 20×40','kafel','https://images.unsplash.com/photo-1574362848149-11496d93a7c7?w=100','65000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1615529479858-75c11cefbe38?w=400&auto=format&fit=crop" alt="Tashqi kafel" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Aksiya</span>
              <div class="prod-card__name">Dekor Plitka "Terra" 30×30</div>
              <div class="prod-card__desc">Zangori naqsh. Sahni va balkon uchun. Sovuqqa chidamli.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">72 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Dekor Plitka Terra 30×30','kafel','https://images.unsplash.com/photo-1615529479858-75c11cefbe38?w=100','72000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=400&auto=format&fit=crop" alt="Mozaika" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Premium</span>
              <div class="prod-card__name">Mozaika Kafel 30×30 (1 varaq)</div>
              <div class="prod-card__desc">Shisha mozaika. Havza va devor bezagi uchun.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">145 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Mozaika Kafel','kafel','https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=100','145000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1637614589439-02a11a59f8cf?w=400&auto=format&fit=crop" alt="Kafel yelimi" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Kafel Yopishqogi C1 (25 kg)</div>
              <div class="prod-card__desc">Plitka yopishtirishga mo'ljallangan professional yelim.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">45 000 <span>so'm/qop</span></div>
                <button class="add-btn" onclick="addToCart(this,'Kafel Yopishqogi C1','kafel','https://images.unsplash.com/photo-1637614589439-02a11a59f8cf?w=100','45000')">+ Savat</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- BO'YOQ PANEL -->
      <div class="products-panel" id="panel-boyoq">
        <div class="products-grid">
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=400&auto=format&fit=crop" alt="Devor bo'yog'i" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Ko'p sotiladi</span>
              <div class="prod-card__name">Interior Emulsion Bo'yoq (10 L)</div>
              <div class="prod-card__desc">Ichki devorlar uchun. Yuvimga chidamli, 100+ rang.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">185 000 <span>so'm/qut</span></div>
                <button class="add-btn" onclick="addToCart(this,'Interior Emulsion Bo\'yoq','boyoq','https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=100','185000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=400&auto=format&fit=crop" alt="Fasad bo'yog'i" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Fasad Bo'yoq "Exterior" (15 L)</div>
              <div class="prod-card__desc">Tashqi devorlar uchun. UV-himoyali, yomg'irga chidamli.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">320 000 <span>so'm/qut</span></div>
                <button class="add-btn" onclick="addToCart(this,'Fasad Bo\'yoq Exterior','boyoq','https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=100','320000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400&auto=format&fit=crop" alt="Lak" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Professional</span>
              <div class="prod-card__name">Parket Laki "Gloss" (5 L)</div>
              <div class="prod-card__desc">Parket va yog'och sirtlar uchun. Yarqiroq qoplama.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">240 000 <span>so'm/qut</span></div>
                <button class="add-btn" onclick="addToCart(this,'Parket Laki Gloss','boyoq','https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=100','240000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&auto=format&fit=crop" alt="Grunt" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Talab ko'p</span>
              <div class="prod-card__name">Grunt Qoplaması "Prima" (10 L)</div>
              <div class="prod-card__desc">Bo'yoq ostiga qo'llash uchun. Yopishqoqlikni oshiradi.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">95 000 <span>so'm/qut</span></div>
                <button class="add-btn" onclick="addToCart(this,'Grunt Prima','boyoq','https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=100','95000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=400&auto=format&fit=crop" alt="Shpatlevka" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">Shpaklyovka "Gloss" (20 kg)</div>
              <div class="prod-card__desc">Devor tekislashtirish uchun. Ingichka va qalin qatlamlar.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">68 000 <span>so'm/qop</span></div>
                <button class="add-btn" onclick="addToCart(this,'Shpaklyovka Gloss','boyoq','https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=100','68000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=400&auto=format&fit=crop" alt="Boyoq vositalari" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Yangi</span>
              <div class="prod-card__name">Antifungal Bo'yoq (5 L)</div>
              <div class="prod-card__desc">Zamburug' va namlikka qarshi maxsus himoyali qoplama.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">155 000 <span>so'm/qut</span></div>
                <button class="add-btn" onclick="addToCart(this,'Antifungal Bo\'yoq','boyoq','https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=100','155000')">+ Savat</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- LAMINAT PANEL -->
      <div class="products-panel" id="panel-laminat">
        <div class="products-grid">
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1562663474-6cbb3eaa4d14?w=400&auto=format&fit=crop" alt="Laminat" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Ko'p sotiladi</span>
              <div class="prod-card__name">Laminat "Oak Natural" 8mm AC4</div>
              <div class="prod-card__desc">Eman naqshi. Yuqori bosimga chidamli. 1 qutida 2.13 m².</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">145 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Laminat Oak Natural 8mm','laminat','https://images.unsplash.com/photo-1562663474-6cbb3eaa4d14?w=100','145000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1574180566232-aaad1b5b8450?w=400&auto=format&fit=crop" alt="Parket" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Premium</span>
              <div class="prod-card__name">Massiv Parket "Walnut" 20mm</div>
              <div class="prod-card__desc">100% tabiiy yong'oq yog'och. Qayta ishlash mumkin.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">480 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Massiv Parket Walnut','laminat','https://images.unsplash.com/photo-1574180566232-aaad1b5b8450?w=100','480000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&auto=format&fit=crop" alt="SPC pol" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Yangi</span>
              <div class="prod-card__name">SPC Vinyl Pol "Bamboo" 5mm</div>
              <div class="prod-card__desc">100% suv o'tkazmaydigan. Hammom va oshxona uchun ham.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">195 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'SPC Vinyl Pol Bamboo','laminat','https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=100','195000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=400&auto=format&fit=crop" alt="Laminat plintus" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Omborda bor</span>
              <div class="prod-card__name">MDF Plintus 60mm (2.4 m)</div>
              <div class="prod-card__desc">Laminat va parket uchun mos plintus. Ko'p ranglar.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">28 000 <span>so'm/dona</span></div>
                <button class="add-btn" onclick="addToCart(this,'MDF Plintus 60mm','laminat','https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=100','28000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=400&auto=format&fit=crop" alt="Podlozhka" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Kerakli</span>
              <div class="prod-card__name">Laminat Ostligi 3mm (10 m²)</div>
              <div class="prod-card__desc">Shovqin kamaytiruvchi va issiqlik saqlovchi podlozhka.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">42 000 <span>so'm/rulon</span></div>
                <button class="add-btn" onclick="addToCart(this,'Laminat Ostligi 3mm','laminat','https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=100','42000')">+ Savat</button>
              </div>
            </div>
          </div>
          <div class="prod-card">
            <img class="prod-card__img" src="https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=400&auto=format&fit=crop" alt="Engineered parket" />
            <div class="prod-card__body">
              <span class="prod-card__badge">Eksport sifat</span>
              <div class="prod-card__name">Injenering Parket "Cherry" 14mm</div>
              <div class="prod-card__desc">Gilos yog'ochi. Issiqlik o'tkazuvchi pol tizimi uchun mos.</div>
              <div class="prod-card__footer">
                <div class="prod-card__price">320 000 <span>so'm/m²</span></div>
                <button class="add-btn" onclick="addToCart(this,'Injenering Parket Cherry','laminat','https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=100','320000')">+ Savat</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== RECOMMENDED ===== -->
  <section id="recommended">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Tavsiyalar</span>
        <h2 class="section-title">Eng ko'p sotib olingan 10 ta mahsulot</h2>
        <p class="section-sub">Har bir toifadan eng mashhur mahsulotlar</p>
      </div>
      <div class="rec-grid" id="recGrid">
        <!-- filled by JS -->
      </div>
    </div>
  </section>

  <!-- ===== CALCULATOR ===== -->
  <section id="calculator">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Hisoblash</span>
        <h2 class="section-title">Material Kalkulyatori</h2>
        <p class="section-sub">Loyihangiz uchun kerakli miqdorni aniqlang</p>
      </div>
      <div class="calc-wrap">
        <div class="calc-info">
          <h3>Nima uchun kalkulyator?</h3>
          <p>Materiallarni ortiqcha yoki kamayib xarid qilishning oldini oling.</p>
          <ul class="calc-tips">
            <li><span>📐</span> Kafel va laminat uchun 10% qo'shimcha qoldiq hisoblab oling</li>
            <li><span>🧱</span> Sement miqdori devor qalinligi va hajmga bog'liq</li>
            <li><span>🎨</span> Bo'yoq iste'moli — 1 qatlam uchun 1 L / 10 m²</li>
            <li><span>💡</span> Natijalar taxminiy, ustaning baho berishi tavsiya etiladi</li>
          </ul>
        </div>
        <div class="calc-box">
          <div class="calc-tabs">
            <button class="calc-tab-btn active" onclick="switchCalc('kafel-calc')">Kafel</button>
            <button class="calc-tab-btn" onclick="switchCalc('boyoq-calc')">Bo'yoq</button>
            <button class="calc-tab-btn" onclick="switchCalc('sement-calc')">Sement</button>
          </div>

          <!-- Kafel calc -->
          <div class="calc-panel active" id="kafel-calc">
            <div class="field">
              <label>Uzunlik (m)</label>
              <input type="number" id="k-len" value="4" min="0.1" step="0.1" oninput="calcKafel()" />
            </div>
            <div class="field">
              <label>Kenglik (m)</label>
              <input type="number" id="k-wid" value="3" min="0.1" step="0.1" oninput="calcKafel()" />
            </div>
            <div class="field">
              <label>Qoldiq foizi (%)</label>
              <select id="k-extra" onchange="calcKafel()">
                <option value="10">10% (to'g'ri qirqish)</option>
                <option value="15">15% (burchak qirqishlari)</option>
                <option value="20">20% (diagonal naqsh)</option>
              </select>
            </div>
            <div class="calc-result">
              <p>Jami kerakli maydon</p>
              <strong id="kafelRes">13.2 m²</strong>
            </div>
          </div>

          <!-- Boyoq calc -->
          <div class="calc-panel" id="boyoq-calc">
            <div class="field">
              <label>Xona uzunligi (m)</label>
              <input type="number" id="b-len" value="5" min="0.5" step="0.5" oninput="calcBoyoq()" />
            </div>
            <div class="field">
              <label>Xona kengligi (m)</label>
              <input type="number" id="b-wid" value="4" min="0.5" step="0.5" oninput="calcBoyoq()" />
            </div>
            <div class="field">
              <label>Balandlik (m)</label>
              <input type="number" id="b-h" value="2.8" min="1" step="0.1" oninput="calcBoyoq()" />
            </div>
            <div class="field">
              <label>Qatlamlar soni</label>
              <select id="b-layers" onchange="calcBoyoq()">
                <option value="1">1 qatlam</option>
                <option value="2" selected>2 qatlam</option>
              </select>
            </div>
            <div class="calc-result">
              <p>Kerakli bo'yoq miqdori</p>
              <strong id="boyoqRes">15.1 L</strong>
            </div>
          </div>

          <!-- Sement calc -->
          <div class="calc-panel" id="sement-calc">
            <div class="field">
              <label>Devor uzunligi (m)</label>
              <input type="number" id="s-len" value="10" min="1" step="0.5" oninput="calcSement()" />
            </div>
            <div class="field">
              <label>Devor balandligi (m)</label>
              <input type="number" id="s-h" value="3" min="1" step="0.1" oninput="calcSement()" />
            </div>
            <div class="field">
              <label>Devor qalinligi (sm)</label>
              <input type="number" id="s-t" value="20" min="5" step="5" oninput="calcSement()" />
            </div>
            <div class="calc-result">
              <p>Taxminiy sement miqdori</p>
              <strong id="sementRes">148 kg</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== DELIVERY ===== -->
  <section id="delivery">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">Xizmatlar</span>
        <h2 class="section-title">Nima uchun QurilishMart?</h2>
        <p class="section-sub">Sizga qulay bo'lsin deb ishlaymiz</p>
      </div>
      <div class="delivery-grid">
        <div class="del-card">
          <div class="del-icon">🚛</div>
          <h3>Tezkor Yetkazib Berish</h3>
          <p>Toshkent bo'ylab buyurtma kuni o'zingizga yetkazamiz. 5 tonna gacha bepul.</p>
        </div>
        <div class="del-card">
          <div class="del-icon">💳</div>
          <h3>Qulay To'lov</h3>
          <p>Click, Payme, bank kartasi, naqd yoki muddatli to'lov imkoniyati.</p>
        </div>
        <div class="del-card">
          <div class="del-icon">🔒</div>
          <h3>Sifat Kafolati</h3>
          <p>Barcha mahsulotlar sertifikatlangan. Noto'g'ri chiqsa — almashtirish yoki qaytarish.</p>
        </div>
        <div class="del-card">
          <div class="del-icon">🧑‍🔧</div>
          <h3>Maslahat Xizmati</h3>
          <p>Mutaxassislarimiz mahsulot tanlashda bepul maslahat berishadi.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== B2B ===== -->
  <section id="b2b">
    <div class="container">
      <div class="section-head">
        <span class="section-eyebrow">B2B Hamkorlik</span>
        <h2 class="section-title">Ulgurji va korporativ buyurtmalar</h2>
        <p class="section-sub">Qurilish kompaniyalari, prorablar va rieltorlar uchun maxsus shartlar</p>
      </div>
      <div class="b2b-grid">
        <div class="b2b-perks">
          <div class="b2b-perk">
            <div class="b2b-perk__icon">📦</div>
            <div>
              <h4>Ulgurji Narxlar</h4>
              <p>10+ tonna buyurtmada 15–25% chegirma. Maxsus shartnoma shartlari.</p>
            </div>
          </div>
          <div class="b2b-perk">
            <div class="b2b-perk__icon">📋</div>
            <div>
              <h4>Hisob-kitob (Invoice)</h4>
              <p>Yuridik shaxslar uchun hisob-faktura, aktlar va hisobot hujjatlari.</p>
            </div>
          </div>
          <div class="b2b-perk">
            <div class="b2b-perk__icon">🚚</div>
            <div>
              <h4>Qurilish Maydoniga Yetkazish</h4>
              <p>Kran va yuk mashinalari bilan bevosita qurilish maydoniga.</p>
            </div>
          </div>
          <div class="b2b-perk">
            <div class="b2b-perk__icon">🤝</div>
            <div>
              <h4>Shaxsiy Menejer</h4>
              <p>Har bir B2B mijozga alohida menejer. 7/24 aloqa.</p>
            </div>
          </div>
        </div>

        <!-- CART / ORDER SUMMARY -->
        <div class="b2b-order">
          <div class="b2b-order__head">
            <h3>🛒 Buyurtma Jadvali</h3>
            <span id="cartCount">0 mahsulot</span>
          </div>
          <div class="b2b-order__body">
            <div class="cart-items" id="cartItems">
              <div class="cart-empty">
                <div class="empty-icon">🛒</div>
                <p>Hali mahsulot qo'shilmagan.<br>Katalogdan mahsulot tanlang.</p>
              </div>
            </div>
            <div class="cart-footer">
              <div class="cart-totals" id="cartTotals" style="display:none">
                <div class="cart-row"><span>Mahsulotlar:</span><span id="itemCount">0</span></div>
                <div class="cart-row"><span>Yetkazib berish:</span><span>Bepul</span></div>
                <div class="cart-row total"><span>Jami summa:</span><span id="totalSum">0 so'm</span></div>
              </div>
              <button class="order-btn" id="orderBtn" disabled onclick="openOrderModal()">
                📋 Buyurtma Berish
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo" style="color:#fff;">⚙ Qurilish<span style="color:var(--orange)">Mart</span></div>
          <p>O'zbekistondagi eng yirik qurilish mollari internet-do'koni. Sifat, narx va tezlik kafolati.</p>
          <div style="display:flex;gap:10px;">
            <a href="#" style="color:#9ca3af;font-size:20px;">📱</a>
            <a href="#" style="color:#9ca3af;font-size:20px;">💬</a>
            <a href="#" style="color:#9ca3af;font-size:20px;">📷</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Katalog</h4>
          <a href="#">Sement va Qurilish</a>
          <a href="#">Kafel va Plitka</a>
          <a href="#">Bo'yoq va Lak</a>
          <a href="#">Laminat va Parket</a>
        </div>
        <div class="footer-col">
          <h4>Xizmatlar</h4>
          <a href="#">Yetkazib berish</a>
          <a href="#">Kalkulyator</a>
          <a href="#">B2B Hamkorlik</a>
          <a href="#">Maslahat</a>
        </div>
        <div class="footer-col">
          <h4>Aloqa</h4>
          <a href="tel:+998712345678">+998 71 234-56-78</a>
          <a href="mailto:info@qurilishmart.uz">info@qurilishmart.uz</a>
          <a href="#">Toshkent, Chilonzor</a>
          <a href="#">Dush–Shan: 9:00–18:00</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 QurilishMart. Barcha huquqlar himoyalangan.</span>
        <div style="display:flex;gap:16px;">
          <a href="#">Maxfiylik siyosati</a>
          <a href="#">Foydalanish shartlari</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ===== ORDER MODAL ===== -->
  <div class="modal-overlay" id="orderModal">
    <div class="modal">
      <h3>✅ Buyurtmani tasdiqlash</h3>
      <p>Menejerimiz siz bilan 15 daqiqa ichida bog'lanadi va buyurtmani rasmiylashtiramiz.</p>
      <div class="field">
        <label>Ism va familiya</label>
        <input type="text" placeholder="Aziz Karimov" id="orderName" />
      </div>
      <div class="field">
        <label>Telefon raqami</label>
        <input type="tel" placeholder="+998 90 123-45-67" id="orderPhone" />
      </div>
      <div class="modal-actions">
        <button class="btn btn--outline" onclick="closeOrderModal()">Bekor qilish</button>
        <button class="btn btn--primary" onclick="confirmOrder()">📋 Tasdiqlash</button>
      </div>
    </div>
  </div>

  <!-- ===== TOAST ===== -->
  <div class="toast" id="toast">
    <span id="toastIcon">✅</span>
    <span id="toastMsg">Mahsulot savatga qo'shildi</span>
  </div>

  <!-- ===== JAVASCRIPT ===== -->
  <script>
    // ---- State ----
    let cart = [];

    // ---- Recommended products ----
    const RECOMMENDED = [
      { rank:1,  name:"Portland Sement M400",    cat:"Sement",  price:78000,  img:"https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=200&auto=format&fit=crop", unit:"qop" },
      { rank:2,  name:"Interior Emulsion Bo'yoq", cat:"Bo'yoq",  price:185000, img:"https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=200&auto=format&fit=crop", unit:"qut" },
      { rank:3,  name:"Pol Plitka Granito 60×60", cat:"Kafel",   price:120000, img:"https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=200&auto=format&fit=crop", unit:"m²" },
      { rank:4,  name:"Laminat Oak Natural 8mm",  cat:"Laminat", price:145000, img:"https://images.unsplash.com/photo-1562663474-6cbb3eaa4d14?w=200&auto=format&fit=crop", unit:"m²" },
      { rank:5,  name:"Armatura d=12mm",          cat:"Sement",  price:18500,  img:"https://images.unsplash.com/photo-1590593162201-f67611a18b87?w=200&auto=format&fit=crop", unit:"m" },
      { rank:6,  name:"Hammom Kafel Aqua 20×40",  cat:"Kafel",   price:65000,  img:"https://images.unsplash.com/photo-1574362848149-11496d93a7c7?w=200&auto=format&fit=crop", unit:"m²" },
      { rank:7,  name:"Fasad Bo'yoq Exterior",    cat:"Bo'yoq",  price:320000, img:"https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=200&auto=format&fit=crop", unit:"qut" },
      { rank:8,  name:"SPC Vinyl Pol Bamboo",     cat:"Laminat", price:195000, img:"https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=200&auto=format&fit=crop", unit:"m²" },
      { rank:9,  name:"Qurilish G'ishti",         cat:"Sement",  price:1200,   img:"https://images.unsplash.com/photo-1597173791720-87ec8a2a9bef?w=200&auto=format&fit=crop", unit:"dona" },
      { rank:10, name:"Kafel Yopishqogi C1",      cat:"Kafel",   price:45000,  img:"https://images.unsplash.com/photo-1637614589439-02a11a59f8cf?w=200&auto=format&fit=crop", unit:"qop" }
    ];

    function buildRecommended() {
      const grid = document.getElementById('recGrid');
      grid.innerHTML = RECOMMENDED.map(p => `
        <div class="rec-card">
          <img class="rec-card__img" src="${p.img}" alt="${p.name}" loading="lazy" />
          <div class="rec-card__body">
            <div class="rec-rank">${p.rank}</div>
            <div class="rec-card__name">${p.name}</div>
            <div class="rec-card__cat">${p.cat}</div>
            <div class="rec-card__price">${p.price.toLocaleString()} <small>so'm/${p.unit}</small></div>
            <button class="rec-add-btn" onclick="addToCart(this,'${p.name}','${p.cat}','${p.img}','${p.price}')">
              + Savatga qo'shish
            </button>
          </div>
        </div>
      `).join('');
    }
    buildRecommended();

    // ---- Category tabs ----
    function switchCat(id) {
      document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.products-panel').forEach(p => p.classList.remove('active'));
      document.getElementById('tab-' + id).classList.add('active');
      document.getElementById('panel-' + id).classList.add('active');
    }

    // ---- Calculator ----
    function switchCalc(id) {
      document.querySelectorAll('.calc-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.calc-panel').forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById(id).classList.add('active');
    }

    function calcKafel() {
      const len = parseFloat(document.getElementById('k-len').value) || 0;
      const wid = parseFloat(document.getElementById('k-wid').value) || 0;
      const extra = parseFloat(document.getElementById('k-extra').value) || 10;
      const area = len * wid * (1 + extra / 100);
      document.getElementById('kafelRes').textContent = area.toFixed(1) + ' m²';
    }
    calcKafel();

    function calcBoyoq() {
      const len = parseFloat(document.getElementById('b-len').value) || 0;
      const wid = parseFloat(document.getElementById('b-wid').value) || 0;
      const h   = parseFloat(document.getElementById('b-h').value) || 0;
      const lay = parseFloat(document.getElementById('b-layers').value) || 1;
      const perimeter = 2 * (len + wid);
      const area = perimeter * h;
      const liters = (area / 10) * lay;
      document.getElementById('boyoqRes').textContent = liters.toFixed(1) + ' L';
    }
    calcBoyoq();

    function calcSement() {
      const len = parseFloat(document.getElementById('s-len').value) || 0;
      const h   = parseFloat(document.getElementById('s-h').value) || 0;
      const t   = parseFloat(document.getElementById('s-t').value) || 20;
      const vol = len * h * (t / 100);
      const kg  = vol * 370;
      document.getElementById('sementRes').textContent = Math.round(kg) + ' kg';
    }
    calcSement();

    // ---- Cart ----
    function addToCart(btn, name, cat, img, price) {
      const existing = cart.find(i => i.name === name);
      if (existing) {
        existing.qty++;
      } else {
        cart.push({ name, cat, img, price: parseInt(price), qty: 1 });
      }
      renderCart();
      showToast('✅', `"${name}" savatga qo'shildi`);
      if (btn) {
        const orig = btn.textContent;
        btn.textContent = '✓ Qo\'shildi';
        btn.classList.add('added');
        setTimeout(() => { btn.textContent = orig; btn.classList.remove('added'); }, 1500);
      }
    }

    function changeQty(name, delta) {
      const item = cart.find(i => i.name === name);
      if (!item) return;
      item.qty += delta;
      if (item.qty <= 0) cart = cart.filter(i => i.name !== name);
      renderCart();
    }

    function removeItem(name) {
      cart = cart.filter(i => i.name !== name);
      renderCart();
    }

    function renderCart() {
      const container = document.getElementById('cartItems');
      const badge = document.getElementById('cartCountBadge');
      const countEl = document.getElementById('cartCount');
      const totalsEl = document.getElementById('cartTotals');
      const orderBtn = document.getElementById('orderBtn');
      const totalSumEl = document.getElementById('totalSum');
      const itemCountEl = document.getElementById('itemCount');

      const totalQty = cart.reduce((s, i) => s + i.qty, 0);
      const totalSum = cart.reduce((s, i) => s + i.qty * i.price, 0);

      badge.textContent = totalQty;
      countEl.textContent = totalQty + ' mahsulot';

      if (cart.length === 0) {
        container.innerHTML = `<div class="cart-empty"><div class="empty-icon">🛒</div><p>Hali mahsulot qo'shilmagan.<br>Katalogdan mahsulot tanlang.</p></div>`;
        totalsEl.style.display = 'none';
        orderBtn.disabled = true;
      } else {
        container.innerHTML = cart.map(item => `
          <div class="cart-item">
            <img class="cart-item__img" src="${item.img}" alt="${item.name}" />
            <div class="cart-item__info">
              <div class="cart-item__name">${item.name}</div>
              <div class="cart-item__cat">${item.cat}</div>
            </div>
            <div class="cart-item__qty">
              <button class="qty-btn" onclick="changeQty('${item.name}', -1)">−</button>
              <span class="qty-val">${item.qty}</span>
              <button class="qty-btn" onclick="changeQty('${item.name}', +1)">+</button>
            </div>
            <div class="cart-item__price">${(item.qty * item.price).toLocaleString()} so'm</div>
            <button class="cart-item__del" onclick="removeItem('${item.name}')">🗑</button>
          </div>
        `).join('');
        itemCountEl.textContent = totalQty + ' ta';
        totalSumEl.textContent = totalSum.toLocaleString() + ' so\'m';
        totalsEl.style.display = 'block';
        orderBtn.disabled = false;
      }
    }

    // ---- Modal ----
    function openOrderModal() {
      document.getElementById('orderModal').classList.add('open');
    }
    function closeOrderModal() {
      document.getElementById('orderModal').classList.remove('open');
    }
    function confirmOrder() {
      const name = document.getElementById('orderName').value.trim();
      const phone = document.getElementById('orderPhone').value.trim();
      if (!name || !phone) { showToast('⚠️', 'Ism va telefon raqamini kiriting'); return; }
      closeOrderModal();
      cart = [];
      renderCart();
      showToast('🎉', 'Buyurtma qabul qilindi! Tez orada aloqaga chiqamiz.');
    }
    document.getElementById('orderModal').addEventListener('click', function(e) {
      if (e.target === this) closeOrderModal();
    });

    // ---- Toast ----
    let toastTimer;
    function showToast(icon, msg) {
      clearTimeout(toastTimer);
      document.getElementById('toastIcon').textContent = icon;
      document.getElementById('toastMsg').textContent = msg;
      const t = document.getElementById('toast');
      t.classList.add('show');
      toastTimer = setTimeout(() => t.classList.remove('show'), 3000);
    }
  </script>
</body>
</html>
'''

components.html(HTML_CONTENT, height=5000, scrolling=False)
