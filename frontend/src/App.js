import React from 'react';
import CadastroCliente from './components/CadastroCliente';
import ConsultaCliente from './components/ConsultaCliente';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Sistema de Avaliação de Crédito</h1>
      </header>
      <main>
        <CadastroCliente />
        <ConsultaCliente />
      </main>
    </div>
  );
}

export default App;