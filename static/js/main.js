// ─── Toast Notifications ────────────────────────────────────────────────────
function showToast(message, type = 'info', duration = 3000) {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    document.body.appendChild(container);
  }
  const icons = { success: '✅', error: '❌', info: 'ℹ️' };
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${icons[type] || ''}</span><span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), duration);
}

// ─── API Helper ─────────────────────────────────────────────────────────────
async function api(path, options = {}) {
  const defaults = {
    headers: { 'Content-Type': 'application/json' },
    credentials: 'same-origin'
  };
  const res = await fetch(path, { ...defaults, ...options });
  if (res.status === 401) { window.location.href = '/login'; return null; }
  return res;
}

// ─── Modal Helpers ───────────────────────────────────────────────────────────
function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('open');
}
function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('open');
}
function closeAllModals() {
  document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
}

// Close modal on overlay click
document.addEventListener('click', e => {
  if (e.target.classList.contains('modal-overlay')) closeAllModals();
});

// ─── Logout ─────────────────────────────────────────────────────────────────
async function logout() {
  await api('/api/auth/logout', { method: 'POST' });
  window.location.href = '/login';
}

// ─── Badge Helper ────────────────────────────────────────────────────────────
function reviewBadge(status) {
  return status === 'confirmed'
    ? '<span class="badge badge-confirmed">✓ Confirmed</span>'
    : '<span class="badge badge-pending">⏳ Pending</span>';
}
function statusBadge(status) {
  const map = {
    'Open': 'badge-open',
    'In Progress': 'badge-progress',
    'Awaiting Parts': 'badge-waiting',
    'Closed': 'badge-closed'
  };
  return `<span class="badge ${map[status] || 'badge-open'}">${status}</span>`;
}

// ─── Format Helpers ──────────────────────────────────────────────────────────
function fmtDowntime(mins) {
  if (!mins) return '—';
  if (mins < 60) return `${mins} min`;
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  return m ? `${h}h ${m}m` : `${h}h`;
}
function fmtDate(d) {
  if (!d) return '—';
  const dt = new Date(d + 'T00:00:00');
  return dt.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
}
