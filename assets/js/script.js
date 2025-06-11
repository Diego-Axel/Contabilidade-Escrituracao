// Dados
const entries = [];


// Elementos
const form = document.getElementById('entryForm');
const diarioBody = document.querySelector('#diario tbody');
const razaoDiv = document.getElementById('razaoContent');
const taccDiv = document.getElementById('taccountsContent');
const balAtivo = document.getElementById('balancoAtivo');
const balPass = document.getElementById('balancoPassivo');
const tabs = document.querySelectorAll('.tab');


// Navegação entre abas
tabs.forEach(tab => tab.addEventListener('click', () => {
  document.querySelectorAll('.tab, .section').forEach(el => el.classList.remove('active'));
  tab.classList.add('active');
  document.getElementById(tab.dataset.target).classList.add('active');
}));


// Submissão do formulário
form.addEventListener('submit', e => {
  e.preventDefault();
  const date = document.getElementById('entryDate').value;
  const account = document.getElementById('entryAccount').value;
  const desc = document.getElementById('entryDesc').value;
  const value = parseFloat(document.getElementById('entryValue').value);
  const type = document.getElementById('entryType').value;
  entries.push({ date, account, desc, value, type });
  renderAll();
  form.reset();
  document.getElementById('entryDate').valueAsDate = new Date();
});


// Renderização geral
function renderAll() {
  renderDiario();
  renderRazao();
  renderTAccounts();
  renderBalanco();
}


function renderDiario() {
  diarioBody.innerHTML = entries
    .sort((a, b) => new Date(a.date) - new Date(b.date))
    .map(e => `
      <tr>
        <td>${e.date}</td>
        <td>${e.account}</td>
        <td>${e.desc}</td>
        <td>${e.type}</td>
        <td>${e.value.toFixed(2)}</td>
      </tr>
  `).join('');
}


function groupByAccount() {
  return entries.reduce((acc, e) => {
    acc[e.account] = acc[e.account] || [];
    acc[e.account].push(e);
    return acc;
  }, {});
}


function renderRazao() {
  const groups = groupByAccount();
  razaoDiv.innerHTML = Object.entries(groups).map(([acc, items]) => {
    const total = items.reduce((sum, e) => sum + (e.type === 'debito' ? e.value : -e.value), 0);
    return `
      <h3>${acc}</h3>
      <table>
        <thead>
          <tr><th>Data</th><th>Descrição</th><th>Débito</th><th>Crédito</th><th>Saldo</th></tr>
        </thead>
        <tbody>
          ${items.map(e => {
            const debit = e.type === 'debito' ? e.value.toFixed(2) : '';
            const credit = e.type === 'credito' ? e.value.toFixed(2) : '';
            return `<tr>
              <td>${e.date}</td>
              <td>${e.desc}</td>
              <td>${debit}</td>
              <td>${credit}</td>
              <td></td>
            </tr>`;
          }).join('')}
        </tbody>
        <tfoot>
          <tr><td colspan="4">Saldo</td><td>${total.toFixed(2)}</td></tr>
        </tfoot>
      </table>
    `;
  }).join('');
}


function renderTAccounts() {
  const groups = groupByAccount();
  taccDiv.innerHTML = Object.entries(groups).map(([acc, items]) => {
    const rows = items.map(e => {
      const d = e.type === 'debito' ? e.value.toFixed(2) : '';
      const c = e.type === 'credito' ? e.value.toFixed(2) : '';
      return `<tr><td>${d}</td><td>${c}</td></tr>`;
    }).join('');
    const saldo = items.reduce((sum, e) => sum + (e.type === 'debito' ? e.value : -e.value), 0).toFixed(2);
    return `
      <div class="t-account">
        <strong>${acc}</strong>
        <table>
          <thead><tr><th>D</th><th>C</th></tr></thead>
          <tbody>${rows}</tbody>
          <tfoot><tr><td colspan="2">Saldo: ${saldo}</td></tr></tfoot>
        </table>
      </div>
    `;
  }).join('');
}


function renderBalanco() {
  const groups = groupByAccount();
  let ativoTotal = 0, passTotal = 0;
  balAtivo.innerHTML = Object.entries(groups).map(([acc, items]) => {
    const sum = items.reduce((s, e) => s + (e.type === 'debito' ? e.value : 0), 0);
    ativoTotal += sum;
    return `<tr><td>${acc}</td><td>${sum.toFixed(2)}</td></tr>`;
  }).join('');
  balPass.innerHTML = Object.entries(groups).map(([acc, items]) => {
    const sum = items.reduce((s, e) => s + (e.type === 'credito' ? e.value : 0), 0);
    passTotal += sum;
    return `<tr><td>${acc}</td><td>${sum.toFixed(2)}</td></tr>`;
  }).join('');
  balAtivo.innerHTML += `<tr><th>Total Ativo</th><th>${ativoTotal.toFixed(2)}</th></tr>`;
  balPass.innerHTML += `<tr><th>Total Passivo+PL</th><th>${passTotal.toFixed(2)}</th></tr>`;
}


// Inicializa data padrão
window.onload = () => {
  document.getElementById('entryDate').valueAsDate = new Date();
};