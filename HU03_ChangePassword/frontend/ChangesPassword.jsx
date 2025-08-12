import React, { useState } from 'react';
import { useChangePassword } from '../../../hooks/authHook';

const ChangesPassword = () => {
const [form, setForm] = useState({
    email: '',
    current_password: '',
    new_password: '',
    confirm_password: '',
});
const [mensaje, setMensaje] = useState('');
const { changePassword } = useChangePassword();

const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
};

const handleSubmit = async (e) => {
    e.preventDefault();
    if (form.new_password !== form.confirm_password) {
    setMensaje('Las contraseñas no coinciden');
    return;
    }
    try {
    const result = await changePassword({
        email: form.email,
        current_password: form.current_password,
        new_password: form.new_password,
    });
    setMensaje('Contraseña cambiada correctamente');
    } catch (error) {
    setMensaje(error.message || 'Error inesperado');
    }
};

return (
    <form onSubmit={handleSubmit}>
    <input type="email" name="email" placeholder="Email" onChange={handleChange} />
    <input type="password" name="current_password" placeholder="Contraseña actual" onChange={handleChange} />
    <input type="password" name="new_password" placeholder="Nueva contraseña" onChange={handleChange} />
    <input type="password" name="confirm_password" placeholder="Confirmar nueva contraseña" onChange={handleChange} />
    <button type="submit">Cambiar Contraseña</button>
    <p>{mensaje}</p>
    </form>
);
};

export default ChangesPassword;
