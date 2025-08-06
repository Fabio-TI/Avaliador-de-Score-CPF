import React, { useState } from 'react';
import api from '../services/api';

function CadastroCliente() {
  const [formData, setFormData] = useState({
    cpf: '',
    nome: '',
    telefone: '',
    cep: '',
  });
  const [mensagem, setMensagem] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/clientes/', formData);
      setMensagem("Cliente cadastrado com sucesso!");
    } catch (error) {
      setMensagem(`Erro: ${error.response?.data?.detail || error.message}`);
    }
  };

  return (
    <div>
      <h2>Cadastrar Cliente</h2>
      <form onSubmit={handleSubmit}>
        <input name="cpf" placeholder="CPF (somente números)" value={formData.cpf} onChange={handleChange} required />
        <input name="nome" placeholder="Nome" value={formData.nome} onChange={handleChange} required />
        <input name="telefone" placeholder="Telefone" value={formData.telefone} onChange={handleChange} required />
        <input name="cep" placeholder="CEP" value={formData.cep} onChange={handleChange} required />
        <button type="submit">Cadastrar</button>
      </form>
      {mensagem && <p>{mensagem}</p>}
    </div>
  );
}

export default CadastroCliente;