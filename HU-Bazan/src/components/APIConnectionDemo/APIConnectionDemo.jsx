import React, { useState, useEffect } from 'react';
import { Card, Button, Alert, Spin, Tag, Space, Typography, Divider } from 'antd';
import { CheckCircle, XCircle, LoadingOutlined, ApiOutlined, DatabaseOutlined, GlobalOutlined } from '@ant-design/icons';
import axios from 'axios';

const { Title, Text } = Typography;

const APIConnectionDemo = () => {
  const [connectionStatus, setConnectionStatus] = useState({
    django: 'checking',
    hu02: 'checking',
    hu05: 'checking',
    react: 'checking'
  });
  const [testResults, setTestResults] = useState({});
  const [loading, setLoading] = useState(true);

  const testEndpoint = async (name, url, method = 'GET') => {
    try {
      const response = await axios({
        method,
        url,
        timeout: 5000,
        headers: {
          'Content-Type': 'application/json',
        }
      });
      return { success: true, status: response.status, data: response.data };
    } catch (error) {
      return { 
        success: false, 
        status: error.response?.status || 'No response',
        error: error.message 
      };
    }
  };

  const runConnectionTests = async () => {
    setLoading(true);
    
    // Test Django server
    const djangoTest = await testEndpoint('Django', 'http://127.0.0.1:8000/api/');
    
    // Test HU02 Profile Management
    const hu02Test = await testEndpoint('HU02', 'http://127.0.0.1:8000/api/profile/me/');
    
    // Test HU05 User Search
    const hu05Test = await testEndpoint('HU05', 'http://127.0.0.1:8000/api/users/search/');
    
    // Test React frontend
    const reactTest = await testEndpoint('React', 'http://localhost:5174/');

    setConnectionStatus({
      django: djangoTest.success ? 'connected' : 'disconnected',
      hu02: hu02Test.success ? 'connected' : 'disconnected',
      hu05: hu05Test.success ? 'connected' : 'disconnected',
      react: reactTest.success ? 'connected' : 'disconnected'
    });

    setTestResults({
      django: djangoTest,
      hu02: hu02Test,
      hu05: hu05Test,
      react: reactTest
    });

    setLoading(false);
  };

  useEffect(() => {
    runConnectionTests();
  }, []);

  const getStatusIcon = (status) => {
    switch (status) {
      case 'connected':
        return <CheckCircle style={{ color: '#52c41a' }} />;
      case 'disconnected':
        return <XCircle style={{ color: '#ff4d4f' }} />;
      case 'checking':
        return <LoadingOutlined style={{ color: '#1890ff' }} />;
      default:
        return <LoadingOutlined />;
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'connected':
        return 'success';
      case 'disconnected':
        return 'error';
      case 'checking':
        return 'processing';
      default:
        return 'default';
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'connected':
        return 'Conectado';
      case 'disconnected':
        return 'Desconectado';
      case 'checking':
        return 'Verificando...';
      default:
        return 'Desconocido';
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <Card>
        <Title level={2} style={{ textAlign: 'center', marginBottom: '20px' }}>
          🔗 Demostración de Conexión API
        </Title>
        
        <Alert
          message="Estado de Conexión del Sistema"
          description="Verificación en tiempo real de la conectividad entre React y Django"
          type="info"
          showIcon
          style={{ marginBottom: '20px' }}
        />

        <Space direction="vertical" size="large" style={{ width: '100%' }}>
          {/* Django Backend */}
          <Card size="small" title={
            <Space>
              <DatabaseOutlined />
              <Text strong>Backend Django</Text>
            </Space>
          }>
            <Space direction="vertical" style={{ width: '100%' }}>
              <Space>
                {getStatusIcon(connectionStatus.django)}
                <Tag color={getStatusColor(connectionStatus.django)}>
                  {getStatusText(connectionStatus.django)}
                </Tag>
                <Text code>http://127.0.0.1:8000/</Text>
              </Space>
              {testResults.django && (
                <Text type="secondary">
                  Status: {testResults.django.status} | 
                  {testResults.django.success ? ' ✅ Funcionando' : ' ❌ Error: ' + testResults.django.error}
                </Text>
              )}
            </Space>
          </Card>

          {/* HU02 Profile Management */}
          <Card size="small" title={
            <Space>
              <ApiOutlined />
              <Text strong>Módulo HU02 - Gestión de Perfiles</Text>
            </Space>
          }>
            <Space direction="vertical" style={{ width: '100%' }}>
              <Space>
                {getStatusIcon(connectionStatus.hu02)}
                <Tag color={getStatusColor(connectionStatus.hu02)}>
                  {getStatusText(connectionStatus.hu02)}
                </Tag>
                <Text code>http://127.0.0.1:8000/api/profile/</Text>
              </Space>
              {testResults.hu02 && (
                <Text type="secondary">
                  Status: {testResults.hu02.status} | 
                  {testResults.hu02.success ? ' ✅ Funcionando' : ' ❌ Error: ' + testResults.hu02.error}
                </Text>
              )}
            </Space>
          </Card>

          {/* HU05 User Search */}
          <Card size="small" title={
            <Space>
              <ApiOutlined />
              <Text strong>Módulo HU05 - Búsqueda de Usuarios</Text>
            </Space>
          }>
            <Space direction="vertical" style={{ width: '100%' }}>
              <Space>
                {getStatusIcon(connectionStatus.hu05)}
                <Tag color={getStatusColor(connectionStatus.hu05)}>
                  {getStatusText(connectionStatus.hu05)}
                </Tag>
                <Text code>http://127.0.0.1:8000/api/users/</Text>
              </Space>
              {testResults.hu05 && (
                <Text type="secondary">
                  Status: {testResults.hu05.status} | 
                  {testResults.hu05.success ? ' ✅ Funcionando' : ' ❌ Error: ' + testResults.hu05.error}
                </Text>
              )}
            </Space>
          </Card>

          {/* React Frontend */}
          <Card size="small" title={
            <Space>
              <GlobalOutlined />
              <Text strong>Frontend React</Text>
            </Space>
          }>
            <Space direction="vertical" style={{ width: '100%' }}>
              <Space>
                {getStatusIcon(connectionStatus.react)}
                <Tag color={getStatusColor(connectionStatus.react)}>
                  {getStatusText(connectionStatus.react)}
                </Tag>
                <Text code>http://localhost:5174/</Text>
              </Space>
              {testResults.react && (
                <Text type="secondary">
                  Status: {testResults.react.status} | 
                  {testResults.react.success ? ' ✅ Funcionando' : ' ❌ Error: ' + testResults.react.error}
                </Text>
              )}
            </Space>
          </Card>
        </Space>

        <Divider />

        <Space direction="vertical" style={{ width: '100%' }}>
          <Button 
            type="primary" 
            onClick={runConnectionTests}
            loading={loading}
            icon={<ApiOutlined />}
            size="large"
            style={{ width: '100%' }}
          >
            🔄 Actualizar Estado de Conexión
          </Button>

          <Alert
            message="Información de Conexión"
            description={
              <div>
                <p><strong>Backend Django:</strong> Servidor API en Python</p>
                <p><strong>HU02:</strong> Gestión de perfiles de usuario</p>
                <p><strong>HU05:</strong> Búsqueda y filtros de usuarios</p>
                <p><strong>Frontend React:</strong> Interfaz de usuario</p>
              </div>
            }
            type="success"
            showIcon
          />
        </Space>
      </Card>
    </div>
  );
};

export default APIConnectionDemo;
