import React, { useState } from 'react';
import api from '../services/api';

function ConsultaCliente() {
  const [cpf, setCpf] = useState('');
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);

  const consultar = async () => {
    setLoading(true);
    try {
      const res = await api.get(`/clientes/${cpf}`);
      setResultado(res.data);
    } catch (error) {
      setResultado({ erro: error.response?.data?.detail || "Cliente não encontrado" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Consultar Cliente</h2>
      <input
        value={cpf}
        onChange={(e) => setCpf(e.target.value)}
        placeholder="CPF para consulta"
      />
      <button onClick={consultar} disabled={loading}>
        {loading ? 'Consultando...' : 'Consultar SERASA e CDL'}
      </button>

      {resultado && (
        <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ccc' }}>
          {resultado.erro ? (
            <p style={{ color: 'red' }}>{resultado.erro}</p>
          ) : (
            <>
              <h3>Cliente: {resultado.cliente.nome}</h3>
              <p><strong>CPF:</strong> {resultado.cliente.cpf}</p>
              <p><strong>Score:</strong> {resultado.score}/100</p>
              <p><strong>Status:</strong> 
                <span style={{ color: resultado.status === 'Aprovado' ? 'green' : 'red' }}>
                  {' '} {resultado.status}
                </span>
              </p>
              <p><strong>Restrições:</strong> {resultado.restricoes.join(', ')}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default ConsultaCliente;