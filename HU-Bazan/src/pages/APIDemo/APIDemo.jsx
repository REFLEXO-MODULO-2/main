import React from 'react';
import APIConnectionDemo from '../../components/APIConnectionDemo/APIConnectionDemo';

const APIDemo = () => {
  return (
    <div style={{ 
      minHeight: '100vh', 
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      padding: '20px'
    }}>
      <APIConnectionDemo />
    </div>
  );
};

export default APIDemo;
